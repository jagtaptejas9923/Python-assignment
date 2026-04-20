import json
import csv

# Read JSON file
with open("input.json", "r") as json_file:
    data = json.load(json_file)   # loads JSON array

# Open CSV file for writing
with open("output.csv", "w", newline="") as csv_file:
    
    # Get column names from JSON keys
    headers = data[0].keys()
    
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    
    writer.writeheader()   # write column names
    writer.writerows(data) # write data rows

print("JSON converted to CSV successfully!")