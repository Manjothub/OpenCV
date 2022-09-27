import cv2
    
video_c=cv2.VideoCapture(0) 
while True:
        
    ret, frame = video_c.read()
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    if ret == True:
        cv2.imshow('Frame',frame)
    

    if cv2.waitKey(1) == ord('q'):
        break


 
# Release the video capture object

video_c.release()
cv2.destroyAllWindows()
