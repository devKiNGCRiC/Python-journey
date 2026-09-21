import cv2
import matplotlib.pyplot as plt


# Read grayscale image
img = cv2.imread("nature.jpeg", 0)

# Canny edge detection
canny = cv2.Canny(img, 100, 200)

# LoG (Laplacian of Gaussian)
log = cv2.Laplacian(
	cv2.GaussianBlur(img, (5, 5), 0),
	cv2.CV_64F,
)

# DoG (Difference of Gaussian)
dog = cv2.absdiff(
	cv2.GaussianBlur(img, (3, 3), 0),
	cv2.GaussianBlur(img, (9, 9), 0),
)

# Display all results
results = [
	(img, "Original"),
	(canny, "Canny"),
	(log, "LoG"),
	(dog, "DoG"),
]

for index, (image, title) in enumerate(results, 1):
	plt.subplot(1, 4, index)
	plt.imshow(image, cmap="gray")
	plt.title(title)
	plt.axis("off")

plt.show()