import csv

# Define the input and output file names
input_file = "all-new-products.csv"
output_file = "only-i7-13e-gen.csv"

# Open the input and output CSV files
with open(input_file, mode='r') as input_csv, open(output_file, mode='w', newline='') as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)

    # Write the header row to the output file
    header = next(reader)
    writer.writerow(header)

    # Iterate through the rows in the input file
    for row in reader:
        # Check if the row contains "i7-13e-gen"
        if ("i7-13e-gen" in ' '.join(row)) :#and ("gamer" not in ' '.join(row)) :
            # Write the row to the output file
            writer.writerow(row)

print(f"Lines containing 'i7-13e-gen' have been extracted to {output_file}")

