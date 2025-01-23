Recognise Me
Recognise Me is a playful “fun filter” app that lets couples, friends, or family members swap eyes in a photo. It’s a lighthearted way to see if everyone can still “recognise” each other after the swap!

Table of Contents
Description
Features
Demo
Installation
Usage
How It Works
Future Improvements
License
Contributing
Contact
Description
“Recognise Me” takes a single photo with at least two people facing forward. It then detects both faces, swaps their eyes, and presents the resulting image to see if others can guess who’s who. It’s a fun twist on face filters that can be used at parties or for social media challenges.

Features
Eye Swapping: Detects the left and right eyes of two faces and exchanges them in the same image.
Simple to Run: Command-line or script-based tool (can be adapted into a web interface).
Lightweight: Uses common Python libraries such as OpenCV, dlib, and numpy.
Demo
If you have a demo image, you can provide screenshots here:

Original Image	Swapped Image
Insert Original	Insert Swapped
(Feel free to replace with real images or GIFs.)

Installation
Clone the Repository

bash
Copy
git clone https://github.com/<YOUR_USERNAME>/recognise-me.git
cd recognise-me
Install Dependencies

Make sure you have Python 3.7+ installed.
Then install required packages:
bash
Copy
pip install -r requirements.txt
You’ll typically need:
opencv-python
dlib
numpy
Obtain the Dlib Landmark Model

Download the file shape_predictor_68_face_landmarks.dat from dlib-models
Place it in the data/ folder so the script can access it.
Usage
Prepare Your Photo

Place a single image named (for example) group_photo.jpg in the data/ folder. Make sure it contains two people looking forward.
Run the Script

bash
Copy
python src/main.py
The script will:
Detect the two faces.
Swap their eyes.
Display the original and swapped images in pop-up windows.
Optionally, save the swapped output to a file named swapped_result.jpg.
Enjoy the Result

Share your fun swapped photo with friends, or challenge them to guess whose eyes are whose!
How It Works
Face & Landmark Detection: Uses dlib.get_frontal_face_detector() to detect faces and shape_predictor_68_face_landmarks.dat for facial landmark detection (68 points).
Identify Eye Regions: The script locates the indices for the left (36–41) and right (42–47) eyes.
Swapping: Extracts each eye region (with masks), resizes if necessary, and copies from one face to the other.
Display: Shows the original and final swapped images side-by-side or in separate windows.
Future Improvements
Seamless Blending: Use Poisson blending or cv2.seamlessClone to better merge edges.
Multiple Faces: Allow the user to pick which two faces to swap if more than two faces are detected.
Web Interface: Convert to a lightweight web app using Flask or Streamlit for a user-friendly upload-and-swap experience.
Swap Other Features: Extend swapping to lips, noses, or hair for more fun.
License
This project is available under the MIT License. Feel free to use, modify, and distribute as you see fit. If you build something awesome, let us know!
