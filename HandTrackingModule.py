import cv2 as cv
import mediapipe as mp
import os

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionConfidence=0.5, trackConfidence=0.5):
        print("Starting initialisation...")
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        print("Initialised hands Detector")

    def findhands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mphands.HAND_CONNECTIONS)
        return img
  
    def findPosition (self, img, hand_no=0, draw=True):
        lmList = []

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy= int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 20, (255,0,255), -1)
        
        return lmList

def main():
     cap = cv.VideoCapture(0)
     detector = handDetector()

     while True:
        success, img = cap.read()
        img = detector.findhands(img)
        lm_list = detector.findPosition(img)
        print(lm_list)
        cv.imshow("Camera", img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()