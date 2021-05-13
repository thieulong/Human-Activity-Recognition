import numpy as np
import cv2

cap = cv2.VideoCapture("test_sample_videos/sample1.mp4")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("output_video/frame2.png", frame)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()