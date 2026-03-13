import cv2

image = cv2.imread(r'Classwork\OpenCV\Save & grayscale with OpenCV\Image.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(gray_image, (480, 480))

cv2.imshow('Processed Image', resized_image)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('grayscaled_image.png', resized_image)
    print("Image saved as grayscaled_image.png")

else: print('Image not saved')

cv2.destroyAllWindows()

print(f'Processed Image Dimensions: {image.shape}')