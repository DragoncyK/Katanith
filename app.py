import streamlit as st
from supabase import create_client, Client

st.set_page_config(page_title="Katanith Journal", page_icon="🗡️", layout="centered")

@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

# Inicializar la variable de sesión
if 'user' not in st.session_state:
    st.session_state.user = None

st.title("Katanith Trading Journal")
st.markdown("---")

# Si ya ha iniciado sesión, mostramos un aviso
if st.session_state.user:
    st.success(f"Sesión activa: {st.session_state.user.email}")
    if st.button("Cerrar Sesión"):
        supabase.auth.sign_out()
        st.session_state.user = None
        st.rerun()
else:
    st.subheader("Acceso al sistema")
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Iniciar Sesión"):
            try:
                res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                st.session_state.user = res.user
                st.success("¡Acceso concedido!")
                st.rerun()
            except Exception as e:
                st.error(f"Error al iniciar sesión: Comprueba tus datos.")

    with col2:
        if st.button("Crear Cuenta"):
            try:
                res = supabase.auth.sign_up({"email": email, "password": password})
                st.success("¡Cuenta creada! Revisa tu correo para verificarla.")
            except Exception as e:
                st.error(f"Error al crear la cuenta: {e}")