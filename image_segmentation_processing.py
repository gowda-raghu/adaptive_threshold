import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def adaptive_thresh(path):
    img = cv2.imread(path,0)
    width, height = 150, 150        #dimensions of the region of interest is to defined wrt image selected.
    x, y = 250, 350
    # Crop image to specified area using slicing
    img = img[y:y+height, x:x+width]
    img = cv.medianBlur(img,3)
    ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY,11,2)
    th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv.THRESH_BINARY,11,2)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

path =r'C:\Autosys_internship\Assignment for Internship_at_Autoyos\Internship at Autoyos\4.png'
adaptive_thresh(path)
plt.imshow(images[2],'gray')
