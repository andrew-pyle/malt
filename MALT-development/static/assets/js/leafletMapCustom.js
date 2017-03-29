/**************
 * Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.
 * See http://maps.stamen.com
 * StamenTileLayer arguments:
 *  "toner"
 *  "toner-lite"
 *  "terrain"
 *  "watercolor"
 **************/

// TODO Create AJAX call back to flask to get the map markers and .addTo(map)

var layer = new L.StamenTileLayer("toner-lite");
var map = new L.Map("mapid", {
    center: new L.LatLng(34.7, -92.3),
    zoom: 12
});
map.addLayer(layer);

var marker = L.marker([34.7, -92.3]).addTo(map);
