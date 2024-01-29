from flask import Flask, request, jsonify
import autochord
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/recognize", methods=["POST"])
def recognize():
    # Check if the POST request contains a file
    if "file" not in request.files:
        return "No file part in the request"

    file = request.files["file"]

    # Check if the user submitted an empty part without filename
    if file.filename == "":
        return "No selected file"

    # Check if the file is an allowed file type (e.g., WAV)
    allowed_extensions = {"wav"}
    if "." not in file.filename or file.filename.rsplit(".", 1)[1].lower() not in allowed_extensions:
        return "Invalid file type. Please upload a .wav file."

    # Save the uploaded file
    upload_folder = "/home/ec2-user/autochord"
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    # Call autochord.recognize with the file path
    lab_output_path = file_path[:-4] + ".lab"
    autochord.recognize(file_path, lab_fn=lab_output_path)

    # Return the response as JSON
    response = {"lab_content": "", "message": "Chord recognition complete"}
    with open(lab_output_path, 'r') as lab_file:
        response["lab_content"] = lab_file.read()

    return jsonify(response)


if __name__ == "__main__":

    app.run(host='0.0.0.0', debug=False)
