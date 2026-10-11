"""
Basic Weather App (Beginner Tier)
Oasis Infobyte SIP - Python Programming Track - Task 4

Fetches real-time weather for a city name or ZIP code using the free
OpenWeatherMap API and displays temperature (C and F), humidity,
weather description and wind speed.

API key: put it in a file named api_key.txt next to this script
(or set the OPENWEATHER_API_KEY environment variable).
NEVER upload your API key to GitHub.
"""

import os
import sys

import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"
TIMEOUT_SECONDS = 10
DEFAULT_COUNTRY = "IN"  # used when only a ZIP/PIN code is typed


class WeatherError(Exception):
    """Raised for any problem fetching or reading weather data."""


def load_api_key():
    """Read the API key from the environment or from api_key.txt."""
    key = os.environ.get("OPENWEATHER_API_KEY", "").strip()
    if key:
        return key

    key_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "api_key.txt")
    if os.path.exists(key_file):
        with open(key_file, "r", encoding="utf-8") as f:
            key = f.read().strip()
        if key:
            return key

    raise WeatherError(
        "No API key found. Create a file named api_key.txt in this folder "
        "and paste your OpenWeatherMap API key into it."
    )


def build_params(location, api_key):
    """Work out whether the user typed a city name or a ZIP code."""
    params = {"appid": api_key, "units": "metric"}
    first_part = location.split(",")[0].strip()

    if first_part.isdigit():
        # ZIP / PIN code. Accepts "560001" or "94040,US".
        if "," in location:
            params["zip"] = location.replace(" ", "")
        else:
            params["zip"] = f"{first_part},{DEFAULT_COUNTRY}"
    else:
        params["q"] = location
    return params


def fetch_weather(location, api_key):
    """Call the API and return the parsed JSON, or raise WeatherError."""
    try:
        response = requests.get(
            API_URL, params=build_params(location, api_key), timeout=TIMEOUT_SECONDS
        )
    except requests.exceptions.Timeout:
        raise WeatherError("The request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        raise WeatherError("Network error. Please check your internet connection.")
    except requests.exceptions.RequestException as err:
        raise WeatherError(f"Something went wrong with the request: {err}")

    if response.status_code == 401:
        raise WeatherError(
            "Invalid API key. Check api_key.txt (new keys can take up to a "
            "couple of hours to activate)."
        )
    if response.status_code == 404:
        raise WeatherError(f"Location '{location}' was not found. Check the spelling.")
    if response.status_code == 429:
        raise WeatherError("Too many requests. Please wait a minute and try again.")
    if response.status_code != 200:
        raise WeatherError(f"The weather service returned an error ({response.status_code}).")

    try:
        return response.json()
    except ValueError:
        raise WeatherError("The weather service sent an unreadable response.")


def parse_weather(data):
    """Pull out the fields we want to display."""
    try:
        temp_c = data["main"]["temp"]
        return {
            "place": f'{data["name"]}, {data["sys"]["country"]}',
            "temp_c": temp_c,
            "temp_f": temp_c * 9 / 5 + 32,
            "feels_like_c": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "wind_ms": data["wind"]["speed"],
        }
    except (KeyError, IndexError, TypeError):
        raise WeatherError("The weather data was incomplete. Please try again.")


def display_weather(info):
    """Print the weather report."""
    print("\n" + "=" * 36)
    print(f"  Weather in {info['place']}")
    print("=" * 36)
    print(f"  Temperature : {info['temp_c']:.1f} °C / {info['temp_f']:.1f} °F")
    print(f"  Feels like  : {info['feels_like_c']:.1f} °C")
    print(f"  Condition   : {info['description']}")
    print(f"  Humidity    : {info['humidity']}%")
    print(f"  Wind speed  : {info['wind_ms']} m/s ({info['wind_ms'] * 3.6:.1f} km/h)")
    print("=" * 36 + "\n")


def main():
    print("=" * 36)
    print("          WEATHER APP")
    print("=" * 36)

    try:
        api_key = load_api_key()
    except WeatherError as err:
        print(f"\nError: {err}")
        sys.exit(1)

    while True:
        location = input("Enter a city name or ZIP code (e.g. Bengaluru or 560001): ").strip()
        if not location:
            print("  Error: location cannot be empty.")
            continue

        try:
            info = parse_weather(fetch_weather(location, api_key))
            display_weather(info)
        except WeatherError as err:
            print(f"  Error: {err}\n")

        again = input("Check another location? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using the Weather App!")
            break
        print()


if __name__ == "__main__":
    main()
