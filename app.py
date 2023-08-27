import streamlit as st
from translator import EN2GE

@st.cache_resource
def get_model():
    return EN2GE()

en_txt = st.text_area("#### Enter English Text:", placeholder="Write text to be translated here...")
st.button("Translate")
en_txt = en_txt if en_txt else "Translated Text will appear here..."

st.markdown("#### German Text:")
st.markdown(get_model().translate(en_txt))