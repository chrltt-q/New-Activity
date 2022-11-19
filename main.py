print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

import phonenumbers
import folium
from phonenumbers import geocoder


def confirmation():
    while True:
        print("This program is solely intended for tracking down someone in case of emergencies.")
        confirm = input("Would you like to proceed? Type yes or no: ")
        if confirm == "yes":
            break
        elif confirm == "no":
            print("Now closing the program. Thank you!")
            break
        else:
            print("Invalid answer, please type yes or no only.")
            continue

print("Welcome!")
confirmation()

from MyPhoneNumber import phone_number
print("Phone Number being tracked successfully.")
person_number = phonenumbers.parse(phone_number)
person_location = geocoder.description_for_number(person_number, "en")
print("Country:", person_location)

# Get the service provider
from phonenumbers import carrier
service_provider = phonenumbers.parse(phone_number)
final_service_provider = carrier.name_for_number(service_provider, "en")
print("Service Provider: "f"{final_service_provider}")

from MyPhoneNumber import Key
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(person_location)
results = geocoder.geocode(query)

# Get the latitude and longitude of the person's location
lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]
print("Latitude: "f"{lat}\nLongitude: {lng}")

person_map = folium.Map(location=[lat, lng], zoom_start=3)
folium.Marker([lat, lng], popup=person_location).add_to(person_map)

# Save the map in a HTML file
person_map.save("Location Tracked.html")
