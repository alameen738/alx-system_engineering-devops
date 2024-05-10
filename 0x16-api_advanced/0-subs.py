#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    # URL of the Reddit API endpoint for fetching subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid "Too Many Requests" error
    headers = {"User-Agent": "Custom User Agent"}

    # Send GET request to the Reddit API
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

    # Check if the response is successful (status code 200) and JSON content
    if response.status_code == 200 and "application/json" in response.headers.get("Content-Type", ""):
        # Parse JSON response
        data = response.json()
        # Extract the number of subscribers from the response
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    else:
        # Invalid subreddit or other error, return 0
        return 0

# Example usage
if __name__ == "__main__":
    subreddit_name = "learnpython"
    print(f"Number of subscribers in subreddit '{subreddit_name}': {number_of_subscribers(subreddit_name)}")
