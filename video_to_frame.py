import numpy as np
import cv2
import os, shutil
import PoseModule as pm


# Delete all file in directory (if needed)
def delete_all_file(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

path = 'test_output_frames'
delete_all_file(path)

samples_path = "test_sample_videos"

total = 1
frame_index = 1
frame_skip_rate = 10

for video in os.listdir(samples_path):
    cap = cv2.VideoCapture(samples_path + "/" + video)

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
            if total % frame_skip_rate == 0:
                cv2.imwrite("test_output_frames/frame" + str(frame_index) + ".png", frame)
                frame_index += 1
            total += 1

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()