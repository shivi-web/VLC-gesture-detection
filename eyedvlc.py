import time
import cv2
import vlc
v=cv2.VideoCapture(0)
path=r'C:\Users\KIIT\Desktop\python\project\vlc using eyedetection\\'
a=['I_cant_get_enough.mp3','Watchme.mp3','Black_Magic.mp3']
x=1
cp=path+a[x]+'.mp3'
m=vlc.MediaPlayer(cp)
fd=cv2.CascadeClassifier(r'C:\Users\KIIT\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
eye=cv2.CascadeClassifier(r'C:\Users\KIIT\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\cv2\data\haarcascade_eye.xml')
leye=cv2.CascadeClassifier(r'C:\Users\KIIT\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\cv2\data\haarcascade_lefteye_2splits.xml')
reye=cv2.CascadeClassifier(r'C:\Users\KIIT\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\cv2\data\haarcascade_righteye_2splits.xml')
time.sleep(1)
m.play()
flag=1
vol=100
m.audio_set_volume(vol)
while(1):
    r,i=v.read()
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(gray)
    f=eye.detectMultiScale(gray)
    lf=leye.detectMultiScale(gray)
    rf=reye.detectMultiScale(gray)
    if(len(f)==2):
        m.play()
        print("current song coz 2 eyes detected")
        flag=0
    elif(len(f)==1 and flag==0 ):
        if(len(lf)==1):
            m.stop()
            print('left eye detetcted .')
            flag=1
            if(x<2):
                cp=path+a[x+1]+'.mp3'
                m=vlc.MediaPlayer(cp)
                m.play()
                flag=0
            else:
                cp=path+a[0]+'.mp3'
                m=vlc.MediaPlayer(cp)
                m.play()
                flag=0
        elif(len(rf)==1):
            m.stop()
            print('right eye detetcted .')
            flag=1
            if(x>0):
                cp=path+a[x-1]+'.mp3'
                m=vlc.MediaPlayer(cp)
                m.play()
                flag=0
            else:
                cp=path+a[2]+'.mp3'
                m=vlc.MediaPlayer(cp)
                m.play()
                flag=0
    cv2.imshow('face',i)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break
cv2.destroyAllWindows()
v.release()


