# PyGeo_LocationTracker_v1.0
# Created by Cephas Cardozo
# Developed using Python

# imports
import webbrowser
import phonenumbers
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

print("PyGeoLocator")
print("Created by Cephas Cardozo")
print("Developed using Python\n")

# variable
num = input("Please input a phone number with the country code\nType here : ")
pep_number = phonenumbers.parse(num)
location = geocoder.description_for_number(pep_number, "en")
service_pro = phonenumbers.parse(num)

# print_statements
print(location)
print(carrier.name_for_number(service_pro, "en"))

# opencage_apiKey
key = '#put_in_your_own_OpencageApiKey'

# variables
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

# geo_location_Latitude_Longitude_variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# prints_geo_location
print(lat, lng)

# variable_map[latitude, longitude]
myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=location).add_to(myMap)


# geo_location_Data_SavedIn_HTML_File
myMap.save("PyGeoLocation.html")


# opens_pygeolocation.html_automatically
webbrowser.open_new_tab("PyGeoLocation.html")

# end_of_code