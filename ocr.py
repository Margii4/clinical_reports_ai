import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os

def preprocess_image(img: Image.Image) -> Image.Image:
    img = img.convert("L")
    img = img.point(lambda x: 0 if x < 180 else 255, "1")
    return img

def extract_text_from_pdf(pdf_path: str) -> str:
    images = convert_from_path(pdf_path, dpi=300)
    texts = []
    for img in images:
        img = preprocess_image(img)
        text = pytesseract.image_to_string(img, lang='ita')
        texts.append(text)
    return "\n\n".join(texts)
