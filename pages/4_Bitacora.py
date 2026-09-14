import streamlit as st
from supabase import create_client, Client
import pandas as pd

st.set_page_config(page_title="Bitácora - Katanith", page_icon="🗡️", layout="wide")

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

st.title("📜 Bitácora de Operaciones")
st.markdown("---")

# Hacemos una consulta a Supabase uniendo trades y cuentas para ver los datos completos
response = supabase.table("trades").select("*, cuentas(nombre_cuenta, broker)").eq("user_id", user_id).order("created_at", desc=True).execute()
trades = response.data

if trades:
    # Convertimos los datos a una tabla limpia para visualizar
    tabla_datos = []
    for t in trades:
        nombre_cta = t["cuentas"]["nombre_cuenta"] if t["cuentas"] else "Cuenta eliminada"
        tabla_datos.append({
            "Fecha": t["created_at"][:10],
            "Cuenta": nombre_cta,
            "Activo": t["activo"],
            "Dirección": t["direccion"],
            "Estrategia": t["estrategia"],
            "Riesgo (%)": t["riesgo_porcentaje"],
            "Resultado (R:R)": t["resultado_rr"],
            "Notas": t["notas"]
        })
    
    df = pd.DataFrame(tabla_datos)
    
    # Métrica rápida superior
    total_trades = len(df)
    win_rate_calc = (df["Resultado (R:R)"] > 0).sum() / total_trades * 100 if total_trades > 0 else 0
    
    col1, col2 = st.columns(2)
    col1.metric("Total de Trades", total_trades)
    col2.metric("Win Rate Aproximado", f"{win_rate_calc:.1f}%")
    
    st.markdown("---")
    
    # Mostramos la tabla interactiva
    st.dataframe(df, use_container_width=True)
    
else:
    st.info("Todavía no hay operaciones registradas. Ve a la sección 'Nuevo Trade' para añadir la primera.")