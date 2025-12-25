import cv2
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def process_stream(source):
    cap = cv2.VideoCapture(source)

    total_vehicles = 0
    frame_count = 0
    emergency_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, stream=True)
        vehicles_in_frame = 0

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # NORMAL VEHICLES
                if label in ["car", "bus", "truck", "motorcycle"]:
                    vehicles_in_frame += 1
                    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                    cv2.putText(frame, label, (x1,y1-5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        total_vehicles += vehicles_in_frame
        frame_count += 1

        # 🔴 MANUAL EMERGENCY TRIGGER (PRESS 'E')
        key = cv2.waitKey(1) & 0xFF
        if key == ord('e'):
            emergency_count += 1
            cv2.putText(frame, "🚨 EMERGENCY VEHICLE DETECTED",
                        (40,80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,0,255),
                        3)

        cv2.putText(frame, f"Vehicles: {vehicles_in_frame}",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255,0,0),
                    2)

        cv2.imshow("AI Traffic Monitoring", frame)

        if key == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

    avg_vehicles = total_vehicles // max(frame_count, 1)

    return {
        "total": total_vehicles,
        "average": avg_vehicles,
        "emergency": emergency_count,
        "time": time.strftime("%H:%M:%S")
    }
