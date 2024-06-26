from io import BytesIO
from django.core.files import File
from PIL import Image


def make_thumbnail(image, size=(100, 100)):
    """Makes thumbnails of given size from given image"""

    im = Image.open(image)
    im.convert("RGB") # convert mode
    im.thumbnail(size) # resize image
    thumb_io = BytesIO() # create a BytesIO object
    im.save(thumb_io, "JPEG", quality=85) # save image to BytesIO object
    thumbnail = File(thumb_io, name=image.name) # create a django friendly File object
    return thumbnail