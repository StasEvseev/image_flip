# Image Flip

This is a research about fast image flip implementation.

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

## Research

There were two methods implemented to demonstrate that copying and flipping has their limits
(it require more resource as amount of pixels grow).

| Method/Size                                                                              | 512x512  | 1920x1080 | 3840x2160 |
| ---------------------------------------------------------------------------------------- |:--------:| ---------:| ---------:|
| Copying pixels                                                                           | 288 msec | 2.28 sec  | 9.69 sec  |
| [Flip array](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fliplr.html)     | 14.1 msec      |   72.4 msec | 263 msec |

