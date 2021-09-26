import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
# from spotify.KEYS.spotifyKeys import *

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getID(name):
    res1 = sp.search(name, limit=1)
    res2 = res1['tracks']
    res3 = dict(res2['items'][0])
    res4 = res3['album']
    res5 = dict(res4['artists'][0])
    return res5['id']


def getTop10Songs(name):
    topSongs = []
    id = getID(name)
    res1 = sp.artist_top_tracks(id)['tracks']
    for i in res1:
        topSongs.append(i['name'])
    return topSongs


def getTopAlbums(name):
    albums = []
    id = getID(name)
    res1 = sp.artist_albums(id)['items']
    for i in res1:
        if i['album_type'] == 'album':
            count = 0
            temp = {"name": "", "image": ""}
            temp['name'] = i['name']
            image = i['images']
            temp['image'] = image[0]['url']
            for j in albums:
                if (j["name"] == i['name']):
                    count += 1
            if count == 0:
                albums.append(temp)

    return albums


def getRelatedArtists(name):
    related_artists = []
    id = getID(name)
    res1 = sp.artist_related_artists(id)['artists']
    for i in res1:
        related_artists.append(i['name'])
    return related_artists


def getArtistImage(name):
    id = getID(name)
    res1 = sp.artist(id)['images']
    return res1[0]['url']


def getArtistGenre(name):
    genres = []
    id = getID(name)
    res1 = sp.artist(id)['genres']
    for i in res1:
        genres.append(i)
    return genres


def getAll(name):
    info = {"name": name, "genre": "", "top songs": "", "albums": "", "related artists": "", "image": ""}
    info['genre'] = getArtistGenre(name)
    info['top songs'] = getTop10Songs(name)
    info["albums"] = getTopAlbums(name)
    info['related artists'] = getRelatedArtists(name)
    info['image'] = getArtistImage(name)
    return info
