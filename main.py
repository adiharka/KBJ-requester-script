# Set the interval in seconds
# interval = 3
# API endpoint url
endpoint = 'https://dummyjson.com/users/'

from flask import Flask

app = Flask(__name__)

import requests
import time

def randomize_slug():
  return str(time.time()).replace(".", "")

def send_api_request():
  slug = randomize_slug()
  response = requests.get(endpoint + slug)
  # Print the request endpoint
  print(f"Request endpoint: {endpoint + slug}")
  # Print the request time
  print(f"Request time: {response.elapsed.total_seconds()} seconds")
  # Print the response status code
  print(f"Response status code: {response.status_code}")
  print('\n')
  return response

# while True:
send_api_request()
#   time.sleep(interval)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def api_requester():
    res = send_api_request()
    return res