import hashlib
from PIL import Image

from image import flip


def hash_image(img):
    return hashlib.md5(img.tobytes()).hexdigest()


def test_flip():
    image = Image.open('Lenna.png')

    image_flip = flip(image=image)
    image_double_flip = flip(image=image_flip)

    assert hash_image(image) != hash_image(image_flip)
    assert hash_image(image) == hash_image(image_double_flip)
