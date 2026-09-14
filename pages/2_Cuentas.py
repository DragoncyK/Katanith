import streamlit as st
from supabase import create_client, Client

st.set_page_config(page_title="Gestión de Cuentas - Katanith", page_icon="🗡️", layout="wide")

# Comprobación de seguridad de sesión
if 'user' not in st.session_state or st.session_state.user is None:
    st.warning("⚠️ Debes iniciar sesión en la página principal para acceder a esta sección.")
    st.stop()

@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()
user_id = st.session_state.user.id

st.title("💼 Gestión de Cuentas de Trading")
st.markdown("---")

# Formulario para añadir nueva cuenta
with st.form("form_cuenta"):
    st.subheader("Añadir nueva cuenta (Axi, Fondeo, Personal...)")
    col1, col2 = st.columns(2)
    with col1:
        nombre_cuenta = st.text_input("Nombre de la cuenta (ej. Axi Personal, Prop Firm Phase 1)")
        broker = st.text_input("Bróker o Empresa de Fondeo (ej. Axi, Wall Street Funded)")
    with col2:
        balance_inicial = st.number_input("Balance Inicial ($)", value=10000.0, step=100.0)
    
    submit_cuenta = st.form_submit_button("Guardar Cuenta")
    
    if submit_cuenta:
        if nombre_cuenta and broker:
            data = {
                "user_id": user_id,
                "nombre_cuenta": nombre_cuenta,
                "broker": broker,
                "balance_inicial": balance_inicial
            }
            supabase.table("cuentas").insert(data).execute()
            st.success("¡Cuenta registrada con éxito!")
        else:
            st.error("Por favor, rellena todos los campos obligatorios.")

st.markdown("---")
st.subheader("Mis Cuentas Activas")

# Cargar y mostrar las cuentas del usuario actual
response = supabase.table("cuentas").select("*").eq("user_id", user_id).execute()
cuentas = response.data

if cuentas:
    for c in cuentas:
        with st.container():
            st.markdown(f"### 🛡️ {c['nombre_cuenta']}")
            st.write(f"**Bróker:** {c['broker']} | **Balance Inicial:** ${c['balance_inicial']:,.2f}")
            st.markdown("---")
else:
    info = st.info("No tienes ninguna cuenta registrada todavía. Añade la primera arriba.")