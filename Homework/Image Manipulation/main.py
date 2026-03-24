from matplotlib import pyplot as plt
from colorama import init, Fore
import numpy as np
import cv2

init(autoreset=True)

image = cv2.imread(r'Homework\Image Manipulation\example.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h, w = image_rgb.shape[:2]

grayscale_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(grayscale_image, cmap='gray')
plt.title("Grayscale Image")
plt.show()

brightened_image = cv2.add(image_rgb, np.ones(image.shape, dtype='uint8') * 40)
plt.imshow(brightened_image)
plt.title("Brightened Image")
plt.show()

cropped_image = image_rgb[int(h*0.05):int(h*0.45), int(w*0.35):int(w*0.65)]
plt.imshow(cropped_image)
plt.title("Cropped Image")
plt.show()

center = (h//2, w//2)
M = cv2.getRotationMatrix2D(center, 50, 1.0)
rotated = cv2.warpAffine(image_rgb, M, (w, h))
plt.imshow(rotated)
plt.title("Rotated Image")
plt.show()