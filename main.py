from hoough import *
from region_growth import *

import glob

def detect_circles(filename):
    image_list = []
    img = imarray(filename)
    image_list.append(img)
    # res = smoothen(img,display=True)                                               #set display to True to display the edge image
    res = edge(img,170,display=False)                                               #set display to True to display the edge image
    #detectCircles takes a total of 4 parameters. 3 are required.
    #The first one is the edge image.
    # Second is the thresholding value and
    # the third is the region size to detect peaks.
    #The fourth is the radius range.
    # res = detectCircles(img,8.1,15,radius=[100,1])
    res = detectCircles(img,12,15,radius=[85,25])
    circles = displayCircles(res, filename)

    return circles


def distance(pixel1, pixel2):
    return ((pixel1[0] - pixel2[0])**2 + (pixel1[1] - pixel2[1])**2)**0.5


circles = detect_circles('images/Medium cut/3026_lg.jpg')
image = imarray('images/Medium cut/3026_lg.jpg')

x = int(len(list(image)) / 2)
y = x
#
# if len(circles)>0:
#     y = circles[0][1]
#     x = circles[0][2]

simple_region_growing(image, x, y, 16)

# for filename in glob.glob('images/Medium cut/*.jpg'):
# circles = detect_circles('images/Medium cut/3829_lg.jpg')

# print(circles)
