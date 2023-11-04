import requests
from geopy.geocoders import Nominatim
# it get latitude and longitude value by area name 
def get_lat_lng(city: str) -> tuple:
   geolocator = Nominatim(user_agent="your_app_name")
   location = geolocator.geocode(city)
   if location:
      latitude = round(location.latitude, 3)
      longitude = round(location.longitude, 3)
      return latitude, longitude
   return 0, 0

# it gets water quality index from api using api_key and return that data 
def wqi_data(city: str) -> dict:
   api_key = "4FYIeuwcXmpspTIjK4fkK8BJJIHSpwuL"
   lat, lng = get_lat_lng(city)
   if lat and lng:
      url = f"https://api.meersens.com/environment/public/air/current?lat={lat}&lng={lng}"
      headers = {
            "apikey": api_key
      }
      response = requests.get(url, headers=headers)
      if response.status_code == 200:
         data = response.json()
         return data
   return {"found": False}

# Enter the city name 
city = input("city name: ").lower().strip()
# get the  wqi details using api details

details = wqi_data(city)

# parse the data and print it on screen you can manuplate it accoding to what do you want to do with this data.
if details['found']:
   print("\n")
   print(f"Date time: {details['datetime']}")
   print(f"Index type: {details['index']['index_type']}")
   print(f"Overall Qualificaton: {details['index']['qualification']}")
   print(f"Total index value: {details['index']['value']}")
   print(f"Main pollutaints list: ")
   print(*details['index']['main_pollutants'])
   
   print(f"{'#'*20}\n")

   pollutants_keys = details.get('pollutants', {})
   for pollutant_key, pollutant_data in pollutants_keys.items():
      print(f"Chemical name: {pollutant_data['name']} ({pollutant_data['shortcode']})")
      print(f"Chemical index value: {pollutant_data['value']}")
      print(f"Confidence level: {pollutant_data['confidence']}")
      print(f"Index Type: {pollutant_data['index']['index_type']}")
      print(f"Index Name: {pollutant_data['index']['index_name']}")
      print(f"Qualification: {pollutant_data['index']['qualification']}")
      print(f"Description: {pollutant_data['index']['description']}")
      print(f"Overall chemical index level: {pollutant_data['index']['value']}")
      print(f"{'*'*20}\n")
else:
   print(details)
