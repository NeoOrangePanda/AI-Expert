import cv2
import numpy as np

# blank white canvas
img = np.ones((600, 800, 3), dtype=np.uint8) * 255

drawing = False
last_x, last_y = -1, -1

def draw(event, x, y, flags, param):
    global drawing, last_x, last_y

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_x, last_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img, (last_x, last_y), (x, y), (0, 0, 0), 3)
            last_x, last_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow("Doodle")
cv2.setMouseCallback("Doodle", draw)

while True:
    cv2.imshow("Doodle", img)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:   # ESC = quit
        break
    elif key == ord("c"):   # press C = clear
        img[:] = 255

cv2.destroyAllWindows()