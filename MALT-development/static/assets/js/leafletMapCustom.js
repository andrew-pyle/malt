// var map = L.map('mapid').setView([34.7464809, -92.2895947], 10);
//
// L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
//     subdomains: ['a','b','c'],
// }).addTo(map);
//
// var marker = L.marker([34.7464809, -92.2895947]).addTo(map)
//     .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
//     .openPopup();

/**************
 * Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.
 * See http://maps.stamen.com
 * StamenTileLayer arguments:
 *  "toner"
 *  "toner-lite"
 *  "terrain"
 *  "watercolor"
 **************/
var layer = new L.StamenTileLayer("toner-lite");
var map = new L.Map("mapid", {
    center: new L.LatLng(34.7, -92.3),
    zoom: 12
});
map.addLayer(layer);

var marker = L.marker([34.7, -92.3]).addTo(map);
