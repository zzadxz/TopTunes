import spotify_auth
import spotify_search

if __name__ == "__main__":
    # Get the authorization URL
    auth_url = spotify_auth.get_auth_url()

    # Print the URL and prompt the user to visit it
    print(f"Please visit this URL to authorize the application: {auth_url}")

    # Get the full redirect URL from the user
    full_redirect = input("Enter the full redirect URL: ")

    # Extract the authorization code from the redirect URL
    code = spotify_auth.extract_auth_code(full_redirect)

    # Exchange the authorization code for an access token
    token_response = spotify_auth.code_to_token(code)

    # Extract the access token, refresh token, and expiration time
    access_token = token_response['access_token']
    refresh_token = token_response['refresh_token']
    expires_in = token_response['expires_in']

    # Get the user's ID
    user_id = spotify_auth.get_user_id(access_token)

    # Create a playlist
    playlist_id = spotify_auth.create_playlist(user_id, "Top Tracks Playlist")

    # Get the names of the artists
    artist_names = input("Enter the names of the artists, separated by commas: ").split(",")

    # For each artist
    for name in artist_names:
        # Get the top tracks
        top_tracks = spotify_search.get_top_tracks(name.strip(), access_token)

        # For each track
        for track in top_tracks:
            # Add the track to the playlist
            spotify_auth.add_track_to_playlist(user_id, playlist_id, track['id'], access_token)

    print("All tracks added to the playlist!")
