** IMPORTANT** Download dlib's pretrained shape-predictor and place it in the same directory as that of the code:
Link: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

First thing first, activate the particular environment. In my case,

$ conda activate env_dlib

- The  facial landmark detector in dlib is an implementation of the research paper: https://pdfs.semanticscholar.org/d78b/6a5b0dcaa81b1faea5fb0000045a62513567.pdf
- The code comprises of 2 parts: Localizing the face using any pretrained model or custom_trained, and then applying the shape-predictor to extract the facial features
- Localizing the face can be achieved by any method, it can be done using OpenCVs pretrained Haar Cascades, or by deep learning algorithms, or may be by using Historam Oriented Gradients + Linear SVM (which is included in dlib as dlib.get_frontal_face_detector())
- Feature detection in dlib is trained on the I-BUG 300 W dataset (https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/). It returns 68 points specifying the x, y coordinates of the features. (other models such as the 194 point model trained on the HELEN Dataset exist, but we'll be using dlib's implementation)
- I've included 2 helper functions in the code (Thanks to the PyImageSearch Blogs) to convert the dlib returned objects to OpenCV compatible numpy arrays.

`landmarks.py` uses the image variable to extract the features
`video_landmarks.py` takes the feed from the webcam and extracts features in real time, and also writes the output to the memory.
