#! /usr/bin/env python
# -*- coding: utf-8 -*-


# adapted from source: http://numba.pydata.org/numba-doc/dev/user/examples.html

from matplotlib.pyplot import imshow, show, cm, savefig
import numpy as np


def mandel(x, y, max_iters):
    """
    Given a complex number x + y*j, determine
    if it is part of the Mandelbrot set given
    a fixed number of iterations.
    """
    i = 0
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 1e3:
            return i

    return 255


def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color

    return image

resx = 500
resy = 500

image = np.zeros((resx, resy), dtype=np.uint8)

xmin, xmax, ymin, ymax = -2.0, 1.0, -1.0, 1.0

create_fractal(xmin, xmax, ymin, ymax, image, 255)

# set special colormap
imshow(image, extent=(xmin, xmax, ymin, ymax), cmap=cm.plasma)
show()
