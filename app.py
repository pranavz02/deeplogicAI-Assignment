from flask import Flask, render_template, request, send_file
import os
import csv
from functions import extract_text_from_image, extract_key_value_pairs, allowed_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    if file and allowed_file(file.filename):
        image_path = os.path.join('uploads', 'input.png')
        file.save(image_path)

        extracted_text = extract_text_from_image(image_path)
        key_value_pairs = extract_key_value_pairs(extracted_text)

        csv_output = os.path.join('uploads', 'output.csv')
        with open(csv_output, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for key, value in key_value_pairs.items():
                csv_writer.writerow([key, value])

        return send_file(csv_output, as_attachment=True)

    return render_template('index.html', error='Invalid file format')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
