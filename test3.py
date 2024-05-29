import pandas as pd
from sklearn.cluster import KMeans

# Read the CSV file into a DataFrame with the appropriate encoding
df = pd.read_csv('hehu.csv', encoding='utf-8-sig')

# Select the Latitude and Longitude columns
coordinates = df[['Latitude', 'Longitude']]

# Perform K-means clustering with k=3
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(coordinates)

# Add a new column to the DataFrame with the cluster labels
df['Cluster'] = kmeans.labels_

# Print the count of places in each cluster
print(df['Cluster'].value_counts())