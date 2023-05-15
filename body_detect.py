import cv2

vid = cv2.imread("C:/Users/Lenovo/Downloads/Project 106/PRO-106-ProjectTemplate-main/walking.avi")

gray= cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('C:/Users/Lenovo/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_fullbody.xml')

faces = face_cascade.detectMultiScale(gray,1.1,5)
print(len(faces))

for (x,y,w,h) in faces:
       cv2.rectangle(vid,(x,y),(x+w,y+h),(255,0,0),2)
             
cv2.imshow('vid',vid)
cv2.waitKey(0)



