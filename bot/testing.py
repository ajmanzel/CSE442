
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def getTrackID(name, artist):
    client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    res1 = sp.search(name)
    res2 = res1['tracks']
    res3 = res2['items']
    for i in res3:
        if artist in str(i):
            tempname = str(i['name'])
            if tempname.__contains__(" ("):
                tempname = tempname.split(" (")[0]
            tempname = tempname.strip()

            if len(tempname) == len(name):
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

testvar = getRelatedSongs("STAY", "The Kid LAROI")
print(testvar)



