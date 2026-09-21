import cv2
import matplotlib.pyplot as plt
import numpy as np


# Read grayscale image
img = cv2.imread("nature.jpeg", 0)

# Quantization levels
levels = [256, 128, 64, 32, 16, 8, 4, 2]

# Create figure
plt.figure(figsize=(15, 8))

# Apply quantization
for index, level in enumerate(levels):
	if level == 256:
		quantized = img
	else:
		quantized = (
			(img * (level - 1) / 255).round() * 255 / (level - 1)
		).astype(np.uint8)

	# Display quantized image
	plt.subplot(3, 3, index + 1)
	plt.imshow(quantized, cmap="gray")
	plt.title(f"{level} Levels")
	plt.axis("off")

plt.tight_layout()
plt.show()

# Save 16-level image
quantized_16 = ((img * 15 / 255).round() * 255 / 15).astype(np.uint8)
cv2.imwrite("quantized_16_levels.jpg", quantized_16)