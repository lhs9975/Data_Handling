# import os
# import h5py
#
#
# def copy_group_structure(src_group, dst_group, start_idx, end_idx):
#     """
#     src_group 내부의 모든 subgroup, dataset을 순회하며
#     - 그룹이면: 동일한 이름으로 dst_group에 그룹을 생성하고 재귀적으로 복사
#     - 데이터셋이면: 첫 번째 축(0번째 차원)을 [start_idx:end_idx] 슬라이싱하여 dst_group에 복사
#     (만약 데이터셋이 스칼라 또는 1D 미만이면 전체 복사)
#     """
#     # 그룹 Attributes 복사
#     for attr_name, attr_value in src_group.attrs.items():
#         dst_group.attrs[attr_name] = attr_value
#
#     for name, item in src_group.items():
#         if isinstance(item, h5py.Group):
#             # 그룹이면 동일한 이름의 그룹 생성 후 재귀 복사
#             sub_group = dst_group.create_group(name)
#             copy_group_structure(item, sub_group, start_idx, end_idx)
#         elif isinstance(item, h5py.Dataset):
#             # 데이터셋일 때
#             data_shape = item.shape
#             data_dtype = item.dtype
#
#             # 데이터셋이 스칼라(예: shape=()) 이거나,
#             # 0차원 / 1차원 미만인 경우에는 통째로 복사
#             if (data_shape is None) or (len(data_shape) == 0):
#                 # 스칼라 데이터
#                 dset = dst_group.create_dataset(name, data=item[()])
#             else:
#                 # 최소 1차원 이상인 경우 -> 첫 번째 축 기준으로 슬라이싱
#                 # 예: shape가 (1000, 20, 30) 이면 첫 번째 축은 0번 차원 -> 1000
#                 N = data_shape[0]
#                 # 인덱스 범위가 데이터셋의 실제 길이를 넘어갈 수도 있으니 min 적용
#                 s_start = min(start_idx, N)
#                 s_end = min(end_idx, N)
#
#                 if s_start >= s_end:
#                     # 만약 분할 구간에 해당하는 데이터가 없다면,
#                     # shape=(0, ...)인 비어있는 데이터셋을 생성하거나,
#                     # 혹은 skip할 수도 있음. 여기서는 shape=(0,)+data_shape[1:] 생성 예시.
#
#                     empty_shape = (0,) + data_shape[1:]
#                     dset = dst_group.create_dataset(
#                         name,
#                         shape=empty_shape,
#                         dtype=data_dtype
#                     )
#                 else:
#                     # 슬라이싱해서 부분 데이터를 읽어온다
#                     partial_data = item[s_start:s_end, ...]  # 첫 차원 [s_start:s_end], 나머지는 전체
#                     dset = dst_group.create_dataset(
#                         name,
#                         data=partial_data,
#                         dtype=data_dtype,
#                         compression=item.compression  # 원본의 압축 방식도 복사(있다면)
#                     )
#
#             # 데이터셋 Attributes 복사
#             for attr_name, attr_value in item.attrs.items():
#                 dset.attrs[attr_name] = attr_value
#
#
# def split_hdf5_file(input_hdf5, num_splits=5):
#     """
#     input_hdf5 파일을 열어, 내부에 있는 모든 그룹/데이터셋을
#     첫 번째 차원(0번 축) 기준으로 num_splits 등분하여
#     각각 다른 HDF5 파일에 나누어 저장합니다.
#     예) original_part1.h5, original_part2.h5, ...
#     """
#
#     with h5py.File(input_hdf5, 'r') as f:
#         # 우선, "0번 차원"을 얼마나 나눌지 결정해야 하는데,
#         # 파일 내 여러 데이터셋 중 어떤 것을 기준으로 할지가 문제입니다.
#         # 가장 큰 첫 번째 차원을 가진 데이터셋의 크기를 기준으로 삼는 예시를 들어보겠습니다.
#
#         max_len = 0
#
#         # 파일 최상위 그룹 f를 순회하면서, 가장 큰 첫 번째 축 길이를 찾음
#         def find_max_first_dim(group):
#             nonlocal max_len
#             for name, item in group.items():
#                 if isinstance(item, h5py.Group):
#                     find_max_first_dim(item)
#                 elif isinstance(item, h5py.Dataset):
#                     if (item.shape is not None) and (len(item.shape) > 0):
#                         # 첫 번째 축(0번 차원) 길이
#                         dim0 = item.shape[0]
#                         if dim0 > max_len:
#                             max_len = dim0
#
#         find_max_first_dim(f)
#
#         # 이제 max_len을 num_splits 로 나눈다
#         part_size = max_len // num_splits
#         remainder = max_len % num_splits
#
#         # 각 파트마다 start, end 인덱스를 정의하고,
#         # 그 범위만큼 복사한다.
#         start_idx = 0
#         for i in range(num_splits):
#             # i번째 파트가 가져갈 길이
#             current_part_size = part_size + (1 if i < remainder else 0)
#             end_idx = start_idx + current_part_size
#
#             # 출력 파일명
#             base_name, ext = os.path.splitext(input_hdf5)
#             output_file = f"{base_name}_part{i + 1}{ext}"
#
#             # 새로 만들 HDF5 파일에 구조를 복사
#             with h5py.File(output_file, 'w') as f_out:
#                 copy_group_structure(f, f_out, start_idx, end_idx)
#
#             print(f"Created {output_file}: [{start_idx}:{end_idx}]")
#
#             # 다음 파트로 넘어감
#             start_idx = end_idx
#
#
# # 사용 예시
# if __name__ == "__main__":
#     input_file = r"C:\Users\MSI\Desktop\hdf5_test\data\0000000494_2024-12-19_05.29.12.19054.hdf5"
#     split_hdf5_file(input_file, num_splits=5)

