# spotify_auth.py

import os
import re
import hashlib
import base64
import requests
import webbrowser
import urllib.parse
import secrets


# Your app's client ID and redirect URI
client_id = 'bcd4271eebc442fc875574ad8c34eebe'  # replace with your actual client ID
client_secret = 'd895000f8287499fbf5adf346afa38a9'  # replace with your actual client secret
redirect_uri = 'http://localhost:8080'  # replace with your actual redirect URI

# The scopes your app is requesting access to
SCOPES = 'user-library-read playlist-modify-public'  # or other scopes depending on your needs

# Spotify Users API URL
USERS_URL = 'https://api.spotify.com/v1/users'

# The Spotify Accounts Authorization API URL
AUTH_URL = 'https://accounts.spotify.com/authorize?response_type=code&client_id={}&redirect_uri={}&scope=user-read-private%20user-read-email%20playlist-modify-public%20playlist-modify-private&state=34fFs29kd09'.format(client_id, redirect_uri)
TOKEN_URL = 'https://accounts.spotify.com/api/token'


# This function gets the access token and gives authorization to the app
def get_access_token():
    # Request access from the user
    code_verifier = base64.urlsafe_b64encode(os.urandom(40)).decode('utf-8')
    code_verifier = re.sub('[^a-zA-Z0-9]+', '', code_verifier)
    code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode('utf-8')).digest()).decode('utf-8')
    code_challenge = code_challenge.replace('=', '').replace('+', '-').replace('/', '_')
    authorization_url = f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&code_challenge_method=S256&code_challenge={code_challenge}&scope=playlist-modify-public%20playlist-modify-private"
    webbrowser.open(authorization_url)
    # The user will be redirected to the redirect_uri after they authorize the app. Take the code parameter from the url
    redirect_url = input("Enter the full redirect URL: ")
    auth_code = redirect_url.split('?code=')[1].split('&state=')[0]

    print("Authorization code:", auth_code)  # Print the authorization code

    # Request the access token
    token_data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri,
        "code_verifier": code_verifier
    }
    token_response = requests.post("https://accounts.spotify.com/api/token", data=token_data)
    token_response_json = token_response.json()

    print("Token response:", token_response.json())  # Print the token response

    access_token = token_response_json['access_token']
    return access_token

def get_current_user_id(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.get('https://api.spotify.com/v1/me', headers=headers)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful
    return response.json()['id']

def get_auth_url():
    state = secrets.token_hex(16)
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": "playlist-modify-public playlist-modify-private",
        "state": state
    }

    url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params)
    return url


# This function creates the playlist
def create_playlist(user_id, access_token):
    # The headers for the API requests
    HEADERS = {
        'Authorization': f"Bearer {access_token}",
        'Content-Type': 'application/json'
    }

    # The data for the create playlist request
    DATA = {
        'name': 'Top Tracks Playlist',
        'public': False
    }

    # Make a POST request to the Spotify Users API to create a new playlist
    create_response = requests.post(f"{USERS_URL}/{user_id}/playlists", headers=HEADERS, json=DATA)

    # Print the entire response
    print(create_response.json())

    # Get the ID of the new playlist from the response
    playlist_id = create_response.json()['id']

    return playlist_id


# This function adds the tracks to the playlist
def add_tracks_to_playlist(playlist_id, track_ids, access_token):
    # The headers for the API requests
    HEADERS = {
        'Authorization': f"Bearer {access_token}",
        'Content-Type': 'application/json'
    }

    # The data for the add tracks request
    DATA = {
        'uris': [f'spotify:track:{track_id}' for track_id in track_ids]
    }

    # Make a POST request to the Spotify Playlists API to add tracks to the playlist
    add_response = requests.post(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", headers=HEADERS, json=DATA)

    # Check if the request was successful
    if add_response.status_code == 201:
        print('Tracks added successfully')
    else:
        print('Failed to add tracks')



