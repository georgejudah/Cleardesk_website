from flask import Flask, render_template, send_from_directory
import zipfile
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download-zip')
def download_zip():
    # Create a temporary directory for storing files to be zipped
    temp_dir = 'downloads/temp'
    os.makedirs(temp_dir, exist_ok=True)

    # Create some example files (you can replace these with your own)
    for i in range(3):
        with open(f'{temp_dir}/file{i}.txt', 'w') as file:
            file.write(f'This is file {i}')

    # Create a zip file containing the files in the temporary directory
    zip_filename = 'myfiles.zip'
    with zipfile.ZipFile(os.path.join('downloads', zip_filename), 'w') as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), temp_dir))

    # Remove the temporary directory
    for file in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, file))
    os.rmdir(temp_dir)

    # Send the zip file to the user
    return send_from_directory('downloads', zip_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
