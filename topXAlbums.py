import pandas as pd
from API import *


## GET TOP 25 ALBUMS THIS YEAR ##
def topXAlbums(user, X):
    payload = {
        'method': 'user.getTopAlbums',
        'user': user,
        'period': '12month',
        'limit': X
    }
    r = lastfm_get(payload)
    #jprint(r.json())
    r_json = r.json()
    r_albums = r_json['topalbums']['album']

    toplist = pd.DataFrame({'Artist': [r_albums[0]['artist']['name']],
                            'Album': [r_albums[0]['name']],
                            'Playcount': [r_albums[0]['playcount']],
                            'Image': [r_albums[0]['image'][2]['#text']]})

    for i in range(1, X):
        temp = pd.DataFrame({'Artist': [r_albums[i]['artist']['name']],
                             'Album': [r_albums[i]['name']],
                             'Playcount': [r_albums[i]['playcount']],
                             'Image': [r_albums[i]['image'][2]['#text']]})
        toplist = toplist.append(temp, ignore_index=True)

    return toplist
