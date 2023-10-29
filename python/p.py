import cv2
import mediapipe as mp
import csv


mpPose = mp.solutions.pose
pose = mpPose.Pose()

# Open the webcam (you may need to adjust the camera index)
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    
    if not ret:
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)
    height=0

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        h, w, _ = frame.shape

        # Extract the position of head and feet
        head = landmarks[mpPose.PoseLandmark.NOSE]
        left_foot = landmarks[mpPose.PoseLandmark.LEFT_ANKLE]
        right_foot = landmarks[mpPose.PoseLandmark.RIGHT_ANKLE]

        # Calculate the height based on the vertical position of head and feet
        height = abs(head.y * h - (left_foot.y * h + right_foot.y * h) / 2)

        # Display the height on the frame
        cv2.putText(frame, f'Height: {height:.2f} pixels', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow('Height Measurement', frame)
    fheight=[height/1.48]

    with open("measure.csv",'w') as csvfile:
       csvwriter=csv.writer(csvfile)
       csvwriter.writerow(fheight)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
capture.release()
cv2.destroyAllWindows()

