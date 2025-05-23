import pandas as pd
import csv
import shutil
import os

def txt_to_csv(txt_file, csv_file, delimiter=None):
    """
    Convert a TXT file to CSV format.

    Parameters:
        txt_file (str): Path to the input text file.
        csv_file (str): Path to the output CSV file.
        delimiter (str): The delimiter used in the TXT file (comma, space, tab, etc.).
        If None, the script will try to detect it automatically.
    """

    # pass
    # Expand ~ to the full home directory path
    txt_file = os.path.expanduser(txt_file)
    csv_file = os.path.expanduser(csv_file)

    with open(txt_file, 'r', encoding='cp1252') as file: # utf-8, unicode_escape
        lines = file.readlines()

    # Try to auto-detect delimiter if not provided
    if delimiter is None:
        sample_line = lines[0]
        if ',' in sample_line:
            delimiter = ','
        elif '\t' in sample_line:
            delimiter = '\t'
        elif ' ' in sample_line:
            delimiter = ' '
        elif '|' in sample_line:
            delimiter = '|'
        elif '  ' in sample_line: # The space is a tab
            delimiter = '   '
        elif '. ' in sample_line:
            delimiter = '. '
        else:
            raise ValueError("Unable to detect delimiter")

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for line in lines:
            writer.writerow(line.strip().split(delimiter))

    print(f"Conversion completed! CSV file saved as: {csv_file}")

# Example:
# txt_file_path = "~/Documents/UH/hon4350/water_quality/GWDBDownload/GWDBDownload_data/WaterQualityMinor.txt"  
# csv_file_path = "~/Documents/UH/hon4350/water_quality/data/WaterQualityMinor_v1.csv" 
# txt_to_csv(txt_file_path, csv_file_path)

def xslx_to_csv(xlsx_file, csv_file, sheet_name=0):
    """
    Convert an Excel XLSX file to CSV format.

    Parameters:
        xlsx_file (str): Path to the input Excel file.
        csv_file (str): Path to the output CSV file.
        sheet_name (str or int): Name or index of the sheet to convert. Default is the first sheet.
    """

    # Expand ~ to home directory
    xlsx_file = os.path.expanduser(xlsx_file)
    csv_file = os.path.expanduser(csv_file)

    # Read the Excel file
    try:
        df = pd.read_excel(xlsx_file, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    # Save as CSV
    try:
        df.to_csv(csv_file, index=False)
        print(f"Conversion completed! CSV file saved as: {csv_file}")
    except Exception as e:
        print(f"Error writing CSV file: {e}")

# xlsx_file_path = "~/Documents/UH/hon4350/water_quality/somefile.xlsx"
# csv_file_path = "~/Documents/UH/hon4350/water_quality/somefile_converted.csv"
# xlsx_to_csv(xlsx_file_path, csv_file_path)


def copy_file_to_destination(source, destination):
    """
    Copies a file from the source path to the destination path.

    Parameters:
        source (str): Path to the source file.
        destination (str): Path to the destination file or directory.
    """
    
    # Expand ~ to the full home directory path
    source = os.path.expanduser(source)
    destination = os.path.expanduser(destination)

    try:
        shutil.copy2(source, destination)  # copy2 preserves metadata (timestamps)
        print(f"File copied successfully from '{source}' to '{destination}'")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except PermissionError:
        print("Error: Permission denied. Try running as administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example:
# source_file = "~/Documents/UH/hon4350/water_quality/GWDBDownload/GWDBDownload_data/WaterQualityMajor.txt"  
# destination_path = "~/Documents/UH/hon4350/water_quality/data/WaterQualityMajor_v1.txt"  
# copy_file_to_destination(source_file, destination_path)

def print_full(df):
    pd.set_option('display.max_rows', len(df))
    print(df)
    pd.reset_option('display.max_rows')