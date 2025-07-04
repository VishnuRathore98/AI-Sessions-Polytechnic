import cv2
img = cv2.imread('Image.jpg')

#Gaussian Blur
blurred = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('Gaussian Blur', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Median Blur
median = cv2.medianBlur(img, 5)  #5 is kernal size
cv2.imshow('Median Blur', median)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Detect Edges using Canny:
edges = cv2.Canny(img, 100, 200)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Thresholding (Black & White Conversion)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Image', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Color Space Conversion (BGR to HSV)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()