/**************
 * Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.
 * See http://maps.stamen.com
 * StamenTileLayer arguments:
 *  "toner"
 *  "toner-lite"
 *  "terrain"
 *  "watercolor"
 **************/


// Initialize Map
var map = L.map('mapid').setView([34.7, -92.3], 13);

// Load Stamen Tile Layer
var layer = new L.StamenTileLayer("toner-lite");
map.addLayer(layer);

// Add Dummy Marker
// var marker = L.marker([34.7, -92.3]).addTo(map);

// load GeoJSON from an external file
// $.getJSON('assets/js/dataset.js',function(data){
//   // add GeoJSON layer to the map once the file is loaded
//   L.geoJson(data).addTo(map);
// });

var marker = L.geoJson({
  "type": "FeatureCollection",
  "features": [
  {"geometry": {"coordinates": [-92.5868279, 34.5645372],
    "type": "Point"},
   "properties": {"Account Name": "xxxxxxxxxxxx",
    "City": "Benton",
    "IP Address": "108.64.45.187"},
   "type": "Feature"}
  ]
}).addTo(map);

// TODO
// 1. Fix pandas-to-geojson.py '' -> ""
// 2. Link dataset.js (rename?) to leafletMapCustom.js (Apache serving)
// 3. Add markers to leaflet
