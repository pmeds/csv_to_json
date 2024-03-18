import csv
import json

# Initialize an empty dictionary to hold the final JSON structure
json_output = {}

# Step 1: Read the CSV file
csv_file_path = 'csv_prod_facet_mapping.csv'  # Replace 'your_csv_file.csv' with the path to your CSV file
with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row:  # Make sure the row is not empty
            key = row[0]  # The first element is the key
            values = row[1:]  # The rest of the elements are the values
            json_output[key] = values


# Optionally, format the JSON output for readability
json_str = json.dumps(json_output, indent=4)
# Print the JSON string to the console
print(json_str)

#Write json to file
json_file_path = 'prod_facet_mapping.json'
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(json_output, json_file, indent=4)  # Directly write the JSON output to the file

