import cv2

logo = cv2.imread("logo.jpg")
logo = cv2.resize(logo, (10, 10))

gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
roi = gray[3:6, 3:6]
roi[:, :] = gray[0:3, 0:3]
print(gray)
print(f"ROI: {roi}")
cv2.imshow("ROI", roi)
cv2.waitKey(0)