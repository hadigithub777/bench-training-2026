# Day 4 — APIs + Requests

Two scripts that talk to real APIs over the internet using the `requests` library.

## Scripts

### exercise_1.py — GitHub Profile Fetcher

Fetches any GitHub user's profile and their top 5 repos sorted by stars.

```bash
python3 exercise_1.py torvalds
```

Example output:

```
  User:      Linus Torvalds (@torvalds)
  Bio:       No bio
  Public repos: 11
  Followers:    291297

  Top 5 repos by stars:
  Repo                            Stars  Language
  -------------------------------------------------------
  HunspellColorize                  314  C
  AudioNoise                       4291  C
  GuitarPedal                      1824  C
  1590A                             548  OpenSCAD
  libgit2                           342  C
```

Handles 404 (user not found), 403 (rate limit), and connection errors.

### exercise_2.py — Weather CLI

Chains two API calls: first geocodes a city name to coordinates, then fetches current weather.

```bash
python3 exercise_2.py Lahore
python3 exercise_2.py "New York"
```

Example output:

```
  City:        Lahore, Pakistan
  Temperature: 17.6°C / 63.7°F
  Wind speed:  6.8 km/h
  Conditions:  Overcast
```

Uses Open-Meteo (free, no API key). Handles unknown cities and network errors.

## What Was Hard

The hardest part was figuring out the shape of the JSON before writing any extraction code. The GitHub API returns a flat object for a user profile, but repos come back as an array and the star count field is called `stargazers_count` not `stars` — had to print the raw response first to see that.

For the weather script, the tricky bit was that you need two separate APIs (geocoding and forecast) and you have to chain them: first call gives you lat/lon, second call uses those. Also the weather condition comes back as a numeric WMO code, not a string, so I had to map those to descriptions manually.
