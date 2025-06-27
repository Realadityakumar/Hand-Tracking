import HandTrackingModule as htm
import cv2 as cv

def main():
    cap = cv.VideoCapture(0)
    detector = htm.handDetector()

    while True:
        success,img = cap.read()
        img = detector.findhands(img,False)
        lm_List = detector.findPosition(img,draw=False)
        for id,cx,cy in lm_List:
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

        cv.imshow("Camera",img)
        cv.waitKey(1)

main()