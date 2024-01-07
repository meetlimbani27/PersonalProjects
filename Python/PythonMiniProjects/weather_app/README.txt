# Windoser Weather App

A simple weather application built using Python and Tkinter to retrieve weather data using the WeatherAPI and display it in a graphical user interface.

## Functionality

- Retrieves weather data based on the selected city or the user's geolocation.
- If the city name input field is left empty and the submit button is clicked, it automatically detects the user's current location using geolocation.
- Displays the weather climate, wind speed, temperature, pressure, humidity, and cloud cover.
- Allows the user to select a city from a list of predefined options.
- Provides a submit button to initiate the retrieval of weather data.
- Utilizes the requests library to make HTTP requests to the WeatherAPI.
- Utilizes the geocoder library to retrieve the user's geolocation information.

## Usage

1. Run the program using Python.
2. The Windoser Weather App window will open.
3. Select a city from the dropdown list or leave it empty to use geolocation.
4. Click the "Submit" button to retrieve the weather data.
5. The weather information will be displayed in the respective labels on the window.
6. The displayed weather information includes the weather climate, wind speed, temperature, pressure, humidity, and cloud cover.
7. Close the window to exit the application.

## Requirements

- Python 3.x
- tkinter library
- requests library
- geocoder library

## Installation

1. Install Python from the official Python website: [Python Downloads](https://www.python.org/downloads/)
2. Install required libraries using pip:

```bash
pip install tkinter requests geocoder
```

## API Key

To use the WeatherAPI, you will need to sign up and obtain an API key. Visit the WeatherAPI website: [WeatherAPI](https://www.weatherapi.com/) to sign up and get your API key.

## License

Feel free to modify and use this code according to your needs.

## Author

MEET LIMBANI

## Acknowledgments

- Inspired by the desire to create a simple weather application using Python and Tkinter.