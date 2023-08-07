# main.py

import spotify_auth
import spotify_search

# Get the access token
access_token = spotify_auth.get_access_token()

# Ask the user to enter the names of the artists
artist_names = input("Enter the names of the artists, separated by commas: ").split(',')

# Get the artist IDs
artist_ids = spotify_search.get_artist_ids(artist_names, access_token)

# Get the top tracks
top_track_ids = spotify_search.get_top_tracks(artist_ids, access_token)

# Create a new playlist
user_id = spotify_auth.get_current_user_id(access_token)
playlist_id = spotify_auth.create_playlist(user_id, access_token)
print(playlist_id)

# Add the top tracks to the new playlist
spotify_auth.add_tracks_to_playlist(playlist_id, top_track_ids, access_token)
