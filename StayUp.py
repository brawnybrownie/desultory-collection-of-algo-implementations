import cv2
import winsound

webcam = cv2.VideoCapture(0)
cv2.namedWindow("preview")
classifier1 = cv2.CascadeClassifier("C:\opencv\data\haarcascades\haarcascade_eye.xml")
classifier2 = cv2.CascadeClassifier("C:\opencv\data\haarcascades\haarcascade_profileface.xml")

if webcam.isOpened():
        rval, frame = webcam.read()
else:
    rval = False
count = 0
while rval:
    minisize = (frame.shape[1]/4,frame.shape[0]/4)
    miniframe = cv2.resize(frame, minisize)
    faces = classifier1.detectMultiScale(miniframe)
    if not len(faces):
        count = count + 1
    else:
        count = 0
    for f in faces:
        x, y, w, h = [v*4 for v in f]
        cv2.rectangle(frame, (x,y), (x+w,y+w), (0, 0, 255))
    cv2.putText(frame, "Press ESC to close.", (5, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))
    cv2.imshow("preview", frame)
    rval, frame = webcam.read()
    if count > 12:
        winsound.PlaySound("wub.wav", winsound.SND_FILENAME)
    key = cv2.waitKey(20)
    if key in [27, ord('Q'), ord('q')]: # exit on ESC
        break

    
