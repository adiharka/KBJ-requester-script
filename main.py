# Set the interval in seconds
interval = 3
# API endpoint url
endpoint = 'https://dummyjson.com/users/'

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

while True:
  send_api_request()
  time.sleep(interval)