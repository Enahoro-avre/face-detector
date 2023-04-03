import cv2
from random import randrange
#Load some pretrained data on face frontal from open cv (harr cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Choose an image to detect faces
# img = cv2.imread('img.jpg')

#capture video
webcam = cv2.VideoCapture(0)
while True:

    #read the current frame
    successful_frame_read , frame = webcam.read()

    # covert to grayscale
    grayscaled_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    # Dectect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x , y , w ,h ) in face_coordinates:
      cv2.rectangle(frame , ( x , y ), (x+w , y+h) , ( 0 , 255 , 0 ), 4 )

    cv2.imshow('Face Detector' , frame)
    key= cv2.waitKey(1) # could use any parameter "key" , "me" , etc...

    # if Q is pressed
    if key == 81 or key == 113:
      break

webcam.release()






















"""""
#Must covert to greyscale
grayscaled_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

#Dectect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Draw rectangle around faces
# cv2.rectangle(img , (507 , 254), (507 + 282 , 254 + 282), (0 , 255 , 0) , 2)
for (x , y , w ,h ) in face_coordinates:
    cv2.rectangle(img , ( x , y ), (x+w , y+h) , (0 , 255,0 ,), 2 )
# for (x , y , w ,h ) in face_coordinates:
#     cv2.rectangle(img , ( x , y ), (x+w , y+h) , (randrange(256) , randrange(256) , randrange(256) ), 5 )


# # print(face_coordinates)


# Dispaly images
cv2.imshow('Clever programmer face detector' , img)
cv2.waitKey()
"""""

print('Code completed')