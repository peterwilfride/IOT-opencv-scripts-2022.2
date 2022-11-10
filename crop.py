import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cropped = image[6:154, 580:744]

cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", cropped)
