import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle

cap=cv2.VideoCapture(0)
def gettestface():
    c=0

    facecascade=cv2.CascadeClassifier('face.xml')
    
    while c<1:
        ret,img=cap.read()
        r=img
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=facecascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            if(y):
                reto=img[y:y+h,x:x+w]
                c=1

    if c==1:
        return [img,reto,x,y,w,h]




def test(clf):
        
    while True: 
        img,a,x,y,w,h=gettestface()
        gray=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
        b=cv2.resize(gray,(350,350))
        flat=b.flatten()
        flat=flat.reshape(1,122500)
        ans=clf.predict(flat)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        print(x,y,w,h)
        print("its : ",ans[0])
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,ans[0],(x,y+2*h),font,4,(255,255,255),2,cv2.LINE_AA)
        cv2.namedWindow('img')
        cv2.moveWindow('img', 40,30)
        cv2.imshow('img',img)
        k=cv2.waitKey(30)
        if k==27:
            break  
    cap.release()      
    cv2.destroyAllWindows()

clf=pickle.load(open("model",'rb'))
test(clf)




