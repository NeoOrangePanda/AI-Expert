import sys
import cv2
import numpy as np
from colorama import Fore, init

init(autoreset=True)

def image_rotation(image: np.ndarray, angle):
    (h, w) = image.shape[:2]
    center = (h // 2, w // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

def brightness(image: np.ndarray, brightness_multiplier):
    brightness_matrix = np.ones(image.shape, dtype='uint8') * brightness_multiplier
    brightened_image = cv2.add(image, brightness_matrix)
    return brightened_image

def cropping(image: np.ndarray, x1, y1, x2, y2): 
    cropped_image = image[y1:y2, x1:x2]
    return cropped_image

def resize(image: np.ndarray, width, height):
    resized_image = cv2.resize(image, (width, height))
    return resized_image

def run():
    image = cv2.imread(r'Homework\Image Manipulation Challenge\example.jpg')

    print(Fore.YELLOW + "-----------------------------------------")
    print(Fore.YELLOW + "        Image Manipulation Ground        ")
    print(Fore.YELLOW + "-----------------------------------------")
    print("")

    print(Fore.LIGHTMAGENTA_EX + "Welcome to Image Manipulation Ground")
    print(Fore.LIGHTMAGENTA_EX + "Select one of the options below:")
    print("")

    print(Fore.LIGHTMAGENTA_EX + "1. Rotate")
    print(Fore.LIGHTMAGENTA_EX + "2. Brightness")
    print(Fore.LIGHTMAGENTA_EX + "3. Crop")
    print(Fore.LIGHTMAGENTA_EX + "4. Resize")
    print("")

    try:
        option_input = input(Fore.CYAN + "Pick any of these (number): ")

        if option_input == "1":
            angle = float(input(Fore.CYAN + "Angle Rotation (Degrees): "))
            cv2.imshow("Rotated Image", image_rotation(image, angle))
        elif option_input == "2":
            brightness_multiplier = float(input(Fore.CYAN + "Brightness multiplier: "))
            cv2.imshow("Brightened Image", brightness(image, brightness_multiplier))
        elif option_input == "3":
            position = input(Fore.CYAN + "Enter your positions (x1||x2||y1||y2): ")
            splitted_positions = position.split("||")
            if len(splitted_positions) != 4:
                raise Exception
            else:
                (x1, x2, y1, y2) = list(map(int, splitted_positions))
                cv2.imshow("Cropped Image", cropping(image, x1, y1, x2, y2))
        elif option_input == "4":
            resize_inputs = input(Fore.CYAN + "New size for your image (width||height): ")
            splitted_resize_input = resize_inputs.split("||")
            if len(splitted_resize_input) != 2:
                raise Exception
            else:
                

    except:
        print(Fore.RED + "!! Invalid Input, please try again !!")

run()
