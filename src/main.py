"""
main.py
--------
A minimal script to swap the eyes of two faces detected in a single image using dlib and OpenCV.
"""

import cv2
import dlib
import numpy as np
import os

# Adjust these paths to match your project setup
PREDICTOR_PATH = os.path.join("data", "shape_predictor_68_face_landmarks.dat")
IMAGE_PATH = os.path.join("data", "group_photo.jpeg")

# Initialize dlib’s face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)

def get_landmarks_for_faces(img):
    """
    Detects all faces in an image and returns a list of landmark arrays (68 points each).
    Each element in the list corresponds to one face.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 1)  # detect faces
    
    if len(faces) < 2:
        raise Exception(f"Expected at least 2 faces, found {len(faces)}.")
    
    landmarks_list = []
    for face_rect in faces:
        shape = predictor(gray, face_rect)
        coords = np.zeros((68, 2), dtype=int)
        for i in range(68):
            coords[i] = (shape.part(i).x, shape.part(i).y)
        landmarks_list.append(coords)
    
    return landmarks_list

def extract_eye_region(img, landmarks, eye_indices):
    """
    Extracts the polygon (convex hull) for an eye given the eye landmark indices.
    Returns (mask, bounding_rect).
    - mask: binary mask of the entire image, with the eye region filled white.
    - bounding_rect: x, y, w, h (the bounding box of that eye region).
    """
    eye_points = landmarks[eye_indices]
    
    # Create a convex hull around the eye
    hull = cv2.convexHull(eye_points)
    
    # Create a mask and fill the hull
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    cv2.fillConvexPoly(mask, hull, 255)
    
    # Bounding box for the eye
    x, y, w, h = cv2.boundingRect(hull)
    
    return mask, (x, y, w, h)

def swap_eyes_in_single_image(img, landmarksA, landmarksB):
    """
    Swaps the eyes between two faces (face A and face B) within the same image.
    Returns a new image with swapped eyes.
    """
    output = img.copy()
    
    # Eye landmark indices (for the 68-landmark model)
    LEFT_EYE_IDX = list(range(36, 42))   # 36-41
    RIGHT_EYE_IDX = list(range(42, 48))  # 42-47
    
    # We'll store the eye regions from each face so we don't overwrite them before the swap
    # This dictionary will hold {'left_eye': (region_image, mask, bounding_rect), 'right_eye': ...}
    faceA_eyes = {}
    faceB_eyes = {}
    
    for eye_indices, label in [(LEFT_EYE_IDX, 'left_eye'), (RIGHT_EYE_IDX, 'right_eye')]:
        # Face A
        maskA, rectA = extract_eye_region(output, landmarksA, eye_indices)
        xA, yA, wA, hA = rectA
        eyeA = output[yA:yA+hA, xA:xA+wA]            # region from face A
        maskA_eye = maskA[yA:yA+hA, xA:xA+wA]
        
        faceA_eyes[label] = (eyeA, maskA_eye, rectA)
        
        # Face B
        maskB, rectB = extract_eye_region(output, landmarksB, eye_indices)
        xB, yB, wB, hB = rectB
        eyeB = output[yB:yB+hB, xB:xB+wB]            # region from face B
        maskB_eye = maskB[yB:yB+hB, xB:xB+wB]
        
        faceB_eyes[label] = (eyeB, maskB_eye, rectB)
    
    # Now swap them: Place B's eyes on A, and A's eyes on B
    for eye_label in ['left_eye', 'right_eye']:
        eyeA, maskA_eye, (xA, yA, wA, hA) = faceA_eyes[eye_label]
        eyeB, maskB_eye, (xB, yB, wB, hB) = faceB_eyes[eye_label]
        
        # Resize B's eye to fit A's bounding box
        eyeB_resized = cv2.resize(eyeB, (wA, hA), interpolation=cv2.INTER_CUBIC)
        
        # Get the region of interest in the output
        roiA = output[yA:yA+hA, xA:xA+wA]
        
        # Replace eye region in face A (where mask is non-zero)
        roiA[maskA_eye > 0] = eyeB_resized[maskA_eye > 0]
        
        # Resize A's eye to fit B's bounding box
        eyeA_resized = cv2.resize(eyeA, (wB, hB), interpolation=cv2.INTER_CUBIC)
        
        # Get the region of interest in the output for face B
        roiB = output[yB:yB+hB, xB:xB+wB]
        
        roiB[maskB_eye > 0] = eyeA_resized[maskB_eye > 0]
        
        # Put the swapped regions back into the output
        output[yA:yA+hA, xA:xA+wA] = roiA
        output[yB:yB+hB, xB:xB+wB] = roiB
    
    return output

def main():
    # Load the image
    img = cv2.imread(IMAGE_PATH)
    if img is None:
        raise FileNotFoundError(f"Could not read {IMAGE_PATH}. Check the path or filename.")
    
    # Detect faces & get their landmarks
    all_landmarks = get_landmarks_for_faces(img)
    
    # Expecting exactly 2 faces for this demo
    if len(all_landmarks) < 2:
        raise Exception("Not enough faces detected for swapping (need at least 2).")
    
    # If there are more than 2 faces, you could let the user pick, 
    # but here we’ll just take the first two
    landmarksA = all_landmarks[0]
    landmarksB = all_landmarks[1]
    
    # Swap eyes in the single image
    swapped_img = swap_eyes_in_single_image(img, landmarksA, landmarksB)
    
    # Show results
    cv2.imshow("Original Image", img)
    cv2.imshow("Swapped Eyes", swapped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Optional: Save the result
    cv2.imwrite("swapped_result.jpg", swapped_img)
    print("Swapped image saved as swapped_result.jpg")

if __name__ == "__main__":
    main()
