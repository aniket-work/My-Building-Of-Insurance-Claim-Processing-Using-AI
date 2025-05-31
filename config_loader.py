# config_loader.py
import json
import yaml
from pathlib import Path

def load_json_config(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_yaml_settings(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
