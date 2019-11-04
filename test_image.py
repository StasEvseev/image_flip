import hashlib
from PIL import Image

from image import flip_copy_pixels, flip_numpy, IMAGE_512_512


def hash_image(img: Image):
    return hashlib.md5(img.tobytes()).hexdigest()


def test_flip():
    image = Image.open(IMAGE_512_512)

    image_flip = flip_copy_pixels(image=image)
    image_double_flip = flip_copy_pixels(image=image_flip)

    assert hash_image(image) != hash_image(image_flip)
    assert hash_image(image) == hash_image(image_double_flip)


def test_flip_numpy():
    image = Image.open(IMAGE_512_512)

    image_flip = flip_numpy(image=image)
    image_double_flip = flip_numpy(image=image_flip)

    assert hash_image(image) != hash_image(image_flip)
    assert hash_image(image) == hash_image(image_double_flip)
