import cv2

# Read an image
logo = cv2.imread("logo.jpg")
cv2.imshow("Original Logo", logo)
print(logo.shape)

# Lossy compression
logo = cv2.resize(logo, (10, 10))
logo_default = cv2.resize(logo, (960, 960))

# Show the image
cv2.imshow("Default Logo", logo_default)

# Cubic image
logo_cubic = cv2.resize(logo, (960, 960), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Cubic Logo", logo_cubic)

cv2.waitKey(0)

