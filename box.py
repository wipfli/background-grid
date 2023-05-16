import json

from calc import GlobalMercator

feature_collection = {
    "type": "FeatureCollection",
    "features": []
}

dx = 5
for i in range(0, 181, dx):
    line_feature = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": [[i, 0], [i, 85]]
        },
        "properties": {
            "width": "wide" if i % 45 == 0 else "narrow"
        }
    }
    feature_collection["features"].append(line_feature)

gm = GlobalMercator()
dx_meters, _ = gm.LatLonToMeters(0, dx)

for i in range(0, 37):
    lat, _ = gm.MetersToLatLon(0, i * dx_meters)
    line_feature = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": [[0, lat], [180, lat]]
        },
        "properties": {
            "width": "wide" if i % 9 == 0 else "narrow"
        }
    }
    feature_collection["features"].append(line_feature)

geojson = json.dumps(feature_collection, indent=2)

# Save the GeoJSON to a file
with open("lines.geojson", "w") as f:
    f.write(geojson)

print("GeoJSON file created successfully.")
