# background-grid
Background grid in MapLibre GL JS

Create a nice google/apple-maps-like background pattern in MapLibre GL JS.

To best see the effect, turn on throtteling in your browser to simulate a slow connection.

## Demo

<a href="https://wipfli.github.io/background-grid">
<img src="maplibre.png">
</a>

## How it works

Generate a tile with lines

```
python3 box.py
tippecanoe -f -z1 -Z1 -o data/out.mbtiles lines.geojson
```

Serve the tile with tileserver-gl

```
docker run --rm -it -v "$(pwd)/data":/data -p 8080:8080 maptiler/tileserver-gl -p 8080
```

Load the tile in the browser, download the pbf, save it to the folder


Turn the tile to a base64 array with vector.html

