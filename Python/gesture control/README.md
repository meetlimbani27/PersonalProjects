
# Hand Tracking Project

A brief description of what this project does and who it's for


## Introduction
This Python project utilizes the OpenCV and MediaPipe libraries to perform hand tracking in real-time through a computer's camera. The application detects landmarks on the user's hand and provides a foundation for creating interactive applications based on hand gestures.
## Prerequisites
Make sure you have the following dependencies installed before running the project:

- Python 3.x
- OpenCV (cv2)
- MediaPipe
- NumPy

You can install the required libraries using the following command:

`pip install opencv-python mediapipe numpy`

## Project Structure

- hand_tracking.py : The main script that captures the video feed from the camera, processes it to detect hand landmarks, and displays the video with additional information such as frames per second (FPS).

- hand_detector.py : A class-based implementation encapsulating the hand detection logic. This class can be easily reused in other projects.

## Usage

1. Run the hand_tracking.py script:
`python hand_tracking.py`
2. A window will open displaying the camera feed with hand landmarks drawn on it.
3. Perform hand gestures in front of the camera to see the real-time hand tracking in action.
4. Press 'q' to exit the application.
## Customization
You can extend this project by adding functionality based on specific hand gestures. Modify the hand_tracking.py script to include actions or triggers based on the detected hand landmarks.
## Additional Notes

- Adjust the detectionCon and trackCon parameters in the handDetector class constructor in hand_detector.py to control the hand detection and tracking confidence thresholds.

- The HAND_CONNECTIONS variable in the handDetector class can be modified to customize the displayed connections between hand landmarks.
## Troubleshooting

If you encounter issues with the camera feed or hand tracking, ensure that your camera is working correctly and that you have installed the required libraries.
## Acknowledgments

This project is based on the OpenCV and MediaPipe libraries, and their contributions to computer vision and hand tracking.

Feel free to explore and enhance this project to suit your needs!





