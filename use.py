import requests

# Set the URL of your Flask app
url = "http://192.168.1.39:5000/recognize"

# Specify the path to the .wav file you want to upload
file_path = "C:/Users/alper/OneDrive/Masaüstü/file.wav"

# Create a dictionary to hold the file data
files = {"file": open(file_path, "rb")}

# Make a POST request to the /recognize route
response = requests.post(url, files=files)

# Print the response content
print(response.text)
