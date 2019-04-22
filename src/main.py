#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import cv2
import numpy as np

from PIL import Image

from perspective import correct_perspective

def main():
    im = Image.open(sys.argv[1])
    img = np.asarray(im)
    final = correct_perspective(img, intermediate=True)[-1]
    final.save('result.png')

if __name__ == '__main__':
    main()
