Eye Swap in a Single Image
Swap the eyes of two people detected in one image using dlib for facial landmarks and OpenCV for image manipulation. This repository provides a simple yet extendable example of facial feature manipulation in Python.

<sup>(Replace the above link with your own demo image or remove this section.)</sup>

Table of Contents
Features
Project Structure
Installation
Usage
Troubleshooting
Roadmap
Contributing
License
Features
Automatic Face Detection: Uses dlib to detect faces in a single image.
Facial Landmark Extraction: Identifies eye regions (68-point model).
Eye Swapping: Swaps the left and right eyes between two detected faces.
Extendable: Code can be adapted for more advanced blending, web interfaces, or additional facial features.
Project Structure
css
Copy
eye_swap_single_image/
├── data/
│   ├── group_photo.jpg
│   └── shape_predictor_68_face_landmarks.dat
├── src/
│   └── main.py
├── requirements.txt
├── README.md
└── .gitignore
data/
group_photo.jpg: Your image file containing two faces.
shape_predictor_68_face_landmarks.dat: Pre-trained dlib landmarks model.
src/
main.py: Main Python script for detecting faces and swapping eyes.
requirements.txt
Lists Python dependencies.
README.md
Project documentation (you’re reading it now!).
.gitignore
Specifies files/folders Git should ignore (e.g., virtual environments, caches).
Installation
Clone or Download this repository:

bash
Copy
git clone https://github.com/<YOUR_USERNAME>/eye_swap_single_image.git
cd eye_swap_single_image
Install Dependencies:

bash
Copy
pip install -r requirements.txt
The main libraries are:

OpenCV for image processing
dlib for face detection and landmarks
NumPy for numeric operations
Obtain Landmark Model (if not in data/ already):

Download the shape_predictor_68_face_landmarks.dat file.
Place it in the data/ folder so the path in main.py is valid.
Usage
Edit Your Image

Ensure group_photo.jpg (or another image with exactly two faces) is placed in data/.
Update the paths in src/main.py if you use different filenames.
Run the Script:

bash
Copy
python src/main.py
Results:

Two windows will pop up: one showing the original image and another showing the swapped result.
By default, a swapped_result.jpg file may be created (depending on your main.py settings).
Troubleshooting
No Faces Detected: Ensure your image has two clear, front-facing heads. Check lighting and resolution.
Dlib Installation Issues: Some systems need extra steps (like installing CMake) to build dlib. Check dlib’s documentation.
Image Path Errors: Verify group_photo.jpg and shape_predictor_68_face_landmarks.dat paths in main.py match your folder structure.
More Than Two Faces: The demo script only swaps eyes between the first two detected faces. Modify the code to handle more if needed.
