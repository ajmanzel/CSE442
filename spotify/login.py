from spotipy.client import Spotify
from KEYS.spotifyKeys import *
import spotipy

scopes = "user-top-read streaming user-library-read playlist-read-collaborative user-read-currently-playing user-follow-read user-follow-modify user-read-email user-modify-playback-state user-read-recently-played app-remote-control user-read-playback-position user-read-playback-state ugc-image-upload"

oauth_object = spotipy.SpotifyOAuth(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    redirect_uri = REDIRECT_URL,
    scope = scopes
)

token_dict = oauth_object.get_access_token()
spotify_object = spotipy.Spotify(auth=token_dict['access_token'])
tracks = spotify_object.current_user_top_tracks(limit=10, time_range='medium_term')
print(tracks)
