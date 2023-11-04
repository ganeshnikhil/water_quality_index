# water_quality_index

# Water Quality Index (WQI) Lookup

This Python script allows you to retrieve the Water Quality Index (WQI) for a specific city by providing its name. It uses the Meersens API to fetch WQI data based on the city's geographical coordinates.

## Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/)
- Libraries: `requests`, `geopy`

## Installation

1. Clone this repository or download the `wqi.py` script to your local machine.

2. Install the required libraries by running the following command:

   ```bash
   pip install -r requirements.txt
   
# response json.
```
Enter city name: Bihar

Date time: 2023-11-04T10:00:00.000Z
Index type: meersens
Overall Qualification: Mediocre
Total index value: 69.55
Main pollutants list:
pm10
####################

Chemical name: Carbon monoxide (CO)
Chemical index value: 353.5
Confidence level: 5
Index Type: meersens
Index Name: MAQI
Qualification: Perfect
Description: Air quality level won't present a risk for health for an exposure time superior to decades
Overall chemical index level: 0.86
********************
```

## Technical Overview

This section provides a technical breakdown of how the Water Quality Index (WQI) lookup program works.

### Libraries Used

- **Requests**: Used for making HTTP requests to the Meersens API to retrieve water quality data. It serves as the communication tool with external resources.

- **Geopy (Nominatim)**: Geopy, with the Nominatim geocoder, translates human-readable city names into latitude and longitude coordinates. This is essential for locating the city and fetching its water quality data.

### `get_lat_lng` Function

- This function leverages Geopy's Nominatim geocoder to determine the geographic coordinates (latitude and longitude) of a specified city.

### `wqi_data` Function

- Responsible for fetching water quality data by sending an HTTP GET request to Meersens' API. It includes the city's geographic coordinates and an API key for authentication.

- Checks the HTTP response status code to verify the success of the request (status code 200). The data retrieved from the API is in JSON format.

### User Interaction

- The program prompts the user to provide the name of a city for water quality data lookup.

- User input is processed to ensure uniformity by converting it to lowercase and removing extra spaces.

- The `wqi_data` function is invoked with the specified city name, and it returns water quality data for that city.

### Parsing and Displaying Data

- If data is found for the city, the program displays various details, including:
   
  - The date and time of data retrieval.
  - The type of index used to represent water quality.
  - The overall qualification of water quality.
  - The total index value, serving as a grade for water quality.
  - A list of main pollutants affecting water quality.

- The program also provides detailed information about each pollutant, covering its name, abbreviation (shortcode), index value, confidence level, index type, index name, qualification, and a description of the pollutant's impact on health.


### Important Note (License)

- Users should be aware that while the program is freely provided, there are guidelines and rules to follow, typically outlined in a license. These rules ensure responsible and compliant usage of the program as set by its creators.

This technical overview provides insights into the inner workings of the program, from data retrieval to user interaction, data parsing, and even sharing the required libraries through a web application. It's like a backstage tour of a magic show, revealing the mechanics behind the magic tricks.
