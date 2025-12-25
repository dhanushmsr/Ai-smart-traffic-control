import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")  # auto-downloads model

def detect_vehicles():
    cap = cv2.VideoCapture(0)  # 0 = webcam (or replace with video.mp4)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        vehicle_count = 0

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]

                if label in ["car", "bus", "truck", "motorcycle"]:
                    vehicle_count += 1
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.putText(frame,label,(x1,y1-5),
                                cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

        cv2.putText(frame, f"Vehicles: {vehicle_count}",
                    (20,40), cv2.FONT_HERSHEY_SIMPLEX,
                    1,(0,0,255),2)

        cv2.imshow("Real-Time Traffic Monitoring", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

    return vehicle_count
