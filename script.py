import cv2
from datetime import time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
first_frame = None

status_list = []
times = [0, 0]

while True:
    check, frame = video.read()
    status = 0
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21,21), 0)

    if first_frame is None:
        first_frame = gray_frame
        continue
        
    delta_frame = cv2.absdiff(first_frame, gray_frame)
    thresh_frame = cv2.treshhold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threhs_frame = cv2.dilate(thresh_frame, none, iteration = 2
    
    (cnts, _) = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                              
    for contour in cnts:
        if cv2.contourArea(contour) >= 1000:
            status += 1
            (x,y,w,h) = cv2.boundRect(contour)
            cv2.rectangle(frame, (x,y), (xw, yh), (0,255,0), 3)
                              
    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0: times.apend(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1: times.apend(datetime.now())

                              
    cv2.imshow('Capturing...', gray_frame)
    key = cv2.waitKey(1)
    if key == ord('q'): 
        if status == 1:
            times.append(datetime.now())
        break

video.release()
cv2.destroyAllWindows()
