import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import cv2


nadia = cv2.imread('CV images/Nadia_Murad.jpg',0)
denis = cv2.imread('CV images/Denis_Mukwege.jpg')
solvay = cv2.imread('CV images/solvay_conference.jpg')

plt.imshow(solvay,cmap='gray')

face_cascade = cv2.CascadeClassifier('CV xml/frontalFace10/haarcascade_frontalface_default.xml') # used to uploads necessary xml file

def detect_img(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img) #returns boundary rectangle for detected images
    
    for(x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
        
    return face_img    
    
result = detect_img(denis)
plt.imshow(result1,cmap = 'gray')

result1 = detect_img(solvay)
plt.imshow(result1,cmap = 'gray')



def adj_detect_img(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor = 1.2 ,minNeighbors = 5) #more clears to the image such as not finding the necessary faces in this
    
    for(x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
        
    return face_img 


result = adj_detect_img(solvay)
eye_cascade = cv2.CascadeClassifier('CV xml/Eyes45x11/parojosG.xml')

def detect_eyes(img):
    face_img = img.copy()
    eyes_rects = eye_cascade.detectMultiScale(face_img)
    
    for(x,y,w,h) in eyes_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
        
    return face_img    
result = detect_eyes(nadia)
plt.imshow(result,cmap = 'gray')


cap = cv2.VideoCapture(0)

while True:
    
    ret,frame = cap.read(0)
    frame = detect_img(frame)
    cv2.imshow('Video Frame Detect',frame)
    
    k = cv2.waitKey(2)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
    