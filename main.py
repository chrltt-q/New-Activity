print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

import phonenumbers
from MyPhoneNumber import phone_number
from phonenumbers import geocoder

person_number = phonenumbers.parse(phone_number)
person_location = geocoder.description_for_number(person_number, "en")
print(person_location)

# Get the service provider
from phonenumbers import carrier
service_provider = phonenumbers.parse(phone_number)
print(carrier.name_for_number(service_provider, "en"))
