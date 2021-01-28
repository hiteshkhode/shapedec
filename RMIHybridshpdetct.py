import numpy as np
import cv2
img = cv2.imread('allhollow.jpg')
nimg = img.copy()
k = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGry = cv2.GaussianBlur(k, (3, 3), 0)
ret , thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)

contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

inner = ''
innercou = []
for i in range(len(hierarchy[0])):
    if (hierarchy[0][i][3])%2 != 0:
        innercou.append(contours[i])

shapes = []
for contour in innercou:
    approx = cv2.approxPolyDP(contour, 0.015* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 0
    if len(approx) == 3:
        cv2.putText( nimg, "triangle"+inner, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
        shapes.append("triangle"+inner)
        
    elif len(approx) == 4 :
        x, y , w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(nimg, "square"+inner, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            shapes.append("square"+inner)
        else:
            cv2.putText(nimg, "rectangle"+inner, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            shapes.append("rectangle"+inner)

    elif len(approx) == 5 :
        cv2.putText(nimg, "pentagon"+inner, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes.append("pentagon"+inner)

    elif len(approx) == 10 :
        cv2.putText(nimg, "star"+inner, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes.append("star"+inner)
    elif len(approx) == 6 :
        cv2.putText(nimg, "hexagon"+inner, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes.append("hexagon"+inner)
    else:
        cv2.putText(nimg, "circle"+inner , (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        shapes.append("circle"+inner)

cv2.imshow('shapes', nimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(shapes)