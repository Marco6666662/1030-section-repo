import sys
import csv

# check if a filename was provided as a command line argument
if len(sys.argv) < 2:
    print("Usage: python parser.py <csv_file>")
    sys.exit()

# get the filename from the command line argument
csv_file = sys.argv[1]

# get the table name from the filename
table_name = csv_file.split('.')[0]

# open the CSV file
with open(csv_file, newline='') as csvfile:
    # read the contents of the file into a list of dictionaries
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# create a list of strings representing the data to insert
insert_values = []
for row in rows:
    values = []
    for key, value in row.items():
        # escape any single quotes in the value
        value = value.replace("'", "''")
        values.append(f"'{value}'")
    insert_values.append(f"({','.join(values)})")

# create the SQL insert statement
insert_statement = f"INSERT INTO {table_name} ({','.join(rows[0].keys())}) VALUES {','.join(insert_values)};"

# save the SQL insert statement to a text file
output_file = f"{table_name}.txt"
with open(output_file, "w") as f:
    f.write(insert_statement)

# print a message indicating that the file was saved
print(f"SQL insert statement saved to {output_file}")