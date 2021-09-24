from KEYS.spotifyKeys import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

res1 = sp.search("The Weeknd", limit=1)
res2 = res1['tracks']
res3 = dict(res2['items'][0])
res4 = res3['album']
res5 = dict(res4['artists'][0])
id = res5['id']
res6 = sp.artist_top_tracks(id)['tracks']
topSongs = []
for i in res6:
    topSongs.append(i['name'])

print(topSongs)