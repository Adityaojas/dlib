import numpy as np
import dlib
import cv2


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

img = 'fb_img.jpg'
shape_predictor = 'shape_predictor_68_face_landmarks.dat'

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor)

image = cv2.imread(img)

width = 500
r = 500 / image.shape[1]
height = int(image.shape[0]*r)
dim = (width, height)

image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rects = detector(gray, 1)

FACIAL_LANDMARKS_IDXS = { "mouth": (48, 68), "right_eyebrow": (17, 22), "left_eyebrow": (22, 27),
                         "right_eye": (36, 42), "left_eye": (42, 48), "nose": (27, 35),
                         "jaw": (0, 17) }

for (i, rect) in enumerate(rects):
    shape = predictor(gray, rect)
    shape = shape_to_np(shape)

    (x, y, w, h) = rect_to_bb(rect)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    for (x, y) in shape:
        cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

    for (i,j) in FACIAL_LANDMARKS_IDXS.values():
        for ind in range(i, j-1):
            cv2.line(image, tuple(shape[ind]), tuple(shape[ind+1]), (0, 255, 0), 1)
            

cv2.imshow("Output", image)
cv2.waitKey(0)
