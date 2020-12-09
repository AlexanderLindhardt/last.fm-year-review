import time
import datetime
from API import *


def getTotalScrobbles(user, start, end):
    payload = {
        'method': 'user.getRecentTracks',
        'page': 1,
        'limit': 200,
        'user': user,
        'from': int(time.mktime(datetime.datetime.strptime(start, "%d/%m/%Y").timetuple())),
        'to': int(time.mktime(datetime.datetime.strptime(end, "%d/%m/%Y").timetuple()))
    }
    r = lastfm_get(payload)
    r_json = r.json()
    total_pages = int(r.json()['recenttracks']['@attr']['totalPages'])

    payload = {
        'method': 'user.getRecentTracks',
        'page': total_pages,
        'limit': 200,
        'user': user,
        'from': int(time.mktime(datetime.datetime.strptime(start, "%d/%m/%Y").timetuple())),
        'to': int(time.mktime(datetime.datetime.strptime(end, "%d/%m/%Y").timetuple()))
    }
    r = lastfm_get(payload)
    r_json = r.json()
    return 200 * (total_pages - 2) + len(r_json['recenttracks']['track'])