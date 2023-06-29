import cv2
import time
import HandTrackingModule as htm

wCam, hCam = 720,670
pTime=0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
totalFingers =0


detector = htm.handDetector(detection_confidence = 0.8)
tipID = [4,8,12,16,20]

while True:
    succcess, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) !=0:
        fingers =[]

        #Thumb

        if lmlist[tipID[0]][1] > lmlist[tipID[3] - 1][1]:
            #Right Hand
            if lmlist[tipID[0]][1] > lmlist[tipID[0] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            #Left Hand
            if lmlist[tipID[0]][1] < lmlist[tipID[0] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        #4 Fingers
        for id in range(1,5):
            if lmlist[tipID[id]][2]<lmlist[tipID[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)

        cv2.rectangle(img, (20, 300), (120, 420), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(totalFingers)}', (40, 390), cv2.FONT_HERSHEY_PLAIN, 6, (0, 100, 0), 10)

    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img, f'FPS: {int(fps)}', (500,50), cv2.FONT_HERSHEY_PLAIN, 2, (0,100,0), 4)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
