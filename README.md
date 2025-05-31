![Logo](logo.png)

#  OCR Insurance Claim Processing Portal

A professional, enterprise-grade AI-powered web application for automated extraction and review of insurance claim forms from PDF documents. Built with Streamlit, Hugging Face Transformers, and Docling, this app delivers accurate, structured data extraction for insurance workflows.
---
| Category | Technology | Purpose |
|----------|------------|---------|
| **Frontend** | Streamlit | Web interface and user interaction |
| **AI/ML Framework** | PyTorch | Neural network computation and GPU acceleration |
| **AI Models** | HuggingFace Transformers | Pre-trained vision-to-sequence models |
| **Document AI** | Docling Core | Document structure understanding and DocTags |
| **PDF Processing** | PyMuPDF (Fitz) | PDF to image conversion and rendering |
| **Image Processing** | Pillow (PIL) | Image manipulation and format handling |
| **Data Processing** | Pandas | Structured data manipulation and DataFrames |
| **Configuration** | PyYAML | Settings and configuration management |
| **Environment** | Python-dotenv | Secure credential management |
| **Numerical Computing** | NumPy | Array operations and mathematical functions |
| **Model Hosting** | HuggingFace Hub | Model distribution and authentication |
| **Performance** | Accelerate | Model optimization and distributed computing |
| **Language** | Python 3.12+ | Core programming language |


---

## Features

- **AI-Powered OCR**: Uses state-of-the-art vision-to-sequence models for robust document understanding.
- **Insurance-Ready UI**: Clean, professional interface tailored for insurance claim processing teams.
- **Configurable**: All UI and model settings are managed via `settings.yaml` and `config.json`.
- **Modular Codebase**: Easily maintain and extend with clear separation of concerns (utils, config, OCR engine, PDF processor, etc).
- **Secure**: Supports Hugging Face token authentication via `.env` file.
- **Batch Processing**: Handles multi-page PDFs, displaying each page's extracted fields in a structured table.

---

## Project Structure

```
.
├── main.py                  # Streamlit app entry point
├── config_loader.py         # Config and settings loader
├── pdf_processor.py         # PDF-to-image and batch processing logic
├── ocr_engine.py            # Model inference and single-image OCR
├── utils.py                 # Doctag parsing and table helpers
├── constants.py             # Model and UI constants
├── config.json              # Model and app config
├── settings.yaml            # UI and app settings
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment file for secrets
├── LICENSE                  # License file
├── README.md                # This documentation
├── ...                      # Other assets (logo, sample PDFs, design docs)
```

---

## Quickstart

1. **Clone the repository**

```powershell
git clone https://github.com/aniket-work/My-Building-Of-Insurance-Claim-Processing-Using-AI.git
cd My-Building-Of-Insurance-Claim-Processing-Using-AI
```

2. **Install dependencies**

```powershell
pip install -r requirements.txt
```

3. **Configure environment**

- Copy `.env.example` to `.env` and add your Hugging Face token:

```
HF_TOKEN=your_huggingface_token
```

4. **Run the app**

```powershell
streamlit run main.py
```

5. **Upload a PDF**

- Use the web UI to upload an insurance claim PDF and review the extracted fields in a professional table view.

---

## Configuration

- **Model & Processing**: Edit `config.json` for model name, prompt, and output settings.
- **UI & Layout**: Edit `settings.yaml` for app title, colors, and table styles.

---

## Extending & Customization

- Add new field extraction logic in `utils.py`.
- Swap models or prompts in `config.json`.
- Adjust UI/UX in `settings.yaml` and Streamlit code.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/)
- [Docling](https://github.com/docling-ai/docling)
- [Streamlit](https://streamlit.io/)

---

For questions or support, please open an issue or contact the maintainer.
