
import os
import cv2

detector= cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
# To capture video from existing video.   
in_path = "C:/Users/Admin/Desktop/Work/student-concentration-determiner/Video/"
vid_list = os.listdir(in_path)
for vid in vid_list:
    out_path = 'C:/Users/Admin/Desktop/Work/student-concentration-determiner/Output/' + str(vid.split('.mp4')[0])
    if not os.path.exists(out_path):
        os.makedirs(out_path)
        print(vid)
    
    cap = cv2.VideoCapture(in_path + vid)
    cap.set(cv2.CAP_PROP_FPS, 1)
    count = 0
    while True:  
        # Read the frame  
        _, img = cap.read()
    
        # Convert to grayscale  
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
            # Detect and save the faces  
        faces = detector.detectMultiScale(gray,1.1,4)  
        for (x, y, w, h) in faces:
            # if h >=  and w >= 80:
                count+=1
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
                face = img[y:y+h, x:x+w] #slice the face from the image
                # face = cv2.resize(face, (70,70),  interpolation = cv2.INTER_AREA)
                cv2.imwrite(os.path.join(out_path, str(count) + '.jpg'), face) #save the image 
        
        # Display  
        cv2.imshow('Video', img)  
    
        # Stop if escape key is pressed  

          
        # Release the VideoCapture object  
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

cv2.destroyAllWindows()
