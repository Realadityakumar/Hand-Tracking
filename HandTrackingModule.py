import cv2 as cv
import mediapipe as mp
import time

class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode,
            self.maxHands,
            self.detectionCon,
            self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self,img,handNo=0,draw=True):
        #whhy is it returing both hands result even thogh handno is set to return for the first onlyy
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        # print(id, cx, cy)
                        lmList.append([id,cx,cy])
                        if draw:
                            cv.circle(img, (cx, cy), 10, (255, 0, 255), cv.FILLED)
        return lmList





def main():
    cap = cv.VideoCapture(0)
    pTime = 0

    detector = HandDetector()

    while True:
        success, img = cap.read()
        if not success:
            break

        img = detector.findHands(img)
        lmList = dectector.findPosition(img)

        print(lmList)
        # cTime = time.time()
        # fps = 1 / (cTime - pTime) if cTime != pTime else 0
        # pTime = cTime

        # cv.putText(img, f'FPS: {int(fps)}', (10, 70),
        #            cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

        cv.imshow("Camera live feed", img)
        if cv.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
