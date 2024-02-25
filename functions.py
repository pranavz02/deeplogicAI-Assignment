from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from pdf2image import convert_from_path


def pdf_to_png(input_pdf_path):
    try:
        # Convert PDF to list of PIL images
        image = convert_from_path(input_pdf_path)
        image_path = os.path.join("uploads", "input.png")
        print(f"Conversion successful. PNG images saved.")
        return image_path
    except Exception as e:
        print(f"Error: {e}")


def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    print("In img: ")
    print(text)
    return text


def extract_key_value_pairs(text):
    key_value_pairs = [line.split(":") for line in text.split("\n") if ":" in line]
    key_value_dict = {key.strip(): value.strip() for key, value in key_value_pairs}

    return key_value_dict


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {"pdf"}
