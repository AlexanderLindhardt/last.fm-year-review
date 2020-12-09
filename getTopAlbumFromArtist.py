import pandas as pd
from API import *

def getTopAlbumFromArtist(user, artist):
    payload = {
        'method': 'user.getTopAlbums',
        'period': '12month',
        'limit': 200,
        'user': user
    }

    r = lastfm_get(payload)
    r_json = r.json()
    r_albums = r_json['topalbums']['album']
    for i in range(200):
        if r_albums[i]['artist']['name'] == artist:
            return pd.DataFrame({'Artist': [r_albums[i]['artist']['name']],
                                 'Album': [r_albums[i]['name']],
                                 'Playcount': [r_albums[i]['playcount']],
                                 'Image': [r_albums[i]['image'][2]['#text']]})