import requests

# Set the URL of your Flask app
url = "http://192.168.1.39:5000/recognize"

# Specify the YouTube video link you want to recognize
youtube_link = "https://www.youtube.com/watch?v=r6xw6jlFlJg"

# Create a dictionary to hold the form data
data = {"link": youtube_link}

# Make a POST request to the /recognize route
response = requests.post(url, data=data)

# Print the response content
print(response.text)
