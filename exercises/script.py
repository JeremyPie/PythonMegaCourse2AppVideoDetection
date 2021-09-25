import cv2, time
import pandas as pd
from datetime import datetime

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
first_frame, status_list, times, count = None, [0, 0], [], 0
df = pd.DataFrame(columns = ['Start', 'End'])

while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21,21), 0)

    if count > 15:
        if first_frame is None:
            first_frame = gray_frame
            continue
    else:
        count += 1
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threhs_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    (cnts, _) = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) >= 1000:
            status = 1
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)

    if status_list[-1] == 1 and status_list[-2] == 0: times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1: times.append(datetime.now())

    #cv2.imshow('Gray Frame..', gray_frame)
    #cv2.imshow('Delta Frame...', delta_frame)
    #cv2.imshow('Thresh Hold Frame...', threhs_frame)
    cv2.imshow('Frame...', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

for i in range(0, len(times) - 1, 2):
    df = df.append({'Start':times[i], 'End':times[i+1]}, ignore_index = True)
df.to_csv('Times.csv')

video.release()
cv2.destroyAllWindows()
print(times)
