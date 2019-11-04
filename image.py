from PIL import Image, ImageDraw
import numpy as np

IMAGE_512_512 = 'images/512x512.png'
IMAGE_1080_1920 = 'images/1080x1920.jpg'
IMAGE_3840_2160 = 'images/3840x2160.jpg'


def flip_copy_pixels(image: Image):
    image_pixels = image.load()
    output_image = Image.new("RGB", image.size)
    draw = ImageDraw.Draw(output_image)

    image_width, _ = image.size
    # Copy pixels
    for x in range(output_image.width):
        for y in range(output_image.height):
            xp = image_width - x - 1
            draw.point((x, y), image_pixels[xp, y])

    return output_image


def flip_numpy(image: Image):
    im = np.asarray(image)
    img_flip = Image.fromarray(np.fliplr(im), 'RGB')
    return img_flip


def main():
    image = Image.open(IMAGE_512_512)
    image.show()
    flip_numpy(image).show()


if __name__ == "__main__":
    main()
