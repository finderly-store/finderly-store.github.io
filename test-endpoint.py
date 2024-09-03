import base64
import requests

# Load and encode the image as base64
with open("a388c612-86b5-4723-9d46-0d1a2cdca3d9.jpeg", "rb") as image_file:
    # Encode the image to base64
    base64_encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Prepare the payload for the POST request
payload = {
    "image": f"data:image/jpeg;base64,{base64_encoded_image}"
}

# URL of your FastAPI endpoint
url = "http://127.0.0.1:8000/upload_image/"

# Send POST request to the FastAPI endpoint
response = requests.post(url, json=payload)

# Print response from the server
print(response.status_code)
print(response.json())
