from flask import Flask, request, redirect
import spotify_auth
import main
import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    auth_url = spotify_auth.get_auth_url()
    logging.debug('About to do something...')
    return redirect(auth_url)


@app.route('/callback/')
def callback():
    code = request.args.get('code')
    spotify_auth.get_access_token(code)
    main.main_flow()
    logging.debug('About to do something...')
    return "Playlist created successfully!"

if __name__ == "__main__":
    app.run(port=8080)
