from flask import Flask, jsonify, render_template, request
import requests
import time
import threading
import queue

app = Flask(__name__)

# Set the initial interval in seconds
interval = 3
# API endpoint URL
endpoint = 'https://dummyjson.com/users/'

# Queue to hold request details
request_queue = queue.Queue()
stop_event = threading.Event()

def randomize_slug():
    return str(time.time()).replace(".", "")

def send_api_request():
    # while not stop_event.is_set():
    for _ in range(3):
        slug = randomize_slug()
        response = requests.get(endpoint + slug)
        
        # Prepare the details to be sent to the frontend
        details = {
            "endpoint": endpoint + slug,
            "request_time": response.elapsed.total_seconds(),
            "status_code": response.status_code
        }
        
        # Put the details in the queue
        request_queue.put(details)
        time.sleep(interval)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/start")
def start_requests():
    global stop_event
    stop_event.clear()  # Reset the stop event
    # Start the API request thread
    thread = threading.Thread(target=send_api_request)
    thread.daemon = True
    thread.start()
    return jsonify({"message": "Started API requests!"})

@app.route("/set_interval", methods=["POST"])
def set_interval():
    global interval
    new_interval = request.json.get("interval", interval)
    interval = new_interval
    return jsonify({"message": f"Interval set to {interval} seconds."})

@app.route("/stop")
def stop_requests():
    stop_event.set()  # Signal the thread to stop
    return jsonify({"message": "Stopped API requests!"})

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get_updates")
def get_updates():
    updates = []
    while not request_queue.empty():
        updates.append(request_queue.get())
    return jsonify(updates)

if __name__ == "__main__":
    app.run(debug=True)
