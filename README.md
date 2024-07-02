# Weather4U

Weather4U is a command-line application that provides current weather, weather history, 5-day weather forecast, and allows users to manage their favorite locations. The application uses the **OpenWeatherMap API*** to fetch weather data and supports temperature units in both Celsius and Fahrenheit.

## Features

- **Current Weather**: Get the current weather for a specified location.
- **Weather History**: View the history of weather data fetched during previous sessions.
- **5-Day Weather Forecast**: Get a 5-day weather forecast for a specified location.
- **View Favorites**: View a list of favorite locations.
- **Add Favorite**: Add a new location to the list of favorites.
- **Change Temperature Units**: Switch between Celsius and Fahrenheit for temperature display.

## Requirements

- Python 3.6+
- Requests library (can be installed via `pip install requests`)

## Setup
   1. Clone the repository or download the project files.
   2. Ensure you have Python 3.6+ installed on your machine.
   3. ### Create a Virtual Environment

      It is recommended to use a virtual environment to manage dependencies. You can create one using the following commands:
         
      - ***Create a virtual environment***
      
           python -m venv myvenv
      
      - ***Activate the virtual environment***
           - ***On Windows***
               myvenv\Scripts\activate
         
           - ***On macOS/Linux***
              source myvenv/bin/activate

   4. ### Install Dependencies
      pip install -r requirements.txt


## Usage   
   1. Run the weather_app.py file
      python weather_app.py
   2. Follow the on-screen menu to navigate through the application.   
   
   ### Menu Options

   - **1. Current Weather**: Enter a location to get the current weather.
   - **2. Weather History**: View the history of fetched weather data.
   - **3. 5-Day Weather Forecast**: Enter a location to get a 5-day weather forecast.
   - **4. View Favorites**: View your list of favorite locations.
   - **5. Add Favorite**: Add a new location to your favorites.
   - **6. Change Temperature Units**: Switch between Celsius and Fahrenheit.
   - **0. Quit**: Exit the application.

## Storing Data
- **Weather History**: Weather data is stored in a 'weather_history.json'file.
- **Favorites** :Favorite locations are stored in a 'favorites.json' file.

## Notes
- Ensure you have a stable internet connection as the application fetches data from the OpenWeatherMap API.
- API usage is subject to rate limits imposed by OpenWeatherMap. Consider this when making frequent requests.

## Author
- Dimpal Kaware (https://github.com/Dimplektech)
  

  
