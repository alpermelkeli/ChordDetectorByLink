from flask import Flask, request, jsonify
import autochord
import os
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/recognize", methods=["POST"])
def recognize():
    # Check if the POST request contains a link
    if "link" not in request.form:
        return "No YouTube video link in the request"

    youtube_link = request.form["link"]

    # Download audio from YouTube
    try:
        yt = YouTube(youtube_link)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=".")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.wav'
        os.rename(out_file, new_file)
    except Exception as e:
        return f"Error downloading YouTube audio: {str(e)}"

    # Perform chord recognition
    lab_output_path = new_file[:-4] + ".lab"
    autochord.recognize(new_file, lab_fn=lab_output_path)

    # Return the response as JSON
    response = {"lab_content": "", "message": "Chord recognition complete"}
    with open(lab_output_path, 'r') as lab_file:
        response["lab_content"] = lab_file.read()

    # Remove the WAV and LAB files
    os.remove(new_file)
    os.remove(lab_output_path)

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
