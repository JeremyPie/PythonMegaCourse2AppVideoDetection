import cv2
import time

first_frame = None

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21,21), 0)

    if first_frame is None:
        first_frame = gray_frame
        continue
        
    delta_frame = cv2.absdiff(first_frame, gray_frame)
    thresh_frame = cv2.treshhold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    
    cv2.imshow('Capturing...', gray_frame)
    key = cv2.waitKey(1)
    if key == ord('q'): break

video.release()
cv2.destroyAllWindows()
