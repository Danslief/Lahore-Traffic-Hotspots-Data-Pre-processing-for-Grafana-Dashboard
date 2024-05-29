import csv

filename = 'hehu.csv'  # Replace with the actual filename
output_filename = 'hehu_with_places.csv'  # Replace with the desired output filename

with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ['place']

    with open(output_filename, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            address = row['address']
            if address:
                place_name = address.split(',')[0].strip()
            else:
                place_name = ''

            row['place'] = place_name
            writer.writerow(row)

print("Places extracted and saved to", output_filename)