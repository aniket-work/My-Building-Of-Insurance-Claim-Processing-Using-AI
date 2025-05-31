# pdf_processor.py
import tempfile
import fitz  # PyMuPDF
from PIL import Image
from ocr_engine import process_single_image

def process_pdf(pdf_file, prompt_text):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(pdf_file.read())
    temp_file.close()
    pdf_path = temp_file.name
    doc = fitz.open(pdf_path)
    all_results = []
    total_processing_time = 0
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        result = process_single_image(image, prompt_text)
        result["page"] = page_num + 1
        all_results.append(result)
        total_processing_time += result["processing_time"]
    combined_json = {
        "pages": all_results,
        "total_processing_time": total_processing_time
    }
    return combined_json
