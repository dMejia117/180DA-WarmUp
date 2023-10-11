import cv2
import numpy as np
from sklearn.cluster import KMeans


*******Resources****************
#https://github.com/opencv/opencv/blob/master/samples/python/kmeans.py
#https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
#https://stackoverflow.com/questions/51853018/how-do-i-install-opencv-using-pip


def dominant_color(image, k=1):
    # Reshape the image to be a list of pixels
    pixels = image.reshape((-1, 3))
    
    # Apply KMeans
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    
    # Return the dominant color
    return kmeans.cluster_centers_.astype(int)[0]

def process_frame(frame):
    # Get frame size
    h, w, _ = frame.shape

    # Define the central rectangle
    top, bottom = h//4, 3*h//4
    left, right = w//4, 3*w//4
    
    # Extract the rectangle from frame
    rect = frame[top:bottom, left:right]
    
    # Find the dominant color in the rectangle
    color = dominant_color(rect)
    
    # Draw the rectangle
    #cv2.rectangle(frame, (left, top), (right, bottom), color.tolist(), 2)
    
    # Draw a filled rectangle (color block) at the top-left corner of the frame
    frame[10:110, 10:110] = color
    return frame


# Start capturing the video feed
cap = cv2.VideoCapture(0)  # 0 for default camera

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Process frame
        processed_frame = process_frame(frame)
        # Display the resulting frame
        cv2.imshow('Video', processed_frame)
        # Break the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
