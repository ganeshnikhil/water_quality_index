const axios = require('axios');
const opencage = require('opencage-api-client');

const opencageApiKey = 'cc5196c709b9434a9c993fec31dd4820'; // Replace with your OpenCage API key
const meersensApiKey = '4FYIeuwcXmpspTIjK4fkK8BJJIHSpwuL'; // Replace with your Meersens API key

function geocodeAddress(address) {
  return new Promise((resolve, reject) => {
    opencage
      .geocode({ q: address, key: opencageApiKey })
      .then((data) => {
        if (data.status.code === 200 && data.results.length > 0) {
          const place = data.results[0];
          const latitude = place.geometry.lat;
          const longitude = place.geometry.lng;
          resolve({ latitude, longitude });
        } else {
          reject('Invalid address or no results found');
        }
      })
      .catch((error) => {
        reject('Error while geocoding');
      });
  });
}

const wqiData = async (city) => {
  let lat, lng;

  try {
    const coords = await geocodeAddress(city);
    lat = coords.latitude;
    lng = coords.longitude;
  } catch (error) {
    console.error('Error geocoding address:', error);
    return;
  }

  if (lat !== undefined && lng !== undefined) {
    const url = `https://api.meersens.com/environment/public/air/current?lat=${lat}&lng=${lng}`;

    try {
      const response = await axios.get(url, {
        headers: {
          'apikey': meersensApiKey,
        },
      });

      if (response.status === 200) {
        const data = response.data;
        if (data && data.found) {
          console.log('\nIndex type:', data.index.index_type);
          console.log('Overall Qualification:', data.index.qualification);
          console.log('Total index value:', data.index.value);
          console.log('Main pollutants list:');
          console.log(data.index.main_pollutants.join(', '));
          console.log('#'.repeat(20));

          const pollutants = data.pollutants;
          for (const key in pollutants) {
            if (pollutants.hasOwnProperty(key)) {
              const pollutant = pollutants[key];
              console.log(`Chemical name: ${pollutant.name} (${pollutant.shortcode})`);
              console.log(`Chemical index value: ${pollutant.value}`);
              console.log(`Confidence level: ${pollutant.confidence}`);
              console.log(`Index Type: ${pollutant.index.index_type}`);
              console.log(`Index Name: ${pollutant.index.index_name}`);
              console.log(`Qualification: ${pollutant.index.qualification}`);
              console.log(`Description: ${pollutant.index.description}`);
              console.log(`Overall chemical index level: ${pollutant.index.value}`);
              console.log('*'.repeat(20));
            }
          }
        } else {
          console.log(data);
        }
      } else {
        console.error(`Failed to fetch WQI data for city: ${city}`);
      }
    } catch (error) {
      console.error('Error fetching WQI data:', error.message);
    }
  }
};

const city = 'Munich'; // Replace with your desired city

wqiData(city);
