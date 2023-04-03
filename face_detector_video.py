from tkinter import Frame
import cv2
from cv2 import VideoCapture
import numpy as np

face_classifier = 'haarcascade_frontalface_default.xml'
smile_classifier = 'haarcascade_smile.xml'
body_classifier = 'haarcascade_fullbody.xml'

# img = cv2.imread('curly_hair.jpg')
# img1 = cv2.resize(img , (500 , 500))

face_dectector = cv2.CascadeClassifier(face_classifier)
smile_dectector = cv2.CascadeClassifier(smile_classifier)
body_dectector = cv2.CascadeClassifier(body_classifier)


video = VideoCapture('richest.mp4')
while True:
    success , frame = video.read()

    grayscaled_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)


    face_coordinates = face_dectector.detectMultiScale(grayscaled_img)
    smile_coordinates = smile_dectector.detectMultiScale(grayscaled_img , scaleFactor = 1.7 , minNeighbors = 20)
    body_coordinates = body_dectector.detectMultiScale(grayscaled_img)
    
    
    for ( x , y , w , h ) in body_coordinates:

        # Draw a rectangle on th face  
        cv2.rectangle(frame , ( x , y ), (x+w , y+h) , ( 150 , 250 , 250 ), 4 )   

    for ( x , y , w , h ) in face_coordinates:
        # Draw a rectangle on th face  
        cv2.rectangle(frame , ( x , y ), (x+w , y+h) , ( 100 , 200 , 50 ), 4 )

    # for ( x , y , w , h ) in smile_coordinates:
    #       # Draw a rectangle on th face  
    #       cv2.rectangle(img1 , ( x , y ), (x+w , y+h) , ( 0 , 0 , 255 ), 4 )
    # print(img.shape)

    for ( x , y , w , h ) in smile_coordinates:
        # Draw a rectangle on th face  
            cv2.putText(frame , 'Smiling' , (x , y+h+40) , fontScale=3 , 
                fontFace=cv2.FONT_HERSHEY_PLAIN , color = (0 , 0 , 0))

    cv2.imshow('face dectector' , frame)
    key = cv2.waitKey(1)
    if key == 81 or key== 113:
        break
