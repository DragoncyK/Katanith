import streamlit as st
from supabase import create_client, Client

st.set_page_config(page_title="Nuevo Trade - Katanith", page_icon="🗡️", layout="wide")

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

st.title("📊 Registrar Nueva Operación")
st.markdown("---")

# 1. Cargamos las cuentas del usuario para el selector
cuentas_res = supabase.table("cuentas").select("id, nombre_cuenta").eq("user_id", user_id).execute()
cuentas_disponibles = cuentas_res.data

if not cuentas_disponibles:
    st.warning("⚠️ Primero debes registrar al menos una cuenta en la sección de 'Cuentas' antes de meter trades.")
    st.stop()

# Creamos un diccionario para mapear el nombre bonito con el ID de Supabase
nombres_cuentas = {c["nombre_cuenta"]: c["id"] for c in cuentas_disponibles}

with st.form("form_trade"):
    col1, col2 = st.columns(2)
    
    with col1:
        cuenta_seleccionada_nombre = st.selectbox("Seleccionar Cuenta", options=list(nombres_cuentas.keys()))
        activo = st.text_input("Activo (ej. XAU/USD, EUR/USD)")
        direccion = st.radio("Dirección", ["Long (Compra)", "Short (Venta)"])
        riesgo = st.number_input("Riesgo asumido (%)", value=0.5, step=0.1)
        
    with col2:
        estrategia = st.selectbox("Estrategia / Setup", 
                                  ["Order Block", "Fair Value Gap (FVG)", "Turtle Soup", "Candle Range Theory", "Smart Money Concepts", "Otro"])
        resultado = st.number_input("Resultado (Ratio R:R, ej. 2.5 o -1.0)", value=0.0, step=0.1)
        
    notas = st.text_area("Notas del trade (Confluencias, estado psicológico, errores...)")
    
    submit_trade = st.form_submit_button("Guardar Operación en el Journal")
    
    if submit_trade:
        cuenta_id_real = nombres_cuentas[cuenta_seleccionada_nombre]
        if activo:
            data = {
                "user_id": user_id,
                "cuenta_id": cuenta_id_real,
                "activo": activo.upper(),
                "direccion": direccion,
                "estrategia": estrategia,
                "riesgo_porcentaje": riesgo,
                "resultado_rr": resultado,
                "notas": notas
            }
            supabase.table("trades").insert(data).execute()
            st.success("¡Operación registrada con éxito en tu bitácora!")
        else:
            st.error("Por favor, introduce al menos el activo operado.")