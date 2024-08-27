import csv
import os

# Define the headers according to the expected columns
headers = [
    "CC No", "Month", "Year", "Location", "Name", "Address", "City", "State", "Zip code", "Phone No", "Mail ID", "Country"
]

# Function to process the CSV data and write to an output file
def process_csv_to_file(input_file_path, output_file_path):
    try:
        # Check if the input file exists
        if not os.path.isfile(input_file_path):
            raise FileNotFoundError(f"The file '{input_file_path}' does not exist.")
        
        # Check if the directory for the output file exists
        output_dir = os.path.dirname(output_file_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # Create directory if it does not exist
        
        with open(input_file_path, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
            
            reader = csv.reader(infile, delimiter='|')
            writer = outfile.write
            
            for row in reader:
                line = ""
                for header, value in zip(headers, row):
                    if value:  # Include only non-empty values
                        line += f"{header}: {value}\n"
                if line:  # Write to file only if line is not empty
                    writer(line + "\n=============================\n\n")
                    
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(f"Permission error: {e}")

# Define the input CSV file path and output file path
csv_file_path = 'data/CC_new.csv'  # Update this path as needed
output_file_path = 'out/output_onlyDisplayPresentColumns.txt'  # Ensure this path is correct and writable

# Process the CSV file and write to output file
process_csv_to_file(csv_file_path, output_file_path)
