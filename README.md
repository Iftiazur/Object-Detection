# YOLOv8 Real-Time Object Detection

This project demonstrates real-time object detection using the **YOLOv8** model and **OpenCV**. The script captures video from a webcam, processes each frame with the YOLOv8 model, and displays detected objects with bounding boxes.

## 📸 Demo

Below are sample screenshots of the real-time detection in action:

![Demo 1](/assets/demo1.png)

![Demo 2](/assets/demo2.png)

![Demo 2](/assets/demo3.png)

## 📂 Project Structure

```
yolo_realtime_project/
│── assets                 # Contains images for the readme
│── main.py                # Main script for real-time object detection
│── README.md              # Documentation
│── requirements.txt       # Dependencies

```

## 🚀 Installation

Ensure you have Python installed (Python 3.7+ recommended). Then, install the required dependencies:

```sh
pip install ultralytics opencv-python
```

If you have a `requirements.txt` file, you can install all dependencies at once:

```sh
pip install -r requirements.txt
```

## 💜 Usage

Run the script to start real-time object detection:

```sh
python main.py
```

### Controls
- Press **'q'** to exit the program.

## 📌 Code Explanation

The script follows these steps:
1. Loads the **YOLOv8** pre-trained model (`yolov8s.pt`).
2. Captures frames from the webcam using OpenCV.
3. Converts frames from **BGR to RGB** for processing.
4. Runs YOLOv8 on each frame to detect objects.
5. Draws bounding boxes around detected objects.
6. Displays the real-time processed frame.
7. Press **'q'** to exit.

## 🛠 Troubleshooting

- **Webcam Not Opening?**  
  Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`.

- **Missing Dependencies?**  
  If you face module import errors, install missing dependencies:  
  ```sh
  pip install -r requirements.txt
  ```

- **Low FPS or Lag?**  
  - Reduce input frame size in OpenCV.
  - Use a **lighter** YOLO model (e.g., `yolov8n.pt` instead of `yolov8s.pt`).
  - Run on a GPU for better performance.

## 🛠️ Customization

You can modify the script to use a different YOLOv8 model by replacing:
```python
model = YOLO("yolov8s.pt")
```
with:
- `yolov8n.pt` (Nano - Fastest, Less Accurate)
- `yolov8m.pt` (Medium)
- `yolov8l.pt` (Large - More Accurate, Slower)

## 📌 Notes

- The YOLOv8 model (`yolov8s.pt`) will be **downloaded automatically** the first time you run the script.
- You can use an **external video file** instead of the webcam by modifying:
  ```python
  cap = cv2.VideoCapture("video.mp4")
  ```

## 💜 License
This project is open-source and available for educational purposes.

---

Enjoy detecting objects in real time! 🚀