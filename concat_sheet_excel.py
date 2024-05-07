import os
import pandas as pd

# Directory containing Excel files
directory = "/home/aptech/projects/test/data/excel/data1.xlsx"

# Create an empty DataFrame to store concatenated data
all_temp_data = pd.DataFrame()

# Iterate over each file in the directory
for filename in directory:
    if filename.endswith(".xlsx"):  # Check if file is Excel file
        # Import Excel file
        filepath = os.path.join(directory, filename)
        data = pd.read_excel(filepath, sheet_name=None, engine='openpyxl')

        # Create a single DataFrame by vertically connecting only the temperature data on all sheets
        temp_data_per_file = pd.DataFrame()
        for sheet_name, df in data.items():
            temp_data = df.iloc[:10000, 1]  # Select only 2nd column for temperature data
            temp_data_per_file = pd.concat([temp_data_per_file, temp_data], axis=1)

        # Concatenate data from each file horizontally
        all_temp_data = pd.concat([all_temp_data, temp_data_per_file], axis=1)

# Save the concatenated data to a new Excel file
output_filepath = r"C:\Users\MSI\Desktop\회사\개발\MLTA\dataset\company_data\trace_data_excel\concat_time_60\concat_time_60_2.xlsx"
all_temp_data.to_excel(output_filepath, index=False, header=False)

print("The data from all Excel files in the folder have been concatenated and saved as:", output_filepath)
