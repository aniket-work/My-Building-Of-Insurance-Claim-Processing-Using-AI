# ocr_engine.py
import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from huggingface_hub import login
from constants import MODEL_NAME, MAX_NEW_TOKENS
from docling_core.types.doc import DoclingDocument
from docling_core.types.doc.document import DocTagsDocument
import time
import os

HF_TOKEN = os.getenv("HF_TOKEN")

def process_single_image(image, prompt_text):
    if HF_TOKEN:
        login(token=HF_TOKEN)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    start_time = time.time()
    processor = AutoProcessor.from_pretrained(MODEL_NAME)
    model = AutoModelForVision2Seq.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float32,
    ).to(device)
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": prompt_text}
            ]
        },
    ]
    prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(text=prompt, images=[image], return_tensors="pt")
    inputs = inputs.to(device)
    generated_ids = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS)
    prompt_length = inputs.input_ids.shape[1]
    trimmed_generated_ids = generated_ids[:, prompt_length:]
    doctags = processor.batch_decode(
        trimmed_generated_ids,
        skip_special_tokens=False,
    )[0].lstrip()
    doctags = doctags.replace("<end_of_utterance>", "").strip()
    doctags_doc = DocTagsDocument.from_doctags_and_image_pairs([doctags], [image])
    doc = DoclingDocument(name="Document")
    doc.load_from_doctags(doctags_doc)
    md_content = doc.export_to_markdown()
    processing_time = time.time() - start_time
    output_json = {
        "doctags": doctags,
        "markdown": md_content,
        "processing_time": processing_time
    }
    return output_json
