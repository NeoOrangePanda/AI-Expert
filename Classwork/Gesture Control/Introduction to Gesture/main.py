import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

canvas = None
prev_x, prev_y = None, None

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Cannot read frame")
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(max_contour) > 500:
            x, y, w, h = cv2.boundingRect(max_contour)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

            center_x = x + w // 2
            center_y = y + h // 2

            cv2.circle(frame, (center_x, center_y), 5, (0,0,255), -1)

            if prev_x is not None and prev_y is not None:
                cv2.line(canvas, (prev_x, prev_y), (center_x, center_y), (255, 0, 255), 5)

            prev_x, prev_y = center_x, center_y

    else:
        prev_x, prev_y = None, None

    output = cv2.add(frame, canvas)

    cv2.imshow("Air Doodle Cam", output)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
    elif key == ord("c"):
        canvas[:] = 0

cap.release()
cv2.destroyAllWindows()