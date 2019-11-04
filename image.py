from PIL import Image, ImageDraw


def flip(image):
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


def main():
    image = Image.open('Lenna.png')
    image.show()

    # Create output image
    output_image = flip(image=image)
    output_image.show()


if __name__ == "__main__":
    main()
