import pandas as pd
from API import *

def getTopXArtists(user, X):
    payload = {
        'method': 'user.getTopArtists',
        'period': '12month',
        'limit': X,
        'user': user
    }

    r = lastfm_get(payload)
    r_json = r.json()
    r_artists = r_json['topartists']['artist']

    toplist = pd.DataFrame({'Artist': [r_artists[0]['name']],
                            'Playcount': [r_artists[0]['playcount']],
                            'Image': [r_artists[0]['image'][2]['#text']]})

    for i in range(1, X):
        temp = pd.DataFrame({'Artist': [r_artists[i]['name']],
                             'Playcount': [r_artists[i]['playcount']],
                             'Image': [r_artists[i]['image'][2]['#text']]})

        toplist = toplist.append(temp, ignore_index=True)

    return toplist