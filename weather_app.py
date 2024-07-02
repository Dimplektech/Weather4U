import requests
import json
from datetime import datetime

API_KEY = "b3df37c2831edc1eb315e526cc84f7ca"

MENU = """Weather4U
Please select an opton below:
1. Current weather
2. Weather History
3. 5 Day Weather Forecast
4. View Favorite
5. Add Favorite
6. Change Temprature Units

0. Quit \n"""

units = 'metric'  # Default to Celcius.
favorites = []  # List to store favorite locations.


def get_location(location):
    """
    Fetch location data from openWeatherMap Geocoding API.
    
    Args:
        location(str) : The location name to search for.
        
    Returns:
        list: List of loactions data dictionaries which matching
        with entered location
    """
    payload = {
     'q': location,
     'limit': 5,
     'appid': API_KEY,
     'units': units
    }

    response = requests.get("http://api.openweathermap.org/geo/1.0/direct",
                            params=payload)
    return response.json()


def display_location(locations):
    """
    Display a list of locations for user selection.
    
    Args: 
        locations(list): List of location data dictionaries.
    """
    for i, location in enumerate(locations, 1):
        print(f"{i} - {location['name']}, {location['country']}")


def get_current_weather(lat, lon, units):
    """
    Fetch current weather data from OpenWeatherMap ApI.
    
    Args:
        lat (float): Latitude of the location.
        lon(float): Longitude of the location.
        units(str): Unit for temprature (metric or imperial).
    Returns:
        dict: Current weather data.
    """

    payload = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': units

    }

    response = requests.get("https://api.openweathermap.org/data/2.5/weather", 
                            payload)
    data = response.json()
    store_weather_data(data, units)  # Store fetched weather data for history.
    return data


def draw_line(symbol="-", length=80, print=False):
    """
    Draw a line of a specified length and symbol.

    Args:
       symbol (str): Symbol to use for the line.
       length(int): Length of the line.
       print_line(bool): Whether to print the line or return it as a string.

    Returns:
       str: The drawn line.   
    """

    line = (symbol*length) + "\n"
    if print:
        print(line)
    return line


def display_weather_data(data):
    """
    Display current weather data.
    
    Args:
        data(dict): Current weather data.
        units(str): Unit for temprature(metric or imperial).
    """
    unit_symbol = '\u00b0C' if units == 'metric' else '\u00b0F'
    sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
    sunset_time = datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
    overview = draw_line()
    overview += f"Weather Report: {data['name']} - {data['sys']['country']}\n"
    overview += draw_line()
    overview += f"{data['weather'][0]['description'].title()}\n"
    overview += f"Current Temp {data['main']['temp']}{unit_symbol}\n"
    # '\u00b0C' this will add digree symbol.
    overview += f"Feels Like: {data['main']['feels_like']}{unit_symbol}\n"
    overview += f"Min_temp: {data['main']['temp_min']}{unit_symbol}\n"
    overview += f"Max_temp: {data['main']['temp_max']}{unit_symbol}\n"
    overview += f"Sunrise: {sunrise_time} UTC\n"
    overview += f"Sunset: {sunset_time} UTC\n"
    overview += draw_line()
    print(overview)


def get_5_day_forecast(lat, lon, units):
    """
    Fetch 5-day weather forecast data from OpenWeatherMap API.
    
    Args:
        lat(float): Latitude of the location.
        lon(float): Longitude of the location.#
        units(str): Unit for temprature (metric or imperial)

    Returns:
       dict: 5-day weather forecast data.        
       
    """
    payload = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': units
        }
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                            params=payload)
    return response.json()


def display_5_day_forecast(data):
    """
    Display 5-day weather forwcast data.

    Args:
       data(dict): 5-day weather forecast data.
       units(str): Unit for temprature(metric or imperial.)
    """
    unit_symbol = '\u00b0C' if units == 'metric' else '\u00b0F'
    overview = draw_line()
    overview += f"5 day Weather Forecast: {data['city']['name']},"
    overview += f"{data['city'], ['country']}\n"
    overview += draw_line()

    for forecast in data['list']:
        dt_txt = forecast['dt_txt']
        description = forecast['weather'][0]['description'].title()
        temp = forecast['main']['temp']
        feels_like = forecast['main']['feels_like']
        temp_min = forecast['main']['temp_min']
        temp_max = forecast['main']['temp_max']

        overview += f"\n{dt_txt}"
        overview += f" - {description}\n"
        overview += f" - Temp: {temp}{unit_symbol}\n"
        overview += f" - Feels Like: {feels_like}{unit_symbol}\n"
        overview += f" - Min Temp: {temp_min}{unit_symbol}\n"
        overview += f" - Max Tamp: {temp_max}{unit_symbol}\n"
        overview += draw_line()

    print(overview)


