"""Hand Tracking uses 2 different modules at backend: 1.Palm Detection  2. Hand Landmark
1 ----->  palm Detection works on complete image and outputs the cropped image of the palm
2 ----->  Then
"""

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
while True:
    success, img = cap.read()


    cv2.imshow("Image", img)
    cv2.waitKey(1)