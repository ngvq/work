import cv2
import os
import numpy as np

detector = cv2.CascadeClassifier(
    './haarcascades/haarcascade_frontalface_default.xml')


# def get_face(input_path, output_path):
# print(input_path)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 5)
count = 0
while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect and save the faces
    faces = detector.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        if h >= 40 and w >= 40:
            count += 1
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
            # face = img[y:y+h,x:x+w]  # slice the face from the image
            # face = cv2.resize(
            #     face, (40, 40),  interpolation=cv2.INTER_AREA)
            # cv2.imwrite(os.path.join(output_path, str(
            #     count) + '.jpg'), face)  # save the image
    # Display
    cv2.imshow('Video', img)

    # Stop if escape key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()

# if __name__ == '__main__':
#     get_face(input_path='C:/Users/Admin/Desktop/Work/student-concentration-determiner/Video/f0 (2).mp4',
#              output_path= 'C:/Users/Admin/Desktop/Work/student-concentration-determiner/Output/')
    # print(os.getcwd().replace('\\', '/').replace('/detecting',""))