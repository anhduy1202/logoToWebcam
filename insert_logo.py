import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

logo = cv2.imread("logo.jpg")
logo = cv2.resize(logo, (100, 100))
gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)


while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    roi = frame[-100-10:-10, -100-10:-10]
    # Mask it black
    roi[np.where(mask)] = 0
    # Add logo to that mask area
    roi += logo

    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break
