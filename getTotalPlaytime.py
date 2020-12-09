from getTotalScrobbles import *

def getTotalPlaytime(user, start, end):
    max_pages = 1
    playtime = 0
    page = 1
    counter = 0
    counter0 = 0
    while page <= max_pages:
        payload = {
            'method': 'user.getTopTracks',
            'page': page,
            'limit': 200,
            'user': user,
            'period': '12month'
        }
        # print some output so we can see the status
        #print("Requesting page {}/{}".format(page, max_pages))

        r = lastfm_get(payload)
        r_json = r.json()
        total_pages = int(r.json()['toptracks']['@attr']['totalPages'])
        if page + 2 >= total_pages:
            break

        for i in range(len(r_json['toptracks']['track'])):
            counter += 1
            r_artist = r_json['toptracks']['track'][i]['artist']['name']
            r_song = r_json['toptracks']['track'][i]['name']
            payload = {
                'method': 'track.getInfo',
                'track': r_song,
                'artist': r_artist,
            }
            r2 = lastfm_get(payload)
            r2_json = r2.json()
            r2_duration = r2_json['track']['duration']
            if (int(r2_duration) == 0):
                counter0 += 1
            playtime += int(r2_duration)

        page += 1
    total_scrobbles = getTotalScrobbles(user, start, end)
    avg_duration = playtime / (counter - counter0)
    return avg_duration / (1000 * 60), avg_duration * total_scrobbles / (1000 * 60), total_scrobbles