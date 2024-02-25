# deeplogicAI-Assignment

# Invoice to CSV Converter

This is a simple web application built with Flask that allows users to upload a PDF file, process each page, extract key-value pairs using Tesseract OCR, and save the results as a CSV file.

## Features

- Upload an invoice.
- Extract text from each image using Tesseract OCR.
- Parse key-value pairs from the extracted text.
- Save the key-value pairs to a CSV file.
- Download the CSV file.

## Prerequisites

- Python 3.x
- Flask
- pytesseract
- Pillow
- tabula-py
- Tesseract OCR

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/pranavz02/deeplogicAI-Assignment.git
    cd pdf-to-csv-converter
    ```

2. Install the required dependencies:

    ```bash
    pip install Flask pytesseract Pillow tabula-py
    ```

3. Install Tesseract OCR:

    - Download and install Tesseract OCR from the official website: https://github.com/tesseract-ocr/tesseract
    - During the installation, make sure to add Tesseract to your system's PATH.

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to http://127.0.0.1:5000/

3. Upload an Invoice using the provided form.

4. Click the "Process and Download CSV" button.

5. Download the generated CSV file.

## Folder Structure

- `uploads/`: Folder to store uploaded PNG files and generated CSV files.
- `templates/`: HTML file for the frontend.

## Troubleshooting

- If you encounter issues with Tesseract OCR, ensure it is correctly installed and added to your system's PATH.

