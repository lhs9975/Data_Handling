# read hdf5 file format
import h5py

# HDF5 파일 열기
file_path = r"G:\181213 공주역\0000056382_2018-12-13_01.39.45.76914.hdf5"
with h5py.File(file_path, 'r') as hdf:
    # 루트 그룹의 키 목록 출력
    def print_keys(name, obj):
        if isinstance(obj, h5py.Dataset):
            print(f"Dataset: {name}, Shape: {obj.shape}, DataType: {obj.dtype}")

    print("Keys in the file:")
    hdf.visititems(print_keys)