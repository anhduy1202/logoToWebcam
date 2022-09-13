import cv2

logo = cv2.imread("logo.jpg")
logo = cv2.resize(logo, (10, 10))
gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
print(gray)
# Less than 100 ->  0, More than 100 -> 255
_, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
print(f"Mask: {mask}")
cv2.imshow("Mask", mask)
cv2.waitKey(0)