def save_favorites(favorites):
    """
    Save favorite locations to a JSON file
    
    Args:
        favorites (list): List of favorite locations
    """
    with open('favorites.json', 'w') as f:
        json.dump(favorites, f)


def load_favorites():
    """
    Load favorite locations from a JSON file.
    
    Returns:
       list: List of favorite locations.
    """
    try:
        with open('favorites.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


favorites = load_favorites()


def display_favorites(favorites):
    """
    Display favorite locations.
    
    Args:
        favorites (list): List of favorite locations.
    """
    for i, favorite in enumerate(favorites, 1):
        print(f"{i} - {favorite['name']}, {favorite['country']}")


def add_favorite(location):
    """
    Add a location to favorites
    
    Args:
    location (dict): Location data dictionary.
    """
    favorites.append(location)
    save_favorites(favorites)
    print("Location added to Favorites.")


def change_units():
    global units
    if units == 'metric':
        units = 'imperial'
        print("Switched to Fahrenheit.")
    else:
        units = 'metric'
        print("Switched to Celcius.")


def store_weather_data(data, units):
    """
    Store weather data locally for history purposes.
    
    Args:
        data (dict): Current weather data.
        units (str): Unit for temprature(metric or imperial).
    """
    record = {
        'date': datetime.utcnow().isoformat(),
        'data': data,
        'units': units
    }
    try:
        with open('weather_history.json', 'r') as f:
            history = json.load
    except FileNotFoundError:
        history = []

    history.append(record)
    
    with open('weather_history.json', 'w') as f:
        json.dump(history, f, indent=4)


def get_weather_history():
    """
    Retrieve stored weather history data.
    
    Returns:
        list: List of stored weather history records.
    """
    try:
        with open('weather_history.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("No weather History available.")
        return []


def display_weather_history():
    """
    Display stored weather history.
    """
    history = get_weather_history()
    if not history:
        return

    for record in history:
        date = record['date']
        data = record['data']
        units = record['units']
   
        unit_symbol = '\u00b0C' if units == 'metric' else '\u00b0F'
        sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
        sunset_time = datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
        overview = draw_line()
        overview += f"Date: {date}\n"
        overview += f"Location: {data['name']} - {data['sys']['country']}\n"
        overview += draw_line()
        overview += f"{data['weather'][0]['description'].title()}\n"
        overview += f"Current Temp {data['main']['temp']}{unit_symbol}\n"
        # '\u00b0C' this will add digree symbol.
        overview += f"Feels Like: {data['main']['feels_like']}{unit_symbol}\n"
        overview += f"Min_temp: {data['main']['temp_min']}{unit_symbol}\n"
        overview += f"Max_temp: {data['main']['temp_max']}{unit_symbol}\n"
        overview += f"Sunrise: {sunrise_time} UTC\n"
        overview += f"Sunset: {sunset_time} UTC\n"
        overview += draw_line()
        print(overview)

        print()


while True:
    user_option = input(MENU)
    if user_option == '1':
        location = input("Please enter a location: ")
        locations = get_location(location)
        print("Please select a location below : ")
        display_location(locations)
        index = input(": ")
        index = int(index)-1 
        chosen_location = locations[index]
        current_weather = get_current_weather(chosen_location["lat"],
                                              chosen_location["lon"],
                                              units)
        display_weather_data(current_weather)
        input("Press enter to continue...")

    elif user_option == '2':
        display_weather_history()

    elif user_option == '3':
        location = input("Please Enter your Location: ")
        locations = get_location(location)
        print("Please select a location below: ")
        display_location(locations)
        index = input(": ")
        index = int(index)-1
        chosen_location = locations[index]
        forecast_data = get_5_day_forecast(chosen_location['lat'],
                                           chosen_location['lon'], units)
        display_5_day_forecast(forecast_data)
        input("Press enter to continue: ")

    elif user_option == '4':
        display_favorites(favorites)
        print("Press Enter to Continue...")

    elif user_option == '5':
        location = input("Please enter a location: ")
        locations = get_location(location)
        print("Please select a location below : ")
        display_location(locations)
        index = input(": ")
        index = int(index)-1
        chosen_location = locations[index]
        add_favorite(chosen_location)
        input("Please Enter to Continue...")

    elif user_option == '6':
        print("Change Units")
        change_units()
        input("Press enter to continue...")

    elif user_option == '0':
        break
