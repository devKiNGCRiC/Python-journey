import cv2
import numpy as np
import matplotlib.pyplot as plt


# Read image
img = cv2.imread("nature.jpeg")

# Original points
original_points = np.float32(
	[[50, 50], [300, 50], [50, 300], [300, 300]]
)

# Different projection points
projection_points = [
	[[0, 0], [300, 0], [100, 300], [300, 300]],
	[[50, 0], [300, 50], [0, 300], [350, 250]],
	[[0, 50], [250, 0], [100, 300], [350, 350]],
	[[50, 50], [250, 0], [0, 300], [300, 350]],
	[[0, 100], [300, 0], [50, 350], [350, 250]],
]

# Display five projections
for index in range(5):
	destination_points = np.float32(projection_points[index])
	perspective_matrix = cv2.getPerspectiveTransform(
		original_points,
		destination_points,
	)
	output = cv2.warpPerspective(img, perspective_matrix, (400, 400))

	plt.subplot(2, 3, index + 1)
	plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
	plt.title("Projection " + str(index + 1))
	plt.axis("off")

plt.tight_layout()
plt.show()