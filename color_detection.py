import cv2
import numpy as np
def empty(a):
    pass

framewidth=380
frameheight =380
cap =cv2.VideoCapture(0)
#cap =cv2.VideoCapture("3.mp4")
cap.set(3,frameheight)
cap.set(4,frameheight)


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",380,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    success, img = cap.read()
    img =cv2.resize(img, (framewidth,frameheight))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min =cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    hstack =np.hstack([img,imgResult,mask])

    cv2.imshow("hstack",hstack)
    #cv2.waitKey(0)
    #cv2.imshow("Original",img)
    #cv2.imshow("HSV",imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", imgResult)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
