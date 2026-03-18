"""
Exercise 1 — GitHub Profile Fetcher
Fetches a user's profile + top repos from the GitHub public API.

Usage:
    python exercise_1.py octocat
    python exercise_1.py        (defaults to "torvalds")
"""

import sys
import requests


def fetch_profile(username):
    url = f"https://api.github.com/users/{username}"
    resp = requests.get(url)

    if resp.status_code == 404:
        print(f"User '{username}' not found.")
        return None
    elif resp.status_code == 403:
        print("Rate limit hit. GitHub allows 60 requests/hour without a token.")
        print("Wait a bit and try again.")
        return None
    elif resp.status_code != 200:
        print(f"Something went wrong. Status code: {resp.status_code}")
        return None

    return resp.json()


def fetch_top_repos(username, count=5):
    url = f"https://api.github.com/users/{username}/repos"
    params = {"sort": "stars", "direction": "desc", "per_page": count}
    resp = requests.get(url, params=params)

    if resp.status_code != 200:
        print("Could not fetch repos.")
        return []

    return resp.json()


def display_profile(profile):
    name = profile.get("name") or profile["login"]
    bio = profile.get("bio") or "No bio"
    repos = profile.get("public_repos", 0)
    followers = profile.get("followers", 0)

    print(f"\n  User:      {name} (@{profile['login']})")
    print(f"  Bio:       {bio}")
    print(f"  Public repos: {repos}")
    print(f"  Followers:    {followers}")


def display_repos(repos):
    if not repos:
        print("  No repos found.")
        return

    print(f"\n  Top {len(repos)} repos by stars:")
    print(f"  {'Repo':<30} {'Stars':>6}  {'Language'}")
    print("  " + "-" * 55)
    for r in repos:
        name = r["name"]
        stars = r.get("stargazers_count", 0)
        lang = r.get("language") or "—"
        print(f"  {name:<30} {stars:>6}  {lang}")


def main():
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = "torvalds"
        print(f"No username provided, defaulting to '{username}'")

    try:
        profile = fetch_profile(username)
    except requests.exceptions.ConnectionError:
        print("Network error — check your internet connection.")
        return

    if profile is None:
        return

    display_profile(profile)

    try:
        repos = fetch_top_repos(username)
    except requests.exceptions.ConnectionError:
        print("Network error while fetching repos.")
        return

    display_repos(repos)
    print()


if __name__ == "__main__":
    main()
