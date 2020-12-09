from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests


def createAlbumCollage(toplist, cols=5, rows=5):
    img = Image.open(BytesIO(requests.get(toplist['Image'][0]).content))
    w, h = img.size
    collage_width = cols * w
    collage_height = rows * h
    new_image = Image.new('RGB', (collage_width, collage_height))
    cursor = (0, 0)
    for i in range(len(toplist)):
        if toplist['Image'][i] == '':
            toplist['Image'][i] = 'https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png'
        img = Image.open(BytesIO(requests.get(toplist['Image'][i]).content))
        # place image
        new_image.paste(img, cursor)

        # move cursor
        y = cursor[1]
        x = cursor[0] + w
        if cursor[0] >= (collage_width - w):
            y = cursor[1] + h
            x = 0
        cursor = (x, y)

    return new_image
