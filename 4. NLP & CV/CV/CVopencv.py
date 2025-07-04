import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("Image.jpg")  # BGR format

# Display using OpenCV
cv2.imshow("My Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize
resized = cv2.resize(img, (300, 200))

# Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Resized", resized)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw rectangle (x1, y1) to (x2, y2)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 1)

# Draw circle
cv2.circle(img, (150, 150), 40, (255, 0, 0), -1)

# Put text
cv2.putText(img, 'Hello!', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

cv2.imshow("Shapes and Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

