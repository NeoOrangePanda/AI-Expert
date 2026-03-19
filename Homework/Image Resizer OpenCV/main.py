import cv2
import sys
from colorama import init, Fore
from pathlib import Path

init(autoreset=True)

image_ext = [".png", ".jpg", ".jpeg", ".bmp", ".webp"]

path = Path('Homework/Image Resizer OpenCV')
image_list = [f.name for f in path.iterdir() if f.is_file() and f.suffix.lower() in image_ext]
serialized_image_list = [(x, y) for x, y in enumerate(image_list)]

if len(image_list) == 0:
    sys.exit(Fore.RED + "No image file has been found")

if len(image_list) > 1:
    print(Fore.CYAN + "Hey! Here is some listed images found on your folder -")

    for x, y in serialized_image_list:
        print(Fore.YELLOW + f"{x}. {y}")

    image = cv2.imread(input(Fore.LIGHTMAGENTA_EX + "Which one you want to pick?"))