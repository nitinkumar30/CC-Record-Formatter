import csv

# Define the headers according to the expected columns
headers = [
    "CC No", "Month", "Year", "Location", "Name", "Address", "City", "State", "Zip code", "Phone No", "Mail ID", "Country"
]

# Function to process the CSV data and write to an output file
def process_csv_to_file(input_file_path, output_file_path):
    with open(input_file_path, mode='r', newline='') as infile, \
         open(output_file_path, mode='w', newline='') as outfile:
        
        reader = csv.reader(infile, delimiter='|')
        writer = outfile.write
        
        for row in reader:
            line = ""
            for header, value in zip(headers, row):
                if value:  # Include only non-empty values
                    line += f"{header}: {value}\n"
                else:
                    # Optionally, you can choose to print 'Not Available' for empty values.
                    # If you don't want to display 'Not Available', you can remove the else block.
                    pass
            if line:  # Write to file only if line is not empty
                writer(line + "\n=============================\n\n")

# Define the input CSV file path and output file path
csv_file_path = 'data/CC_new.csv'
output_file_path = 'out/output.txt'

# Process the CSV file and write to output file
process_csv_to_file(csv_file_path, output_file_path)
