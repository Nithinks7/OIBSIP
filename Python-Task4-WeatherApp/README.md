[README.md](https://github.com/user-attachments/files/33296351/README.md)
# Basic Weather App (Beginner Tier)

**Oasis Infobyte SIP | Python Programming Track | Task 4**

A command-line Python app that fetches real-time weather for any city or ZIP
code using the free OpenWeatherMap API.

## Features
- Accepts a city name (e.g. `Bengaluru`) or a ZIP/PIN code (e.g. `560001` or `94040,US`)
- Calls the OpenWeatherMap API and parses the JSON response
- Displays temperature in **°C and °F**, humidity, weather description and wind speed
- Handles errors gracefully: city not found, network timeout, no internet,
  invalid API key, rate limit, incomplete data
- Rejects empty input
- Check multiple locations without restarting

## Setup

**1. Install Python 3.6+ and the requests library**
```bash
pip install -r requirements.txt
```

**2. Get a free API key**
Sign up at https://openweathermap.org/api and copy your key from the *API keys*
tab. New keys can take up to a couple of hours to activate.

**3. Save your key**
Create a file named `api_key.txt` in this folder and paste only the key into it
(see `api_key.example.txt`). Alternatively, set the `OPENWEATHER_API_KEY`
environment variable.

> `api_key.txt` is listed in `.gitignore`, so your key is never uploaded to GitHub.

## How to Run
```bash
python weather_app.py
```
On Mac/Linux use `python3 weather_app.py`.

## Sample Output
```
Enter a city name or ZIP code (e.g. Bengaluru or 560001): Bengaluru

====================================
  Weather in Bengaluru, IN
====================================
  Temperature : 25.0 °C / 77.0 °F
  Feels like  : 25.6 °C
  Condition   : Scattered Clouds
  Humidity    : 60%
  Wind speed  : 3.5 m/s (12.6 km/h)
====================================
```

## Error Handling
| Situation | Message shown |
|-----------|---------------|
| Empty input | Location cannot be empty |
| Unknown city | Location was not found, check spelling |
| Wrong/inactive key | Invalid API key |
| No internet | Network error |
| Slow server | Request timed out |
| Too many requests | Please wait and try again |

## Tech Used
Python 3, `requests`, `json`, OpenWeatherMap Current Weather API (free tier)

## Notes
- A ZIP/PIN code without a country defaults to India (`IN`). Use `94040,US` format for other countries.
- Temperature in °F is calculated from °C: `F = C × 9/5 + 32`.

## Author
Nithin K S - https://github.com/Nithinks7
