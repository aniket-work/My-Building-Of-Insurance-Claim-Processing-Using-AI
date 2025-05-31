import streamlit as st
from config_loader import load_json_config, load_yaml_settings
from pdf_processor import process_pdf
from utils import parse_doctags_to_rows, rows_to_dataframe
import os

# Load configs
CONFIG = load_json_config("config.json")
SETTINGS = load_yaml_settings("settings.yaml")

HF_TOKEN = os.getenv("HF_TOKEN")

def main():
    st.set_page_config(page_title=SETTINGS['app']['page_title'], layout=SETTINGS['app']['layout'], initial_sidebar_state="collapsed")
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] {{display: none;}}
        body {{background: #f4f7fa;}}
        .claim-app-header {{text-align: center; font-size: 2.5em; font-weight: 800; color: {SETTINGS['ui']['header_color']}; margin-top: 0.5em; margin-bottom: 0.2em; letter-spacing: 1px;}}
        .claim-app-subheader {{text-align: center; font-size: 1.3em; color: {SETTINGS['ui']['subheader_color']}; margin-bottom: 2em;}}
        .claim-table th, .claim-table td {{padding: 14px 22px; border: 1px solid {SETTINGS['ui']['table_border']}; font-size: 1.13em;}}
        .claim-table th {{background: {SETTINGS['ui']['table_header_bg']}; color: {SETTINGS['ui']['table_header_color']}; font-weight: 700;}}
        .claim-table {{border-collapse: collapse; width: {SETTINGS['ui']['table_width']}; margin: 0 auto 2em auto; background: {SETTINGS['ui']['table_row_bg']}; box-shadow: {SETTINGS['ui']['table_shadow']}; border-radius: {SETTINGS['ui']['table_radius']}; overflow: hidden;}}
        .claim-page-label {{text-align: center; font-size: 1.1em; color: #3949ab; margin-bottom: 1.5em;}}
        .claim-success {{text-align: center; font-size: 1.1em; color: #388e3c; margin-top: 2em;}}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<div class='claim-app-header'>{SETTINGS['app']['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='claim-app-subheader'>{SETTINGS['app']['subtitle']}</div>", unsafe_allow_html=True)
    if not HF_TOKEN:
        st.warning("HF_TOKEN not found in .env file. Authentication may fail.")
    uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_pdf is not None:
        process_button = st.button("Process PDF")
        if process_button:
            with st.spinner("Processing PDF..."):
                try:
                    combined_json = process_pdf(uploaded_pdf, CONFIG['default_prompt'])
                    for page in combined_json.get("pages", []):
                        doctags = page.get("doctags", "")
                        st.markdown(f"<div class='claim-page-label'>Page {page.get('page', '?')}</div>", unsafe_allow_html=True)
                        rows = parse_doctags_to_rows(doctags)
                        if rows:
                            df = rows_to_dataframe(rows)
                            st.markdown(df.to_html(index=False, classes='claim-table'), unsafe_allow_html=True)
                        else:
                            st.info("No structured fields detected on this page.")
                    st.markdown(f"<div class='claim-success'>PDF processed successfully in {combined_json['total_processing_time']:.2f} seconds</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error processing PDF: {str(e)}")

if __name__ == "__main__":
    main()