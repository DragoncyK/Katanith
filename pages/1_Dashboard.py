import streamlit as st

st.set_page_config(page_title="Katanith Journal", page_icon="🗡️", layout="wide")

# Comprobamos si el usuario ha iniciado sesión previamente
if 'user' not in st.session_state or st.session_state.user is None:
    st.warning("⚠️ Debes iniciar sesión en la página principal para acceder a esta sección.")
    st.stop() # Detiene la ejecución de la página si no hay sesión