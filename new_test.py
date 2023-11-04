import requests
from geopy.geocoders import Nominatim

def get_lat_lng(name: str) -> tuple:
   geolocator = Nominatim(user_agent="your_app_name")
   location = geolocator.geocode(name)
   if location:
      latitude = round(location.latitude, 3)
      longitude = round(location.longitude, 3)
      return latitude, longitude
   return 0, 0

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

city = input("city name: ").lower().strip()
details = wqi_data(city)

# parse the data 
if details['found']:
   print("\n")
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