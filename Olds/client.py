import requests

def send_image_to_server(image_path):
    url = 'http://your-server-address/predict'
    with open(image_path, 'rb') as f:
        response = requests.post(url, files={'file': f})
    return response.json()
