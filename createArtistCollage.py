from getTopAlbumFromArtist import *
from getTopXArtists import *
from getTop3SongsFromArtist import *
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


def insert_name(image, name, cursor, width, height):
    draw = ImageDraw.Draw(image, 'RGBA')
    font = ImageFont.truetype("arial.ttf", size=20)
    x = cursor[0]
    y = cursor[1]
    draw.rectangle([(x, y + 200), (x + 300, y + 240)], (0, 0, 0, 123))
    draw.text((x + 8 + width, y + 10), name, (255, 255, 255), font=font)


def insert_text(image, text, cursor, width, height, row):
    draw = ImageDraw.Draw(image, 'RGBA')
    font = ImageFont.truetype("arial.ttf", size=20)
    x = cursor[0]
    y = cursor[1] + row * 25
    draw.rectangle([(x, y + 200), (x + 300, y + 240)], (0, 0, 0, 123))
    draw.text((x + 8 + width, y + 10), text, (255, 255, 255), font=font)


def createArtistCollage(toplist, rows, cols, user):
    img = Image.open(BytesIO(requests.get(toplist['Image'][0]).content))
    w, h = img.size

    collage_height = 10 * h
    collage_width = collage_height

    new_image = Image.new('RGB', (int(collage_width), int(collage_height / cols)))
    cursor = (0, 0)
    for i in range(len(toplist)):
        topAlbum = getTopAlbumFromArtist(user, getTopXArtists(user, 10)['Artist'][i])
        if topAlbum['Image'][0] == '':
            topAlbum['Image'][0] = 'https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png'

        img = Image.open(BytesIO(requests.get(topAlbum['Image'][0]).content))
        # place image
        new_image.paste(img, cursor)

        # add name
        insert_name(new_image,
                    str(i + 1) + '. ' + toplist['Artist'][i] + ' - ' + toplist['Playcount'][i] + ' scrobbles', cursor,
                    w, h)

        # add top album
        insert_text(new_image, 'Top Album: ' + topAlbum['Album'][0], cursor, w, h, 1)

        insert_text(new_image, 'Top 3 Songs: ', cursor, w, h, 2)

        top3songs = getTop3SongsFromArtist(user, toplist['Artist'][i])
        # add top 1 song
        insert_text(new_image, top3songs['Track'][0], cursor, w, h, 3)
        # add top 2 song
        insert_text(new_image, top3songs['Track'][1], cursor, w, h, 4)
        # add top 3 song
        insert_text(new_image, top3songs['Track'][2], cursor, w, h, 5)

        # move cursor
        x = cursor[0]
        y = cursor[1] + h
        if i == 4:
            x = int(collage_width / 2)
            y = 0
        cursor = (x, y)

    new_image.show()
