from geopy.geocoders import Nominatim

""""geopy is a Python client for several popular geocoding web services.
geopy makes it easy for Python developers to locate the coordinates of addresses, cities, 
countries, and landmarks 
across the globe using third-party geocoders and other data sources."""


geolocator = Nominatim(user_agent="my_dependency_injection")
location = geolocator.geocode("Odintsovo 143007")
print(location.address)
print((location.latitude, location.longitude))