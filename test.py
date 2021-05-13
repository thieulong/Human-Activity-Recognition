import numpy as np
import cv2
import os, shutil
import PoseModule as pm

samples_path = "test_sample_videos"

video = "video2.mp4"
cap = cv2.VideoCapture(samples_path + "/" + video)

cur_angle = 0
prev_angle = 90
degree_up = False
count = 0
frame_count = 0

detector = pm.poseDetector()

while True:
    # Capture frame-by-frame
    success, frame = cap.read()
    if not success:
        break

    frame = detector.findPose(frame, draw=False)
    lmList = detector.findPosition(frame, draw=False)
    if lmList:
        # Our operations on the frame come here
        cur_angle = detector.findAngle(frame, 11, 13, 15, draw=True)
        if frame_count % 5 == 0:
            if degree_up:
                if (cur_angle < prev_angle) and (90 < cur_angle < 190):
                    count += 0.5
                    degree_up = False
            else:
                if (cur_angle > prev_angle) and (0 < cur_angle < 140) :
                    count += 0.5
                    degree_up = True
            prev_angle = cur_angle

        frame_count += 1

    cv2.putText(frame, str(int(count)), (70, 600), cv2.FONT_HERSHEY_PLAIN, 15, (0, 0, 255), 2)



    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()