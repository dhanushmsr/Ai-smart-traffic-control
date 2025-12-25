from flask import Flask, render_template, request
import os
from traffic_engine import process_stream
from signal_control import signal_logic

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

status = {
    "state": "Waiting",
    "result": None,
    "level": None,
    "green": None
}

@app.route("/", methods=["GET", "POST"])
def index():
    global status

    if request.method == "POST":
        status["state"] = "Processing"

        mode = request.form["mode"]

        if mode == "live":
            result = process_stream(0)
        else:
            video = request.files["video"]
            path = os.path.join(UPLOAD_FOLDER, video.filename)
            video.save(path)
            result = process_stream(path)

        level, green = signal_logic(result["average"], result["emergency"])

        status["state"] = "Completed"
        status["result"] = result
        status["level"] = level
        status["green"] = green

    return render_template("index.html", status=status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

