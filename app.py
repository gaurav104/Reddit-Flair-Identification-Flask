import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from support.predictor import predict_flair
from support.process_file import process_file


app = Flask(__name__)


ALLOWED_EXTENSIONS = {'txt'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        reddit_url = request.form['content']
        detected_flair = predict_flair(reddit_url)
        return render_template("flair.html", flair = detected_flair)
    else:
        return render_template("index.html")

@app.route('/automated_testing', methods=['POST', 'GET'])
def testing():
    if request.method == 'POST':

        try:
            file = request.files['upload_file']
        except KeyError:
            return jsonify(status = 'error', message = "Please make sure the key value is 'upload_file' of the files parameter in the POST request")


        if file.filename == '':
            return jsonify(status = 'error', message = "No file detected")

        if file and allowed_file(file.filename):
            predicted_dict = process_file(file)
            return jsonify(predicted_dict)
        else:
            return jsonify(status = 'error', message = 'Please make sure the request is made with a .txt file')

if __name__ == "__main__":
    app.run(debug=True)
