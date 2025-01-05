import pandas as pd
import folium
from geopy.geocoders import Nominatim

# Read the CSV file containing the event data
df = pd.read_csv('events.csv')

# Initialize a geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Geocode the locations to obtain latitude and longitude coordinates
df['Coordinates'] = df['Location'].apply(geolocator.geocode).apply(lambda x: (x.latitude, x.longitude) if x else None)

# Create a map
m = folium.Map(location=[11.0000, 76.9667], zoom_start=12)

for index, row in df.iterrows():
    if row['Coordinates']:
        popup_text = f"<b>{row['Title']}</b><br>{row['Date']}<br>{row['Location']}"
        folium.Marker(location=row['Coordinates'], popup=popup_text).add_to(m)

# Save the map to an HTML file
m.save("events_map.html")