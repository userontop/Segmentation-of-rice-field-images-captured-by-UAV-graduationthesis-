import cv2
import os
import glob
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt


file_path = 'Data_set/'
for filename in glob.glob(os.path.join(file_path, '*.JPG')):

        print("Data_set_resizes/"+path)
        img = cv2.imread(filename)
        # Scale image
        h, w, c = img.shape
        imgScale = cv2.resize(img, (int(w/8), int(h/8)), interpolation = cv2.INTER_LINEAR)
        print('scale image shape: {}'.format(imgScale.shape))
        plt.subplot(121),plt.imshow(imgScale),plt.title('Origin Image')
        plt.subplot(122),plt.imshow(imgScale),plt.title('Scale Image')
        high, weight, ca = imgScale.shape
        print("({},{})".format(high, weight))
        cv2.imwrite("Data_set_resizes/" + path, imgScale)
