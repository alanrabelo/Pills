from hoough import *
import sys
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from Queue import *

def simple_region_growing(img, seedX, seedY, threshold):
    pixelsSearched = 0

    seedPoints = Queue()
    seedPoints.enqueue([seedX, seedY])
    visitedPixels = Queue()

    img = list(img)
    plt.imshow(list(img))

    while seedPoints.size() > 0:
        pixelsSearched += 1
        if pixelsSearched % 100 == 0:
            print(pixelsSearched / float(len(img[0]) * len(img)))
        #
        # if pixelsSearched > len(img[0]) * len(img):
        #     break

        currentSeed = seedPoints.dequeue()
        visitedPixels.enqueue(currentSeed)

        currentNeighbours = [[currentSeed[0]-1, currentSeed[1]],
                             [currentSeed[0],   currentSeed[1]-1],
                             [currentSeed[0]+1, currentSeed[1]],
                             [currentSeed[0],   currentSeed[1]+1]
                            ]

        for neighbor in currentNeighbours:
            if neighbor not in visitedPixels.queue and not isMargin(img, neighbor) and isSimilar(img, currentSeed, neighbor, threshold):
                seedPoints.enqueue(neighbor)

    segmentation = np.zeros((len(img), len(img[0])))
    for pixel in visitedPixels.queue:
        segmentation[pixel[0]][pixel[1]] = 1
    print(str(pixelsSearched) + " Iteracoes")
    # print(str(len(selectedPixels)) + " Selected pixels")

    plt.imshow(list(segmentation))
    plt.show()

    return visitedPixels

import math
def isSimilar(image, seed1, seed2, treshold):

    pixel1 = int(image[seed1[0]][seed1[1]])
    pixel2 = int(image[seed2[0]][seed2[1]])
    return abs(pixel1 - pixel2) < treshold

def isMargin(image, seed):
    return seed[0] < 0 \
           or seed[0] > len(image)-1\
           or seed[1] < 0 \
           or seed[1] > len(image[0])-1




    """
    A (very) simple implementation of region growing.
    Extracts a region of the input image depending on a start position and a stop condition.
    The input should be a single channel 8 bits image and the seed a pixel position (x, y).
    The threshold corresponds to the difference between outside pixel intensity and mean intensity of region.
    In case no new pixel is found, the growing stops.
    Outputs a single channel 8 bits binary (0 or 255) image. Extracted region is highlighted in white.
    """


