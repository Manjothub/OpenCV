import tkinter as Tk
from tkinter import *
import numpy as np
import cv2

win=Tk()
#function coding starts here
def grayimg():
    video_c=cv2.VideoCapture(0) 
    while True:
        ret, frame = video_c.read()
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
        if ret == True:
            cv2.imshow('Frame',frame)
            
            if cv2.waitKey(1) == ord('q'):
                break
    video_c.release()
    cv2.destroyAllWindows()

def edge():
    video_c=cv2.VideoCapture(0) 
    while True:
        ret, frame = video_c.read()
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
        frame=cv2.Canny(frame,100,100)
        if ret == True:
            cv2.imshow('Frame',frame)
            
            if cv2.waitKey(1) == ord('q'):
                break
    video_c.release()
    cv2.destroyAllWindows()
    
def save():
    video_c=cv2.VideoCapture(0) 
    
    while True:
        ret, frame = video_c.read()
        
        if ret == True:
            cv2.imshow('Frame',frame)
            
            cv2.imwrite(f"test.jpg",frame)
            
            
            if cv2.waitKey(1) == ord('q'):
                break
    video_c.release()
    cv2.destroyAllWindows()
    pass

text= Label(win,text = "Camera").place(x = 40,y = 60)  
b1=Button(win,text='Gray',command=grayimg).place(x=20,y=80)
b2=Button(win,text='Edge',command=edge).place(x=60,y=80)
b3=Button(win,text='Save',command=save).place(x=100,y=80)
win.mainloop()