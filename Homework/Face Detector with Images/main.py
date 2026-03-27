from colorama import init, Fore
import cv2

init(autoreset=True)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def camera_face_detection():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print(Fore.LIGHTRED_EX + "Error: Could not open camera.")
        exit()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture images.")
            break
        func = detection_method(frame)
        cv2.imshow('Face detection with Camera - Press q to Exit', func)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def image_face_detection():
    raw_image = cv2.imread(r'Homework\Face Detector with Images\example.jpg')
    image = cv2.resize(raw_image, (1000, 667))
    func = detection_method(image)
    while True:
        cv2.imshow('Face detection with Camera - Press q to Exit', func)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def detection_method(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    return frame

def intro_prompt():
    print(Fore.CYAN + 'Do you want to use camera or image to detect face?')
    print(Fore.CYAN + '1. Camera')
    print(Fore.CYAN + '2. Image')
    print(Fore.CYAN + 'Type only the numbers')

    face_detection_choice = input(Fore.GREEN + ">> ")

    if face_detection_choice.strip() == "1": camera_face_detection()
    elif face_detection_choice.strip() == "2": image_face_detection()
    else:
        print(Fore.LIGHTRED_EX + "Not a correct input. Please try again.")
        print("\n")
        intro_prompt()

if __name__ == "__main__": intro_prompt()