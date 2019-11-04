# Image Flip

This is a research about fast image flip implementation.

## Requirements

 - algorithm should be size indifferent
 - one threaded
 - being generic solution


## Stack

 - pillow
 - numpy


## Demonstration

```bash
make run
```

## Testing

```bash
make test
```

## Outcome

There were two methods implemented to demonstrate that copying and flipping has their limits
(it require more resource as amount of pixels grow), therefore it doesn't fit to one of our needs.

| Method/Size                                                                              | 512x512  | 1920x1080 | 3840x2160 |
| ---------------------------------------------------------------------------------------- |:--------:| ---------:| ---------:|
| Copying pixels                                                                           | 288 msec | 2.28 sec  | 9.69 sec  |
| [Flip array](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fliplr.html)     | 14.1 msec      |   72.4 msec | 263 msec |

The fastest method might be not to flip pixels(arrays), but control rendering part and display images
in different order, or use some device to flip images for you (like actually mirroring it physically).
