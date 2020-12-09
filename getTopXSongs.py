import pandas as pd
from API import *


def getTopXSongs(user, X):
    payload = {
        'method': 'user.getTopTracks',
        'period': '12month',
        'limit': X,
        'page': 1,
        'user': user
    }

    r = lastfm_get(payload)
    r_json = r.json()
    r_tracks = r_json['toptracks']['track']

    toplist = pd.DataFrame({'Track': [r_tracks[0]['name']],
                            'Playcount': [r_tracks[0]['playcount']]})

    for i in range(1, X):
        temp = pd.DataFrame({'Track': [r_tracks[i]['name']],
                             'Playcount': [r_tracks[i]['playcount']]})
        toplist = toplist.append(temp, ignore_index=True)

    return toplist
