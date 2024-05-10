#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # URL of the Reddit API endpoint for fetching hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid "Too Many Requests" error
    headers = {"User-Agent": "Custom User Agent"}

    # Send GET request to the Reddit API
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    # Check if the response is successful (status code 200) and JSON content
    if response.status_code == 200 and "application/json" in response.headers.get("Content-Type", ""):
        # Parse JSON response
        data = response.json()
        # Extract titles of the first 10 hot posts
        posts = data.get("data", {}).get("children", [])
        if posts:
            print("Top 10 hot posts in subreddit '{}' :\n".format(subreddit))
            for post in posts:
                print(post["data"]["title"])
        else:
            print("Subreddit '{}' not found or has no hot posts.".format(subreddit))
    else:
        print("Subreddit '{}' not found or an error occurred.".format(subreddit))

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
