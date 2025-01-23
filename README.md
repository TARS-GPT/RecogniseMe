# Recognise Me

**Recognise Me** is a playful “fun filter” app that lets couples, friends, or family members swap eyes in a photo. It’s a lighthearted way to see if everyone can still **recognise** each other after the swap!

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Description
**Recognise Me** takes a single image with at least two people facing the camera, swaps their eyes, and shows the edited result. It’s a fun, quick way to see how well friends and family can recognise one another after the swap!

## Features
- **Eye Swapping**: Detects and swaps the left and right eyes between two faces in the same image.  
- **Lightweight**: Depends on common Python libraries (OpenCV, dlib, numpy).  
- **Simple**: Runs as a script; can be adapted into a web interface or GUI.

## Demo
*(Replace with real images or gifs if you have them.)*

1. **Original**: A photo of two people.  
2. **Swapped**: After running the script, each person has the other’s eyes.

## Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/recognise-me.git
   cd recognise-me
   ```
2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
   - Typically requires:  
     - [OpenCV](https://opencv.org/)  
     - [dlib](http://dlib.net/)  
     - [numpy](https://numpy.org/)  

3. **Dlib Landmark Model**  
   - Download `shape_predictor_68_face_landmarks.dat` from [dlib-models](https://github.com/davisking/dlib-models) if not included.  
   - Place it in the `data/` folder.

## Usage

1. **Prepare Your Photo**  
   - Ensure your image (e.g., `group_photo.jpg`) with two faces is located in `data/`.

2. **Run the Script**  
   ```bash
   python src/main.py
   ```
   - The script will:
     - Detect the two faces.  
     - Swap their eyes.  
     - Show the original and swapped images in windows.  
     - Optionally save the swapped image as `swapped_result.jpg`.

3. **Have Fun**  
   - Share the swapped photo and challenge others to identify who’s who!

## How It Works
1. **Face & Landmark Detection**: Uses `dlib.get_frontal_face_detector()` and `shape_predictor_68_face_landmarks.dat` to locate 68 facial landmarks per face.  
2. **Eye Extraction**: Locates the left (indices 36–41) and right (42–47) eyes.  
3. **Swapping**: Copies each eye region from one face to the other, resizing if needed.  
4. **Display/Save**: Outputs the final swapped image for fun comparisons.

## Future Improvements
- **Seamless Blending**: Use Poisson blending or `cv2.seamlessClone` for smoother edges.  
- **Multiple Faces**: Option to pick which two faces to swap if more than two are detected.  
- **Web App**: Provide a simple upload-and-swap interface with Flask or Streamlit.  
- **Swap Other Features**: Experiment with mouths, noses, or entire face halves.

## License
This project is released under the [MIT License](LICENSE). You’re free to use, modify, and distribute the code as needed.

## Contributing
Contributions and feedback are always welcome!  
1. Fork this repository.  
2. Create a new branch: `git checkout -b feature/YourFeature`.  
3. Make changes and commit: `git commit -m "Add YourFeature"`.  
4. Push to your fork: `git push origin feature/YourFeature`.  
5. Create a Pull Request on this repo.


Enjoy “Recognise Me” and have a blast seeing how well your friends or family can still recognise each other!
