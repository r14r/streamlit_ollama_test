import streamlit as st
from streamlit_ollama.api import get_models

st.set_page_config(page_title="Streamlit Ollama Models", page_icon="🧠")

st.title("Ollama Models Browser")

type_options = [None, "completion", "embedding"]
func_options = [None, "tools", "thinking"]

type_choice = st.selectbox("Select model type", type_options, index=0)
func_choice = st.selectbox("Select model function", func_options, index=0)

if st.button("Fetch models"):
    with st.spinner("Fetching models..."):
        filtered_models = get_models(type=type_choice, func=func_choice)
        if filtered_models:
            st.success(f"Found {len(filtered_models)} models:")
            for model in filtered_models:
                st.write(f"- {model}")
        else:
            st.warning("No models found matching selection.")

st.markdown("---")
st.write("Note: Leave type or function as None to not filter by that category.")

