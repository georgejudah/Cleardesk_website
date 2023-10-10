from flask import Flask, request, render_template, send_file
import zipfile
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download-zip')
def download_zip():
    # Path to the zipped folder
    zip_folder_path = 'clear_desk-win32-x64.zip'

    # Check if the zipped folder exists
    if not os.path.exists(zip_folder_path):
        return "Zipped folder not found", 404

    # Send the zipped folder to the user
    return send_file(zip_folder_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
