import cv2
import time
import os
import numpy as np

newpath = r'C:\Users\Win10\Desktop\files\python projects\WebCamera\WebCamera\Records' # Records Folder Directory
if not os.path.isdir(newpath):
    os.makedirs(newpath)

q = input("Do You Want To Record YouSelf? (y/n): ")

if q == 'y':

    t = input("\nHow Much Time Do You Want To Record? ")

    i = input("\nWhat Camera Do You Use? ")

    print(f"\nStarting With Camera {i}")

    if int(i) == 0:
        cap = cv2.VideoCapture(int(i))
   
    elif int(i) > 0:
        cap = cv2.VideoCapture(int(i)-1)

    else:
        print(f"\nCannot Open Camera {i} Becase It Is Under The 0\n")
        exit(0)

    prev_frame_time = 0
    new_frame_time = 0

    seconds_to_go_for = int(t)
    current_time = int(time.time())

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out = cv2.VideoWriter(f"Records\Record [Date {time.strftime('%d-%m-%Y', time.localtime())}, Time {time.strftime('%H-%M-%S', time.localtime())}].avi", fourcc, 20.0, (640, 480))

elif q == 'n':
    print('\n')
    exit(0)

else:
    print('\n')
    exit(0)

while True:
    ret, frame = cap.read()
    
    out.write(frame)

    time_now = int(time.time())
    if time_now >= current_time + seconds_to_go_for:
        break

    gray = frame

    font = cv2.FONT_HERSHEY_SIMPLEX

    new_frame_time = time.time()

    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time

    fps = int(fps)
    fps = str(fps)

    cv2.putText(gray, f"FPS: {fps}", (7, 70), font, 1.2, (100, 255, 0), 3, cv2.LINE_AA)
    cv2.putText(gray, f"Timer: {time_now - current_time}", (7, 455), font, 1.2, (100, 255, 0), 3, cv2.LINE_AA)

    grayWindow = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Normal Camera", gray)
    cv2.imshow("Camera In Gray", grayWindow)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print('\n')
cap.release()
cv2.destroyAllWindows()