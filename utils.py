# utils.py
import re
import pandas as pd

def parse_doctags_to_rows(doctags: str):
    """Parse <text>...</text> blocks from doctags and return label-value pairs."""
    text_blocks = re.findall(r'<text>.*?</text>', doctags, re.DOTALL)
    rows = []
    for i in range(0, len(text_blocks), 2):
        label = re.sub(r'<.*?>', '', text_blocks[i]).strip() if i < len(text_blocks) else ''
        value = re.sub(r'<.*?>', '', text_blocks[i+1]).strip() if i+1 < len(text_blocks) else ''
        if label or value:
            rows.append((label, value))
    return rows

def rows_to_dataframe(rows):
    """Convert label-value rows to a pandas DataFrame."""
    return pd.DataFrame(rows, columns=["Field", "Value"])
