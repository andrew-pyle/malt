function validateLocationFilter() {
  var radius = document.forms["filter"]["radius"].value;
  var latitude = document.forms["filter"]["latitude"].value;
  var longitude = document.forms["filter"]["longitude"].value;
  if ((radius != "") || (latitude != "") || (longitude != "")) {
    if ((radius.length > 0) && (latitude.length > 0) && (longitude.length > 0)) {
      return true;
    }
    alert("To filter location, Radius, Latitude, and Longitude must all have values");
    return false;
  }
}
