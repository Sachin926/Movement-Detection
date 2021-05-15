import cv2 as cv
import numpy as np
import time
cap = cv.VideoCapture(0)
_, bgImage = cap.read()
time.sleep(5)
_, bgImage = cap.read()


bgImage = cv.cvtColor(src = bgImage, code = cv.COLOR_BGR2GRAY)
bgImage = cv.GaussianBlur(src = bgImage, ksize = (5, 5), sigmaX = 0)
cv.threshold(src = bgImage, thresh = 20, maxval = 255, type = cv.THRESH_BINARY)

cv.imshow("BackGround", mat = bgImage)
count = 0

while (1):
	_, frame = cap.read()
	if (frame is None):
		break
	else:
		cv.imshow("Footage", mat = frame)
		frame = cv.GaussianBlur(src = frame, ksize = (5, 5), sigmaX = 0)
		frame = cv.cvtColor(src = frame, code = cv.COLOR_BGR2GRAY)
		cv.threshold(src = frame, thresh = 20, maxval = 255, type = cv.THRESH_BINARY)
		count = count + 1
		diff = cv.absdiff(src1 = frame, src2 = bgImage)
		cv.imshow("Difference", mat = diff)
		if (count == 1):
			bgImage = frame
			count = 0
		k = cv.waitKey(1)
	if (k == 13):
		break
cap.release()
cv.destroyAllWindows()
