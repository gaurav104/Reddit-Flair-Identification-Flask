import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from support.predictor import predict_flair
from support.process_file import process_file


app = Flask(__name__)

UPLOAD_FOLDER = "./uploads/"
# DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = {'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
        # file = request.files['file']
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # predicted_dict = process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename),filename)
        # return jsonify(predicted_dict)

        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            predicted_dict = process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename),filename)
            return jsonify(predicted_dict)
    # return render_template('testing.html')

# @app.route('/automated_testing/<filename>')
# def get_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
        app.run(debug=True)
