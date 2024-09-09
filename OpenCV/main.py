import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv2.VideoCapture(0)

def main():
    while True:
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)
        hands, img = detector.findHands(frame)
        if hands:
            lmList = hands[0]
            fingerUp = detector.fingersUp(lmList)

            print(fingerUp)
            cnt.led(fingerUp)
            jari = sum(fingerUp)
            cv2.putText(frame, "jari "+str(jari), (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        else:
            cnt.led([0, 0, 0, 0, 0])
        c = cv2.resize(frame, (1280, 720))
        cv2.imshow("frame", c)
        k = cv2.waitKey(1)
        if k == ord("k"):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()