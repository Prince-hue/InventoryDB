import csv

csv_file_path = 'operatingCost.csv'  # Update with the actual path to your CSV file




with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Assuming the first row contains headers
    headers = next(csv_reader)

    print("Keys (Headers):", headers)

