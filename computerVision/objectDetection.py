import cv2
import numpy as np


img = cv2.imread("nature.jpeg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define color ranges in HSV (e.g., yellow to green)
lower_bound = np.array([15, 50, 50])  # Adjust HSV limits for your target fruit
upper_bound = np.array([85, 255, 255])

# Mask colors and remove noise
mask = cv2.inRange(hsv, lower_bound, upper_bound)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Find contours on clean mask
contours, _ = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE,
)

for contour in contours:
    if cv2.contourArea(contour) > 500:  # Filter out small noise
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("HSV Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()