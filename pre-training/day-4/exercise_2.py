"""
Exercise 2 — Weather CLI
Fetches current weather for any city using Open-Meteo (free, no API key).
Chains two API calls: geocoding (city -> lat/lon) then weather (lat/lon -> conditions).

Usage:
    python exercise_2.py London
    python exercise_2.py "New York"
    python exercise_2.py              (defaults to Lahore)
"""

import sys
import requests


# WMO weather codes -> human-readable descriptions
# (only the common ones, there are more but these cover most cases)
WMO_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def geocode_city(city_name):
    """Turn a city name into latitude, longitude, and the matched name."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1}
    resp = requests.get(url, params=params)

    if resp.status_code != 200:
        print(f"Geocoding failed (status {resp.status_code})")
        return None

    data = resp.json()
    results = data.get("results")
    if not results:
        print(f"Could not find a city called '{city_name}'.")
        return None

    hit = results[0]
    return {
        "name": hit["name"],
        "country": hit.get("country", ""),
        "lat": hit["latitude"],
        "lon": hit["longitude"],
    }


def fetch_weather(lat, lon):
    """Get current weather for given coordinates."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
    }
    resp = requests.get(url, params=params)

    if resp.status_code != 200:
        print(f"Weather API failed (status {resp.status_code})")
        return None

    return resp.json().get("current_weather")


def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 1)


def main():
    if len(sys.argv) > 1:
        city_name = " ".join(sys.argv[1:])
    else:
        city_name = "Lahore"
        print(f"No city provided, defaulting to '{city_name}'")

    try:
        location = geocode_city(city_name)
    except requests.exceptions.ConnectionError:
        print("Network error — check your internet connection.")
        return

    if location is None:
        return

    try:
        weather = fetch_weather(location["lat"], location["lon"])
    except requests.exceptions.ConnectionError:
        print("Network error while fetching weather.")
        return

    if weather is None:
        return

    temp_c = weather["temperature"]
    temp_f = celsius_to_fahrenheit(temp_c)
    wind = weather["windspeed"]
    code = weather.get("weathercode", -1)
    description = WMO_CODES.get(code, f"Unknown (code {code})")

    print(f"\n  City:        {location['name']}, {location['country']}")
    print(f"  Temperature: {temp_c}°C / {temp_f}°F")
    print(f"  Wind speed:  {wind} km/h")
    print(f"  Conditions:  {description}")
    print()


if __name__ == "__main__":
    main()
