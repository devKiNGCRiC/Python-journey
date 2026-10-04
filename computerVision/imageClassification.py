import cv2
import numpy as np


# 1. Define broad reference classes with BGR target values
class_colors = {
    "Apple": np.array([50, 150, 200]),  # Yellow/Golden/Red Apple mixture
    "Green Apple": np.array([50, 180, 50]),  # Bright Green Apple
    "Blueberry": np.array([180, 50, 30]),  # Blue/Dark Purple
}

# 2. Read image
img = cv2.imread("apples.jpeg")

# 3. Calculate average BGR color of the image
mean_color = np.array(cv2.mean(img)[:3])

# 4. Find the closest matching class
best_match = None
min_distance = float("inf")

for class_name, ref_color in class_colors.items():
    distance = np.linalg.norm(mean_color - ref_color)
    if distance < min_distance:
        min_distance = distance
        best_match = class_name

# 5. Display the result
cv2.putText(
    img,
    f"Class: {best_match}",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2,
)

cv2.imshow("Image Classification", img)
cv2.waitKey(0)
cv2.destroyAllWindows()