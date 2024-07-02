# Weather4U

Weather4U is a command-line application that provides current weather, weather history, 5-day weather forecast, and allows users to manage their favorite locations. The application uses the OpenWeatherMap API to fetch weather data and supports temperature units in both Celsius and Fahrenheit.

## Features

- **Current Weather**: Get the current weather for a specified location.
- **Weather History**: View the history of weather data fetched during previous sessions.
- **5-Day Weather Forecast**: Get a 5-day weather forecast for a specified location.
- **View Favorites**: View a list of favorite locations.
- **Add Favorite**: Add a new location to the list of favorites.
- **Change Temperature Units**: Switch between Celsius and Fahrenheit for temperature display.

## Requirements

- Python 3.x
- Requests library (can be installed via `pip install requests`)

## Setup

1. Clone the repository or download the project files.
2. Ensure you have Python 3.x installed on your machine.
3. Install the required libraries using pip:
   ```bash
   pip install requests

## Usage   
- **1. Current Weather**: Enter a location to get the current weather.
- **2. Weather History**: View the history of fetched weather data.
- **3. 5-Day Weather Forecast**: Enter a location to get a 5-day weather forecast.
- **4. View Favorites**: View your list of favorite locations.
- **5. Add Favorite**: Add a new location to your favorites.
- **6. Change Temperature Units**: Switch between Celsius and Fahrenheit.
- **0. Quit**: Exit the application.

## Storing Data
- ** Weather History:** Weather data is stored in a 'weather_history.json'file.
- ** Favorites:** Favorite locations are stored in a 'favorites.json' file.

## Notes
- Ensure you have a stable internet connection as the application fetches data from the OpenWeatherMap API.
- API usage is subject to rate limits imposed by OpenWeatherMap. Consider this when making frequent requests.

## Author
- Dimpal Kaware (https://github.com/Dimplektech)
  

  

