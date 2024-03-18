import csv
import json

# Initialize an empty dictionary to hold the final JSON structure
json_output = {}

# Step 1: Read the CSV file
csv_file_path = 'csv_prod_selector_mapping.csv'  # Replace 'your_csv_file.csv' with the path to your CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    # Read the file line by line
    for line in csv_file:
        # Split the line on the comma to separate the 'type=key' and 'value'
        parts = line.strip().split(',')  # Ensure to strip whitespace/newlines
        if parts and len(parts) == 2:
            # The first part contains 'type=key'. Split on '=' and remove "type=" from the key
            key_part = parts[0].split('=')[1]  # Directly access the key after 'type='
            # The second part is the value without any modification needed
            value = parts[1]
            # Add to the JSON output
            json_output[key_part] = value

# Step 2: Convert the dictionary to a JSON string
json_str = json.dumps(json_output, indent=4)
# Print the JSON string to the console
print(json_str)

# Optionally, save the JSON output to a file
json_file_path = 'prod_selector_mapping.json'
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json_file.write(json_str)


