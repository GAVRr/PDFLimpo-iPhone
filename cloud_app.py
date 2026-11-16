"""Entry point for Streamlit Community Cloud."""
import os
import runpy

import streamlit as st

try:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    api_key = None

if api_key:
    os.environ.setdefault("OPENAI_API_KEY", str(api_key))

runpy.run_path("app.py", run_name="__main__")
