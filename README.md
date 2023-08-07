# TopTunes
TopTunes is an innovative Spotify automation tool that enhances your music experience. The app extracts the 10 best (most streamed) songs of selected artists, creating a personalized playlist for you. With TopTunes, your favorite artists' top hits are just a click away, organized in a playlist and ready to play.

Requirements
1. Python 3.7 or later
2. A Spotify Developer account and the necessary API credentials (Client ID, Client Secret, and Redirect URI)

Setup and Installation
1. Clone this repository to your local machine.
git clone https://github.com/<your-username>/spotify-top-tracks-playlist.git
cd spotify-top-tracks-playlist

2. Install the required Python packages.
pip install -r requirements.txt

3. Create a .env file in the root directory of the project, and add your Spotify API credentials.
SPOTIFY_CLIENT_ID=<your-spotify-client-id>
SPOTIFY_CLIENT_SECRET=<your-spotify-client-secret>
SPOTIFY_REDIRECT_URI=<your-spotify-redirect-uri>

Replace <your-spotify-client-id>, <your-spotify-client-secret>, and <your-spotify-redirect-uri> with your actual Spotify credentials.

4. Run the application.
python main.py

How to Use
1. When you run the application, it will prompt you to enter a URL. To get this URL, you'll need to authenticate with Spotify. The application will provide you with a URL to navigate to in your web browser, where you will log in to Spotify and authorize the application.

2. After logging in and authorizing the application, you'll be redirected to a URL. Copy this entire URL and paste it into the application.

3. The application will then ask you to enter the names of the artists you're interested in, separated by commas.

4. After you enter the artist names, the application will handle the rest. It will search for the artists, fetch their top tracks, create a new playlist, and populate the playlist with these tracks.

5. You can then enjoy your new playlist on Spotify!
