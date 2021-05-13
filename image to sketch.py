#image input user jode levanu set karvanu baki 6e.


import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "4.jpeg" #take image import here

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,.1140])
# it is 2 dimensional array that is the formula to convert image to gray scale.

def dodge(front,back):
    final_sketch = front*255/(255-back)
    #if image is greater than 255 which i don't think is possible if it is there will convert it to 255
    final_sketch[final_sketch>255]=255
    final_sketch[back == 255]= 255
    #to convert any suitable existing column to categorical type we will use apect function
    # and uint8 is for 8-bit signed integer
    return final_sketch.astype('uint8')


ss = imageio.imread(img)
gray = rgb2gray(ss)

i = 255-gray  #0,0,0 is the darkest color and 255,255,255 is for brightest color which is probably white color

#to convert into a blur image

blur = scipy.ndimage.filters.gaussian_filter(i,sigma =13)

# sigma is the intensity of blurness of image

r = dodge(blur, gray) # this function will convert our image to sketch by talking two parameter as blur and gray


cv2.imwrite('4.png',r)






