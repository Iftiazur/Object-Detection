import cv2
from ultralytics import YOLO

# Load the YOLOv8 model (pre-trained)
model = YOLO("yolov8s.pt")  

# Start the webcam
cap = cv2.VideoCapture(0)  # 0 = Default webcam

# Set a default FPS in case the webcam doesn't return a valid FPS
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30  # Set default FPS if not detected

# Get video dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Convert frame from BGR to RGB for YOLOv8
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform object detection
    results = model(frame_rgb)  # Run YOLO model on the frame

    # Draw results on the frame
    annotated_frame = results[0].plot()  # This returns the image with bounding boxes

    # Show the frame
    cv2.imshow("YOLOv8 Real-Time Detection", annotated_frame)


    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
