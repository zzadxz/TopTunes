# spotify_search.py

import requests
import time

# Spotify Search API URL
SEARCH_URL = 'https://api.spotify.com/v1/search'
# Spotify Artists API URL
ARTISTS_URL = 'https://api.spotify.com/v1/artists'


# This function gets the name of the artists
def get_artist_ids(artist_names, access_token):
    # The headers for the API requests
    HEADERS = {
        'Authorization': f"Bearer {access_token}",
    }

    # The parameters for the search requests
    SEARCH_PARAMS = {
        'type': 'artist',
        'limit': 1,
    }

    # A list to store the IDs of the artists
    artist_ids = []

    # Search for each artist
    for name in artist_names:
        # Update the search parameters with the current artist's name
        SEARCH_PARAMS['q'] = name.strip()
        # Make a GET request to the Spotify Search API
        search_response = requests.get(SEARCH_URL, params=SEARCH_PARAMS, headers=HEADERS)
        # Get the ID of the first artist from the response
        artist_id = search_response.json()['artists']['items'][0]['id']
        # Add the artist ID to the list
        artist_ids.append(artist_id)

    return artist_ids

# This function gets the top (most streamed) tracks of the artists
def get_top_tracks(artist_ids, access_token):
    # The headers for the API requests
    HEADERS = {
        'Authorization': f"Bearer {access_token}",
    }

    # A list to store the IDs of the top tracks
    top_track_ids = []

    # Get the top tracks for each artist
    for artist_id in artist_ids:
        # Make a GET request to the Spotify Artists API
        top_tracks_response = requests.get(f"{ARTISTS_URL}/{artist_id}/top-tracks?country=US", headers=HEADERS)

        # Check if the request was successful
        if top_tracks_response.status_code == 200:
            # Get the top tracks from the response
            top_tracks = top_tracks_response.json().get('tracks', [])
            # Add the IDs of the top tracks to the list
            for track in top_tracks:
                top_track_ids.append(track['id'])
        else:
            print(f"Failed to get top tracks for artist {artist_id}. Status code: {top_tracks_response.status_code}")


    return top_track_ids

