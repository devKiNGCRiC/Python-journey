import cv2


# 1. Load images in grayscale
scene = cv2.imread("apples.jpeg", 0)
template = cv2.imread("apple.jpeg", 0)

# Resize template if it is larger than the scene
sh, sw = scene.shape[:2]
th, tw = template.shape[:2]

if th > sh or tw > sw:
    # Resize template to 30% of its original size
    template = cv2.resize(template, (0, 0), fx=0.3, fy=0.3)

# Get new dimensions
h, w = template.shape

# 2. Match template against the scene
result = cv2.matchTemplate(scene, template, cv2.TM_CCOEFF_NORMED)

# 3. Get best match location
_, _, _, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

# 4. Draw bounding box and display
cv2.rectangle(scene, top_left, bottom_right, (255, 255, 255), 3)

cv2.imshow("Recognized Object", scene)
cv2.waitKey(0)
cv2.destroyAllWindows()