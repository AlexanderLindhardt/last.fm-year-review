import pandas as pd
from API import *

def getTop3SongsFromArtist(user, artist):
    counter = 0
    page = 1

    while counter < 3:
        payload = {
            'method': 'user.getTopTracks',
            'period': '12month',
            'limit': 200,
            'page': page,
            'user': user
        }

        r = lastfm_get(payload)
        r_json = r.json()
        r_tracks = r_json['toptracks']['track']
        for i in range(200):
            if r_tracks[i]['artist']['name'] == artist:
                if counter == 0:
                    toplist = pd.DataFrame({'Track': [r_tracks[i]['name']],
                                            'Playcount': [r_tracks[i]['playcount']]})
                else:
                    temp = pd.DataFrame({'Track': [r_tracks[i]['name']],
                                         'Playcount': [r_tracks[i]['playcount']]})
                    toplist = toplist.append(temp, ignore_index=True)
                counter += 1

    return toplist