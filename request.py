# NOT COMPLETED

import requests

# URL of the predict endpoint
url = 'http://127.0.0.1:5000/predict'

# Load an image file
image_path = 'C:\Users\LENOVO\Downloads\golden-yellow-plain-tshirt-mydesignation.jpg'
files = {'file': open(image_path, 'rb')}

# Send POST request with the image file
response = requests.post(url, files=files)

# Print the prediction result
print(response.json())
