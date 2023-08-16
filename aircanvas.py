import numpy as np;#pip install numpy
import os
import time
import cv2; #pip install opencv-python
from handtrackingmodule import handDetector

drawcolor=(255,0,0)

xp,yp=0,0

imgcanvas=np.zeros((720,1280,3),np.uint8)

brushThickness=15
eraserThickness=40

folderpath = 'Header'
myList =os.listdir(folderpath)
print(myList)
overlay=[]

for impath in myList:
    image=cv2.imread(f'{folderpath}/{impath}')
    overlay.append(image)

path2 = 'footer'
overlay2=[]
myList2 =os.listdir(path2)
print(myList2)

overlay2=[]

for impath in myList2:
    image2=cv2.imread(f'{path2}/{impath}')
    overlay2.append(image2)    

print(len(overlay))

header=overlay[0]
footer=overlay2[0]

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = handDetector(detectionCon=0)

while True:
    #1. import image
    success,img= cap.read()
    img=cv2.flip(img,1)
    
    #2. Find hand landmarks
    img=detector.findHands(img)
    lmlist=detector.findPosition(img,draw=False)

    if len(lmlist)!=0:
        print(lmlist)

        x1,y1=lmlist[8][1:] #tip index of middle fingers
        x2,y2=lmlist[12][1:] 


        #3. find which finger are up

        fingers=detector.fingersUp()
        print(fingers)

    #4. if selection mode 2 fingers are up
        if fingers[1] & fingers[2]:
            print("Selection Mode")
            
            xp, yp= 0,0
           

            if y1 < 125:
                if 250 < x1 < 370:
                    header= overlay[0]
                    drawcolor=(255,0,0)
                elif  530 <x1< 656:
                    header= overlay[1]
                    drawcolor=(0,255,0)
                elif  800 < x1 < 926:
                    header= overlay[2]
                    drawcolor=(0,0,255)
                elif 980 < x1 < 1280:
                    header= overlay[3]
                    drawcolor=(0,0,0)
            cv2.rectangle(img,(x1,y1-15),(x2,y2+15),drawcolor,cv2.FILLED)     

            if y1 >125 & y1<225 :
                if 175 < x1 < 260 :
                    footer =overlay2[0]   
                    brushThickness=15
                elif 590 < x1 < 690 :
                    footer =overlay2[1]
                    brushThickness=10
                elif 945 < x1 < 1039 :
                    footer=overlay2[2]
                    brushThickness=5               



    #5. if drawing mode 1 finger are up
        if fingers[1] & fingers[2]==False:
            print("Drawing Mode")
            cv2.circle(img, (x1, y1), 15, drawcolor, cv2.FILLED)
            if xp==0 & yp ==0:
                xp,yp=x1,y1

            if drawcolor ==(0,0,0):
                cv2.line(img,(xp,yp),(x1,y1),drawcolor,eraserThickness)
                cv2.line(imgcanvas,(xp,yp),(x1,y1),drawcolor,eraserThickness)


            else :    

                cv2.line(img,(xp,yp),(x1,y1),drawcolor,brushThickness)
                cv2.line(imgcanvas,(xp,yp),(x1,y1),drawcolor,brushThickness)

            xp,yp=x1,y1    
        
   
   #merging the live frame with black canvas
    imgGray = cv2.cvtColor(imgcanvas,cv2.COLOR_BGR2GRAY)
    _, imginv= cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    imginv=cv2.cvtColor(imginv,cv2.COLOR_GRAY2BGR)
    img=cv2.bitwise_and(img,imginv)
    img=cv2.bitwise_or(img,imgcanvas)
    
    
    img[0:125 ,0:1280]=header
    img[125:195, 0:1280]=footer

    cv2.imshow("air canvas",img)
    #cv2.imshow("canvas",imgcanvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()        


    





 
