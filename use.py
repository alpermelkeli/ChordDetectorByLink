import sys

import requests

# Set the URL of your Flask app
url = "http://3.81.66.38:5000/recognize"

# Specify the YouTube video link you want to recognize
youtube_link = sys.argv[1]

# Create a dictionary to hold the form data
data = {"link": youtube_link}

# Make a POST request to the /recognize route
response = requests.post(url, data=data)

# Function to format and write lab_content to a file
def format_and_write_lab_content(data):
    # Extract lab_content from the JSON response
    lab_content = data.get("lab_content", "")

    # Veriyi düzenle
    formatted_data = lab_content.replace("\t", ",")  # Sekme karakterini virgül ile değiştir

    # Dosyaya yaz
    with open("formatted_data.txt", "w") as file:
        file.write(formatted_data)
    print("Veri başarıyla düzenlendi ve formatted_data.txt dosyasına yazıldı.")

# Call the function with the response content
format_and_write_lab_content(response.json())
