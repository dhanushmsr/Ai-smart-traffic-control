import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

EMERGENCY_CLASSES = ["ambulance", "fire truck", "police"]

def detect_emergency(source):
    cap = cv2.VideoCapture(source)
    emergency_found = False
    vehicle_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]

                if label in ["car", "bus", "truck", "motorcycle"]:
                    vehicle_count += 1

                if label in EMERGENCY_CLASSES:
                    emergency_found = True

        cv2.imshow("Traffic Monitoring", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return emergency_found, vehicle_count
