
clean:
	@find . -name *.pyc -delete
	@rm -rf venv

venv:
	@python3.7 -m venv venv
	@venv/bin/pip install -r requirements.txt

test: venv
	@venv/bin/pytest

perf_test_pil: venv
	@venv/bin/python3 -m timeit -r 10 -s 'from image import flip_copy_pixels, flip_numpy, IMAGE_512_512, IMAGE_1080_1920, IMAGE_3840_2160; from PIL import Image' 'image = Image.open(IMAGE_3840_2160); flip_copy_pixels(image=image)'

perf_test_numpy: venv
	@venv/bin/python3 -m timeit -r 10 -s 'from image import flip_copy_pixels, flip_numpy, IMAGE_512_512, IMAGE_1080_1920, IMAGE_3840_2160; from PIL import Image' 'image = Image.open(IMAGE_3840_2160); flip_numpy(image=image);'

run: venv
	@venv/bin/python image.py
