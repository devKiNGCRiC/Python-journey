import cv2
import numpy as np
import matplotlib.pyplot as plt


# Read image
img = cv2.imread("nature.jpeg")

# Translation
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
translated = cv2.warpAffine(
	img,
	translation_matrix,
	(img.shape[1], img.shape[0]),
)

# Rotation
rotation_matrix = cv2.getRotationMatrix2D(
	(img.shape[1] // 2, img.shape[0] // 2),
	45,
	1,
)
rotated = cv2.warpAffine(
	img,
	rotation_matrix,
	(img.shape[1], img.shape[0]),
)

# Scaling
scaled = cv2.resize(img, None, fx=1.5, fy=1.5)

# Flipping
flipped = cv2.flip(img, 1)

# Display images
images = [img, translated, rotated, scaled, flipped]
titles = ["Original", "Translate", "Rotate", "Scale", "Flip"]

for index in range(5):
	plt.subplot(2, 3, index + 1)
	plt.imshow(cv2.cvtColor(images[index], cv2.COLOR_BGR2RGB))
	plt.title(titles[index])
	plt.axis("off")

plt.show()