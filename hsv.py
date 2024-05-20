import cv2

bgr_img = cv2.imread('image0.jpeg')

hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(hsv_img, cv2.COLOR_BGR2GRAY)
blur_gray = cv2.GaussianBlur(img_gray,(5, 5),0)
edges = cv2.Canny(blur_gray, 50, 150)

cv2.imshow('HSV image', hsv_img)
cv2.waitKey(0)
cv2.imshow('Grey image', img_gray)
cv2.waitKey(0)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
