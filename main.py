import csv
import pyproj

def encode_geohash(latitude, longitude, precision=12):
    # Base32 encoding
    base32 = '0123456789bcdefghjkmnpqrstuvwxyz'

    # Define geohash ranges
    lat_range = (-90.0, 90.0)
    lon_range = (-180.0, 180.0)

    geohash = ''
    bits = 0
    bit = 0
    ch = 0

    while len(geohash) < precision:
        if bit % 2 == 0:
            mid = (lon_range[0] + lon_range[1]) / 2
            if longitude > mid:
                ch |= 1 << (4 - (bits % 5))
                lon_range = (mid, lon_range[1])
            else:
                lon_range = (lon_range[0], mid)
        else:
            mid = (lat_range[0] + lat_range[1]) / 2
            if latitude > mid:
                ch |= 1 << (4 - (bits % 5))
                lat_range = (mid, lat_range[1])
            else:
                lat_range = (lat_range[0], mid)

        bits += 1
        if bits % 5 == 0:
            geohash += base32[ch]
            ch = 0
        bit += 1

    return geohash

# Define the projection for the coordinates (assuming they're in UTM)
projection = pyproj.Proj(init='epsg:3857')  # This assumes coordinates are in Web Mercator (EPSG:3857)

# Read data from CSV file
csv_file = 'geo_hash.csv'
output_file = 'hehu.csv'

with open(csv_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['geohash']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Convert projected coordinates to latitude and longitude
        longitude, latitude = projection(row['Longitude'], row['Latitude'], inverse=True)

        # Encode latitude and longitude into geohash
        geohash = encode_geohash(latitude, longitude)

        # Add geohash to the row and write it to the output file
        row['geohash'] = geohash
        writer.writerow(row)

print("Conversion complete. Geohash values added to the CSV file.")
