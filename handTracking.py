import cv2 as cv
import mediapipe as mp
import os

cap = cv.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
ctime = 0

while True :
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                            #this is to find img pexels, here x is co ordinate which is mulitplied width of image 
                print(id, cx,cy)
                if id == 4:
                  cv.putText(img, 'thumb', (cx, cy), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 123, 255), 2)
                if id == 8:
                  cv.putText(img, 'Index', (cx, cy), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 123, 255), 2)
                if id == 12:
                  cv.putText(img, 'Mid', (cx, cy), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 123, 255), 2)
                if id == 16:
                  cv.putText(img, 'Ring', (cx, cy), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 123, 255), 2)
                if id == 20:
                  cv.putText(img, 'Little', (cx, cy), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 123, 255), 2)

            mpDraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)

    # ctime = time.time()
    # fps = 1/(ctime-pTime)
    # pTime = ctime

    # cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)

    cv.imshow("Camera live feed", img)
    cv.waitKey(1)