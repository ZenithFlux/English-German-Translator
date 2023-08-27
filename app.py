import streamlit as st
from translator import EN2GE

st.set_page_config(page_title="English 2 German Translator")

@st.cache_resource
def get_model():
    return EN2GE()

en_txt = st.text_area("#### Enter English Text:", placeholder="Write text to be translated here...")
st.button("Translate")
en_txt = en_txt if en_txt else "Translated text will appear here..."

st.markdown("#### German Text:")
st.markdown(get_model().translate(en_txt))