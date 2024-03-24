function initMap() {
    const defaultLocation = { lat: -34.397, lng: 150.644 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 16,
        center: defaultLocation,
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const userLocation = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                map.setCenter(userLocation);

                const userMarker = new google.maps.Marker({
                    position: userLocation,
                    map: map,
                    title: "Your Location",
                    icon: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
                });

                const service = new google.maps.places.PlacesService(map);
                service.nearbySearch(
                    {
                        location: userLocation,
                        radius: 5000,
                        type: ["hospital"],
                    },
                    (results, status) => {
                        if (status === google.maps.places.PlacesServiceStatus.OK && results) {
                            results.forEach((result) => {
                                createMarker(result, map, userLocation);
                            });
                        }
                    }
                );
            },
            () => {
                handleLocationError(true, map.getCenter(), map);
            }
        );
    } else {
        handleLocationError(false, map.getCenter(), map);
    }
}

function createMarker(place, map, userLocation) {
    const marker = new google.maps.Marker({
        position: place.geometry.location,
        map: map,
    });

    const infowindow = new google.maps.InfoWindow({
        content: `<h3>${place.name}</h3>
                  <p>${place.vicinity}</p>
                  <a target="_blank" href="https://www.google.com/maps/dir/?api=1&origin=${userLocation.lat},${userLocation.lng}&destination=${place.geometry.location.lat()},${place.geometry.location.lng()}&travelmode=driving">Guide to here</a>`
    });

    marker.addListener("click", () => {
        infowindow.open(map, marker);
    });
}


function handleLocationError(browserHasGeolocation, pos, map) {
    alert(browserHasGeolocation ?
        'Error: The Geolocation service failed.' :
        'Error: Your browser doesn\'t support geolocation.');
    map.setCenter(pos);
}
