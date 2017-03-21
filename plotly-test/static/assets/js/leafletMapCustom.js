var map = L.map('mapid').setView([34.7464809, -92.2895947], 10);

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a','b','c'],
}).addTo(map);

var marker = L.marker([34.7464809, -92.2895947]).addTo(map)
    .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
    .openPopup();
