#!/usr/bin/env python3

from PIL import Image
import numpy as np

# creating a image1 object
im1 = Image.open("crypted1.png")
#.convert("1")

# creating a image2 object
im2 = Image.open("crypted2.png")
#.convert("1")

# Make into Numpy arrays
im1np = np.array(im1)*255
im2np = np.array(im2)*255

# XOR with Numpy
result = np.bitwise_xor(im1np, im2np).astype(np.uint8)

# Convert back to PIL image and save
Image.fromarray(result).save('result.png')
