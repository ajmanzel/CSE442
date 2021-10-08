
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

CLIENT_ID = '63df2b90c04c413ebf70a5868bee07fb'
CLIENT_SECRET = 'ed55f9adf93d4e75853a7c2f7b5a2b66'

def getTrackID(name, artist):
    client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    res1 = sp.search(name)
    res2 = res1['tracks']
    res3 = res2['items']
    for i in res3:
        if artist in str(i):
            if len(i['name']) == len(name):
                return i['id']


def getRelatedSongs(name, artist):
    client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    arr = []
    id = getTrackID(name, artist)
    res1 = sp.recommendations([],[],[id])
    res2 = res1['tracks']
    for i in res2:
        temp = {"title": i['name'], "artist": ""}
        res3 = i['artists']
        res4 = res3[0]
        temp['artist'] = res4['name']
        arr.append(temp)
    return arr

testvar = getRelatedSongs("Blinding Lights", "The Weeknd")
print(testvar)



