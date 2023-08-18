import os
import glob
import pymarc
import shutil
import time

# Set the input and output folder paths
input_folder = ''
output_folder = 'output/'
processed_folder = 'processed/'

# Create the output folder if it doesn't already exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create the processed folder if it doesn't already exist
if not os.path.exists(processed_folder):
    os.makedirs(processed_folder)

start_time = time.time()  # Start the timer

total_lines = 0  # Initialize a counter for the total number of lines processed

# Loop through all MARC files in the input folder
for filename in glob.glob(os.path.join(input_folder, '*.mrc')):
    # Open the MARC file and read the records
    with open(filename, 'rb') as fh:
        reader = pymarc.MARCReader(fh)
        # Loop through all records in the file
        for record in reader:
            # Format the record as human-readable text
            text = str(record)
            # Write the text to a file in the output folder
            output_filename = os.path.join(output_folder, os.path.basename(filename) + '.txt')
            with open(output_filename, 'a', encoding='utf-8') as output_file:
                output_file.write(text)
                output_file.write('\n\n')
                total_lines += 1  # Increment the counter for each line processed
    # Move the processed file to the 'processed' folder
    shutil.move(filename, os.path.join(processed_folder, os.path.basename(filename)))

end_time = time.time()  # Stop the timer

# Calculate the total process time in seconds
total_time = end_time - start_time

# Print the total number of lines and process time to the console
print(f'Total lines processed: {total_lines}')
print(f'Total process time: {total_time:.2f} seconds')