# ----------------------------------------------------------------------------------------------------------------------
#
# import h5py
# import numpy as np
#
# def compare_attributes(obj1, obj2, path):
#     """
#     HDF5 객체(그룹, 데이터셋 등)에 설정된 Attributes(속성)을 비교합니다.
#     """
#     differences = []
#     attrs1 = set(obj1.attrs.keys())
#     attrs2 = set(obj2.attrs.keys())
#
#     # 한쪽에만 있는 attribute
#     for a in sorted(attrs1 - attrs2):
#         differences.append(f"{path}: attribute '{a}' only in file1")
#     for a in sorted(attrs2 - attrs1):
#         differences.append(f"{path}: attribute '{a}' only in file2")
#
#     # 공통 attribute 값 비교
#     for a in sorted(attrs1 & attrs2):
#         v1 = obj1.attrs[a]
#         v2 = obj2.attrs[a]
#         # numpy 배열 형태인지, 스칼라인지 구분해서 비교
#         if isinstance(v1, np.ndarray) and isinstance(v2, np.ndarray):
#             if not np.array_equal(v1, v2):
#                 differences.append(f"{path}: attribute '{a}' differs: {v1} vs {v2}")
#         else:
#             if v1 != v2:
#                 differences.append(f"{path}: attribute '{a}' differs: {v1} vs {v2}")
#
#     return differences
#
# def compare_datasets(dset1, dset2, path):
#     """
#     두 Dataset의 shape, dtype, chunk, compression, attributes 등을 비교합니다.
#     """
#     differences = []
#
#     # Shape 비교
#     if dset1.shape != dset2.shape:
#         differences.append(f"{path}: shape differs {dset1.shape} vs {dset2.shape}")
#
#     # dtype 비교
#     if dset1.dtype != dset2.dtype:
#         differences.append(f"{path}: dtype differs {dset1.dtype} vs {dset2.dtype}")
#
#     # chunk 비교
#     if dset1.chunks != dset2.chunks:
#         differences.append(f"{path}: chunks differ {dset1.chunks} vs {dset2.chunks}")
#
#     # compression 비교
#     if dset1.compression != dset2.compression:
#         differences.append(f"{path}: compression differs {dset1.compression} vs {dset2.compression}")
#     if dset1.compression_opts != dset2.compression_opts:
#         differences.append(f"{path}: compression_opts differs {dset1.compression_opts} vs {dset2.compression_opts}")
#
#     # Attributes 비교
#     differences.extend(compare_attributes(dset1, dset2, path))
#
#     return differences
#
# def compare_groups(g1, g2, path="/"):
#     """
#     재귀적으로 그룹을 순회하며:
#       - 하위 그룹/데이터셋 이름이 동일한지
#       - 각각의 데이터셋이 같은 구조/속성을 가지는지
#     등을 비교합니다.
#     """
#     differences = []
#
#     # 그룹 자체의 Attributes 비교
#     differences.extend(compare_attributes(g1, g2, path))
#
#     # 두 그룹의 key(하위 객체 이름) 비교
#     keys1 = set(g1.keys())
#     keys2 = set(g2.keys())
#
#     # 한쪽에만 있는 키
#     for k in sorted(keys1 - keys2):
#         differences.append(f"{path}: '{k}' present in file1 but not in file2")
#     for k in sorted(keys2 - keys1):
#         differences.append(f"{path}: '{k}' present in file2 but not in file1")
#
#     # 공통 키 비교
#     for k in sorted(keys1 & keys2):
#         item1 = g1[k]
#         item2 = g2[k]
#
#         new_path = (path if path != "/" else "") + "/" + k
#         # 둘 다 Group인지, 둘 다 Dataset인지 체크
#         if isinstance(item1, h5py.Group) and isinstance(item2, h5py.Group):
#             differences.extend(compare_groups(item1, item2, new_path))
#         elif isinstance(item1, h5py.Dataset) and isinstance(item2, h5py.Dataset):
#             differences.extend(compare_datasets(item1, item2, new_path))
#         else:
#             # 하나는 Group, 하나는 Dataset이면 구조가 다름
#             differences.append(f"{new_path}: type mismatch (Group vs Dataset)")
#
#     return differences
#
# def compare_hdf5_files(file1, file2):
#     """
#     두 HDF5 파일을 열어 구조와 메타데이터(Attributes 등)를 비교한 뒤,
#     차이점 목록을 반환합니다.
#     """
#     differences = []
#     with h5py.File(file1, 'r') as f1, h5py.File(file2, 'r') as f2:
#         differences.extend(compare_groups(f1, f2, path="/"))
#     return differences
#
# if __name__ == "__main__":
#     # 여기서 두 개의 HDF5 파일 경로를 직접 지정
#     file1 = r"C:\Users\MSI\Desktop\hdf5_test\split\0000000496_2024-12-19_05.34.12.19054.hdf5"
#     file2 = r"C:\Users\MSI\Desktop\hdf5_test\split\0000000498_2024-12-19_05.35.12.19054.hdf5"
#
#     diffs = compare_hdf5_files(file1, file2)
#     if len(diffs) == 0:
#         print("No differences found. The two HDF5 files are identical in structure/metadata.")
#     else:
#         print("Differences found:")
#         for d in diffs:
#             print("  -", d)

# ----------------------------------------------------------------------------------------------------------------------

