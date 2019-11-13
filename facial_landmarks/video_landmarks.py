import numpy as np
import datetime
import time
import dlib
import cv2
import os 


def rect_to_bb(shape):
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
 
	return (x, y, w, h)

def shape_to_np(shape, dtype="int"):
    coords = np.zeros((68, 2), dtype=dtype)
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords

shape_predictor = 'shape_predictor_68_face_landmarks.dat'

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor)

cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print('Unable to read camera feed')

f_width = int(cap.get(3))
f_height = int(cap.get(4))

width = 400
r = width / f_width
height = int(r * f_height)

if not os.path.exists('vid_output'):
   os.mkdir('vid_output')

out_path = 'vid_output/vid.avi'

output = cv2.VideoWriter(out_path, 0, 10, (f_width, f_height))

FACIAL_LANDMARKS_IDXS = {"mouth": (48, 68), "right_eyebrow": (17, 22), "left_eyebrow": (22, 27),
                         "right_eye": (36, 42), "left_eye": (42, 48), "nose": (27, 35),
                         "jaw": (0, 17)}

time.sleep(2.0)
while True:

    ret, frame = cap.read()
    if ret == False:
        print('no video feed')
        break
        
    # frame = cv2.resize(frame, (width, height), interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    
    

    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)
        (x, y, w, h) = rect_to_bb(rect)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.putText(frame, "Face #{}".format(i + 1), (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        for (x, y) in shape:
            cv2.circle(frame, (x, y), 4, (0, 0, 255), -1)
            
        for (i,j) in FACIAL_LANDMARKS_IDXS.values():
            for ind in range(i, j-1):
                cv2.line(frame, tuple(shape[ind]), tuple(shape[ind+1]), (0, 255, 0), 2)
            
    output.write(frame)  
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
 
    if key == ord("q"):
        break
 
cap.release()
out.release()
cv2.destroyAllWindows()