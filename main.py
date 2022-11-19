print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

import phonenumbers
import folium
from MyPhoneNumber import phone_number
from phonenumbers import geocoder

person_number = phonenumbers.parse(phone_number)
person_location = geocoder.description_for_number(person_number, "en")
print(person_location)

# Get the service provider
from phonenumbers import carrier
service_provider = phonenumbers.parse(phone_number)
print(carrier.name_for_number(service_provider, "en"))

from MyPhoneNumber import Key
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(person_location)
results = geocoder.geocode(query)

# Get the latitude and longitude of the person's location
lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]
print("Latitude: "f"{lat}\nLongitude: {lng}")

person_map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=person_location).add_to(person_map)

# Save the map in a HTML file
person_map.save("Location Tracked.html")
