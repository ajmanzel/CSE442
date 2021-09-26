import os
from spotipy.client import Spotify
# from KEYS.spotifyKeys import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URL = os.environ.get('REDIRECT_URL')

scopes = "user-top-read playlist-read-collaborative user-read-currently-playing user-follow-read user-follow-modify user-read-email user-modify-playback-state user-read-recently-played app-remote-control user-read-playback-position user-read-playback-state ugc-image-upload"

test = "test"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope=scopes))
res = sp.current_user_top_tracks(limit=1)
print(res)
