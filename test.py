import geohash2
import pandas as pd

def geohash_to_lat_lon(geohash):
    try:
        lat, lon = geohash2.decode(geohash)
        return lat, lon
    except ValueError:
        print(f"Invalid geohash: {geohash}")
        return None, None

# Prompt the user to input the file path
file_path = input("Please enter the path to the file containing geohashes: ")

# Load the CSV file
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print("File not found.")
    exit()

# Extract the geohash column
geohash_column = input("Please enter the name of the column containing geohashes: ")

# Create new columns for latitude and longitude
data['Latitude'] = None
data['Longitude'] = None

# Iterate through each row and convert geohashes to latitude and longitude
for index, row in data.iterrows():
    geohash = row[geohash_column]
    latitude, longitude = geohash_to_lat_lon(geohash)
    if latitude is not None and longitude is not None:
        data.at[index, 'Latitude'] = latitude
        data.at[index, 'Longitude'] = longitude

# Save the updated DataFrame to the same CSV file
output_file_path = file_path  # Overwrite the input file
data.to_csv(output_file_path, index=False)

print("Latitude and longitude columns added to the file successfully.")
