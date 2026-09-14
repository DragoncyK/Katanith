import streamlit as st
from supabase import create_client

# ============================================================
# 1. CONFIGURACIÓN BÁSICA
# ============================================================
st.set_page_config(page_title="Katanith", page_icon="👑", layout="wide")

# ============================================================
# 2. ESTADO
# ============================================================
if 'user' not in st.session_state: st.session_state.user = None
if 'lang' not in st.session_state: st.session_state.lang = 'en'          # inglés por defecto
if 'current_view' not in st.session_state: st.session_state.current_view = 'home'

L = st.session_state.lang

# ============================================================
# 3. TEXTOS (EN / ES)
# ============================================================
T = {
    "en": {
        "nav_features": "Features",
        "nav_pricing": "Pricing",
        "nav_faq": "FAQ",
        "login": "Log in",
        "signup": "Get Started",
        "logout": "Log out",
        "lang_switch": "ES",
        "hero_badge": "Now in early access",
        "hero_title_a": "Your strategy shouldn't be",
        "hero_title_b": "tested on feelings.",
        "hero_sub": "Katanith is the most effective way to journal, backtest, and analyze your trading edge — all in one clean workspace.",
        "hero_cta_primary": "Get Started Free",
        "hero_cta_secondary": "See features",
        "hero_note": "No credit card required · Free plan available",
        "mockup_side": ["Dashboard", "Journal", "Backtesting", "Copy Trading", "Calendar"],
        "mockup_stats": [("Win Rate", "64.2%", True), ("Profit Factor", "2.14", True), ("Max Drawdown", "-6.8%", False)],
        "steps_kicker": "HOW IT WORKS",
        "steps_title": "From setup to insight in minutes",
        "steps": [
            ("Connect or log manually", "Add your accounts and start logging trades right away — no broker connection required."),
            ("Tag every setup", "Label each trade with the strategy behind it, so patterns become visible over time."),
            ("Review the data", "See win rate, drawdown and profit factor by account or setup, and let the numbers guide your next move."),
        ],
        "cta_title": "Ready to trade with data, not emotions?",
        "cta_sub": "Join the early access and start journaling your edge today.",
        "footer_tagline": "The professional trading journal for prop-firm and personal-capital traders.",
        "footer_col_product": "Product",
        "footer_col_company": "Company",
        "footer_col_legal": "Legal",
        "features_kicker": "FEATURES",
        "features_title": "Everything you need to trade with discipline",
        "features_sub": "Built for prop-firm and personal-capital traders who take their edge seriously.",
        "features": [
            ("📓", "Trading Journal", "Log every trade with notes, screenshots and setups (Order Blocks, FVGs, Turtle Soup) — filter your performance by strategy."),
            ("🛡️", "Account Protection", "Auto-lock an account when it hits stop-loss, and auto-close when it reaches your profit target."),
            ("🔁", "Backtesting", "Replay historical price action and validate your strategy before risking real capital."),
            ("🤝", "Copy Trading", "Mirror trades from a master account to as many secondary accounts as you need, in real time."),
            ("📅", "Economic Calendar", "Never get caught off guard — high-impact news events surface right inside your dashboard."),
            ("📊", "Advanced Analytics", "Win rate, drawdown, profit factor and monthly performance, broken down by account or setup."),
        ],
        "examples_kicker": "BUILT FOR YOU",
        "examples_title": "One workspace, every account",
        "examples": [
            ("Multi-account overview", "Track every prop-firm and personal account side by side, with combined and per-account equity curves."),
            ("Course creators", "Run your own trading course and monitor every student's progress from a single dashboard."),
            ("Data-driven decisions", "Stop guessing. See exactly which setups actually make you money — and which ones don't."),
        ],
        "pricing_kicker": "PRICING",
        "pricing_title": "Simple, transparent pricing",
        "pricing_sub": "Start free. Upgrade whenever you're ready.",
        "plans": [
            {
                "name": "Free",
                "price": "$0",
                "period": "/ forever",
                "desc": "For traders just getting started.",
                "features": ["1 trading account", "Limited backtesting", "Basic journal", "Community support"],
                "cta": "Start for Free",
                "highlight": False,
            },
            {
                "name": "Premium",
                "price": "$4.99",
                "period": "/ month",
                "desc": "For traders who want the full toolkit.",
                "features": ["Unlimited accounts", "Full backtesting suite", "Copy trading", "Economic calendar", "Advanced analytics"],
                "cta": "Choose Premium",
                "highlight": True,
            },
            {
                "name": "Ultimate",
                "price": "$14.99",
                "period": "/ month",
                "desc": "For mentors and course creators.",
                "features": ["Everything in Premium", "Manage & monitor students", "Priority support", "Early access to new features"],
                "cta": "Choose Ultimate",
                "highlight": False,
            },
        ],
        "most_popular": "MOST POPULAR",
        "faq_kicker": "FAQ",
        "faq_title": "Frequently asked questions",
        "faq": [
            ("What is Katanith?", "Katanith is a professional trading journal built for prop-firm and personal-capital traders. It helps you log trades, backtest strategies and track performance by setup, all in one place."),
            ("Do I need to connect my broker?", "No. You can log trades manually, or connect a supported broker later on to automate account tracking and copy trading."),
            ("Is my data safe?", "Yes. Your data is encrypted in transit and at rest, and it's never shared with third parties."),
            ("Can I cancel anytime?", "Yes, you can upgrade, downgrade or cancel your subscription at any time — no lock-in contracts."),
            ("How does copy trading work?", "Connect a master account and any number of secondary accounts. Every trade placed on the master is mirrored automatically in real time."),
        ],
        "footer_rights": "© 2026 Katanith. All rights reserved.",
        "footer_privacy": "Privacy Policy",
        "footer_terms": "Terms of Service",
        "footer_contact": "Contact",
        "login_title": "Log In",
        "signup_title": "Create Account",
        "email": "Email",
        "password": "Password",
        "signin_btn": "Sign In",
        "signup_btn": "Sign Up",
        "no_account": "Don't have an account?",
        "have_account": "Already have an account?",
        "signup_link": "Sign up",
        "login_link": "Log in",
        "login_error": "Invalid credentials",
        "signup_success": "Check your email to confirm your account",
        "welcome": "Welcome back",
        "sidebar_hint": "👈 Open the sidebar to get started",
    },
    "es": {
        "nav_features": "Funciones",
        "nav_pricing": "Precios",
        "nav_faq": "FAQ",
        "login": "Iniciar sesión",
        "signup": "Empezar",
        "logout": "Cerrar sesión",
        "lang_switch": "EN",
        "hero_badge": "Ahora en acceso anticipado",
        "hero_title_a": "Tu estrategia no debería",
        "hero_title_b": "basarse en emociones.",
        "hero_sub": "Katanith es la forma más efectiva de registrar, hacer backtest y analizar tu operativa — todo en un mismo espacio.",
        "hero_cta_primary": "Empieza gratis",
        "hero_cta_secondary": "Ver funciones",
        "hero_note": "Sin tarjeta de crédito · Plan gratuito disponible",
        "mockup_side": ["Dashboard", "Journal", "Backtesting", "Copy Trading", "Calendario"],
        "mockup_stats": [("Win Rate", "64,2%", True), ("Profit Factor", "2,14", True), ("Drawdown Máx.", "-6,8%", False)],
        "steps_kicker": "CÓMO FUNCIONA",
        "steps_title": "De la operación al análisis en minutos",
        "steps": [
            ("Conecta o registra manualmente", "Añade tus cuentas y empieza a registrar operaciones al instante — sin necesidad de conectar un broker."),
            ("Etiqueta cada setup", "Marca cada operación con la estrategia usada, para que los patrones sean visibles con el tiempo."),
            ("Analiza los datos", "Consulta win rate, drawdown y profit factor por cuenta o por setup, y deja que los números guíen tu siguiente decisión."),
        ],
        "cta_title": "¿Listo para operar con datos, no con emociones?",
        "cta_sub": "Únete al acceso anticipado y empieza a registrar tu operativa hoy mismo.",
        "footer_tagline": "El journal de trading profesional para traders de firmas de fondeo y capital propio.",
        "footer_col_product": "Producto",
        "footer_col_company": "Empresa",
        "footer_col_legal": "Legal",
        "features_kicker": "FUNCIONES",
        "features_title": "Todo lo que necesitas para operar con disciplina",
        "features_sub": "Diseñado para traders de firmas de fondeo y capital propio que se toman en serio su operativa.",
        "features": [
            ("📓", "Journal de Trading", "Registra cada operación con notas, capturas y setups (Order Blocks, FVG, Turtle Soup) — filtra tu rendimiento por estrategia."),
            ("🛡️", "Protección de Cuentas", "Bloquea la cuenta automáticamente al llegar al stop loss, y ciérrala al alcanzar tu objetivo de profit."),
            ("🔁", "Backtesting", "Repasa movimientos históricos y valida tu estrategia antes de arriesgar capital real."),
            ("🤝", "Copy Trading", "Copia las operaciones de una cuenta principal a tantas cuentas secundarias como necesites, en tiempo real."),
            ("📅", "Calendario Económico", "No te pille por sorpresa — las noticias de alto impacto aparecen directamente en tu panel."),
            ("📊", "Analítica Avanzada", "Win rate, drawdown, profit factor y rendimiento mensual, desglosados por cuenta o por setup."),
        ],
        "examples_kicker": "PENSADO PARA TI",
        "examples_title": "Un solo espacio, todas tus cuentas",
        "examples": [
            ("Vista de múltiples cuentas", "Controla cada cuenta de fondeo y personal a la vez, con curvas de equity combinadas e individuales."),
            ("Formadores de trading", "Dirige tu propio curso de trading y supervisa el progreso de cada alumno desde un único panel."),
            ("Decisiones basadas en datos", "Deja de adivinar. Ve exactamente qué setups te dan dinero de verdad — y cuáles no."),
        ],
        "pricing_kicker": "PRECIOS",
        "pricing_title": "Precios simples y transparentes",
        "pricing_sub": "Empieza gratis. Mejora tu plan cuando quieras.",
        "plans": [
            {
                "name": "Gratis",
                "price": "0€",
                "period": "/ para siempre",
                "desc": "Para traders que están empezando.",
                "features": ["1 cuenta de trading", "Backtesting limitado", "Journal básico", "Soporte de la comunidad"],
                "cta": "Empezar gratis",
                "highlight": False,
            },
            {
                "name": "Premium",
                "price": "4,99€",
                "period": "/ mes",
                "desc": "Para traders que quieren todo el potencial.",
                "features": ["Cuentas ilimitadas", "Backtesting completo", "Copy trading", "Calendario económico", "Analítica avanzada"],
                "cta": "Elegir Premium",
                "highlight": True,
            },
            {
                "name": "Definitivo",
                "price": "14,99€",
                "period": "/ mes",
                "desc": "Para mentores y formadores de trading.",
                "features": ["Todo lo de Premium", "Gestión y control de alumnos", "Soporte prioritario", "Acceso anticipado a nuevas funciones"],
                "cta": "Elegir Definitivo",
                "highlight": False,
            },
        ],
        "most_popular": "MÁS POPULAR",
        "faq_kicker": "FAQ",
        "faq_title": "Preguntas frecuentes",
        "faq": [
            ("¿Qué es Katanith?", "Katanith es un journal de trading profesional pensado para traders de firmas de fondeo y capital propio. Te ayuda a registrar operaciones, hacer backtest y medir tu rendimiento por setup, todo en un mismo sitio."),
            ("¿Necesito conectar mi broker?", "No. Puedes registrar tus operaciones manualmente, o conectar un broker compatible más adelante para automatizar el seguimiento y el copy trading."),
            ("¿Están seguros mis datos?", "Sí. Tus datos están cifrados en tránsito y en reposo, y nunca se comparten con terceros."),
            ("¿Puedo cancelar cuando quiera?", "Sí, puedes mejorar, bajar de plan o cancelar tu suscripción cuando quieras, sin permanencia."),
            ("¿Cómo funciona el copy trading?", "Conecta una cuenta principal y tantas cuentas secundarias como necesites. Cada operación de la cuenta principal se copia automáticamente en tiempo real."),
        ],
        "footer_rights": "© 2026 Katanith. Todos los derechos reservados.",
        "footer_privacy": "Política de Privacidad",
        "footer_terms": "Términos del Servicio",
        "footer_contact": "Contacto",
        "login_title": "Iniciar Sesión",
        "signup_title": "Crear Cuenta",
        "email": "Email",
        "password": "Contraseña",
        "signin_btn": "Entrar",
        "signup_btn": "Registrarse",
        "no_account": "¿No tienes cuenta?",
        "have_account": "¿Ya tienes cuenta?",
        "signup_link": "Regístrate",
        "login_link": "Inicia sesión",
        "login_error": "Credenciales incorrectas",
        "signup_success": "Revisa tu correo para confirmar tu cuenta",
        "welcome": "Bienvenido de nuevo",
        "sidebar_hint": "👈 Despliega el menú lateral para empezar",
    },
}
t = T[L]

# ============================================================
# 4. CSS
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    :root {
        --bg: #0a0a0c;
        --bg-elevated: #111114;
        --border: #1f1f24;
        --text: #f2f2f5;
        --text-muted: #9a9aa3;
        --blue: #0A84FF;
        --blue-hover: #2f9bff;
        --nav-height: 76px;
    }

    html { scroll-behavior: smooth; }

    html, body, [class*="css"], .stApp, .stMarkdown, p, span, div, button {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Neutralise any ancestor property that would create a new "containing block"
       (transform/filter/perspective) — otherwise a fixed-position navbar gets trapped
       inside Streamlit's own wrapper divs instead of the real browser viewport. */
    [data-testid="stApp"],
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    section.main,
    .main,
    .block-container,
    [data-testid="stVerticalBlock"],
    [data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stHorizontalBlock"],
    [data-testid="element-container"] {
        transform: none !important;
        perspective: none !important;
    }

    #MainMenu, header, footer {visibility: hidden;}
    [data-testid="collapsedControl"] {display: none;}
    [data-testid="stSidebar"] {display: none;}

    .stApp {
        background:
            radial-gradient(circle at 15% 0%, rgba(10,132,255,0.10), transparent 45%),
            radial-gradient(circle at 85% 15%, rgba(10,132,255,0.06), transparent 40%),
            repeating-linear-gradient(0deg, rgba(255,255,255,0.025) 0px, rgba(255,255,255,0.025) 1px, transparent 1px, transparent 64px),
            repeating-linear-gradient(90deg, rgba(255,255,255,0.025) 0px, rgba(255,255,255,0.025) 1px, transparent 1px, transparent 64px),
            #0a0a0c;
        background-attachment: fixed;
    }

    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        max-width: 1200px;
    }

    /* ---- Navbar: fixed, edge-to-edge, inner content aligned to a centered max-width ---- */
    .st-key-navbar {
        position: fixed !important;
        top: 0; left: 0; right: 0;
        width: 100%;
        height: var(--nav-height);
        z-index: 999;
        background: rgba(9, 9, 11, 0.72);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-bottom: 1px solid var(--border);
        box-shadow: 0 8px 30px -18px rgba(0,0,0,0.6);
        padding: 0 !important;
        margin: 0 !important;
        display: flex;
        align-items: center;
    }
    /* Inner wrapper Streamlit generates inside the keyed container: center it like the rest of the page */
    .st-key-navbar > div {
        width: 100%;
        max-width: 1240px;
        margin: 0 auto;
        padding: 0 2rem;
    }
    .st-key-navbar [data-testid="stHorizontalBlock"] { align-items: center; }

    /* Spacer so page content clears the fixed navbar */
    .nav-spacer { height: var(--nav-height); }

    .nav-logo { color: #fff !important; font-size: 1.2rem; font-weight: 800; letter-spacing: -0.02em; display: flex; align-items: center; gap: 0.4rem; }
    .nav-links-wrap { display: flex; align-items: center; height: 100%; gap: 0.4rem; }
    a.nav-link {
        color: var(--text-muted) !important;
        text-decoration: none !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        padding: 0.5rem 0.85rem;
        border-radius: 7px;
        transition: color 0.15s ease, background-color 0.15s ease;
    }
    a.nav-link:hover { color: #fff !important; background-color: rgba(255,255,255,0.06); }

    /* ---- Buttons ---- */
    div[data-testid="stButton"] > button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        transition: all 0.15s ease !important;
        line-height: 1.2 !important;
    }
    button[kind="primary"] {
        background-color: var(--blue) !important;
        border: 1px solid var(--blue) !important;
        color: white !important;
        padding: 0.5rem 1.2rem !important;
        box-shadow: 0 4px 16px -4px rgba(10,132,255,0.55);
    }
    button[kind="primary"]:hover {
        background-color: var(--blue-hover) !important;
        border-color: var(--blue-hover) !important;
        box-shadow: 0 6px 20px -4px rgba(10,132,255,0.7);
    }
    /* Ghost / secondary buttons look like real (but subtle) buttons, not bare text */
    button[kind="secondary"] {
        background-color: transparent !important;
        border: 1px solid var(--border) !important;
        color: var(--text-muted) !important;
        padding: 0.5rem 1rem !important;
    }
    button[kind="secondary"]:hover {
        color: #fff !important;
        border-color: #3a3a42 !important;
        background-color: rgba(255,255,255,0.06) !important;
    }
    /* Small ghost buttons used inline in the navbar (lang switch, log in) */
    .st-key-navbar button[kind="secondary"] {
        border-color: transparent !important;
        padding: 0.5rem 0.9rem !important;
    }
    .st-key-navbar button[kind="secondary"]:hover {
        border-color: var(--border) !important;
    }

    /* ---- Hero ---- */
    .hero-wrap { padding: 4.5rem 1rem 4rem 1rem; text-align: center; }
    .hero-badge {
        display: inline-block;
        color: var(--blue);
        background: rgba(10,132,255,0.12);
        border: 1px solid rgba(10,132,255,0.35);
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        margin-bottom: 1.6rem;
    }
    .hero-title {
        font-size: 3.2rem;
        line-height: 1.15;
        font-weight: 800;
        letter-spacing: -0.03em;
        color: var(--text);
        margin: 0 auto 1.3rem auto;
        max-width: 780px;
    }
    .hero-title .accent {
        background: linear-gradient(90deg, #0A84FF, #5cc7ff);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }
    .hero-sub {
        color: var(--text-muted);
        font-size: 1.12rem;
        max-width: 620px;
        margin: 0 auto 2.2rem auto;
        line-height: 1.55;
    }
    .hero-note { color: #6f6f78; font-size: 0.82rem; margin-top: 1rem; }
    .trust-bar {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0.6rem 2.2rem;
        margin-top: 2.6rem;
    }
    .trust-item { color: var(--text-muted); font-size: 0.85rem; font-weight: 500; }
    .trust-item::before { content: none; }

    /* ---- Product mockup (pure CSS, no real screenshot) ---- */
    .mockup-wrap { max-width: 980px; margin: 3.5rem auto 0 auto; padding: 0 1rem; }
    .mockup-window {
        border: 1px solid var(--border);
        border-radius: 14px;
        overflow: hidden;
        background: #0d0d10;
        box-shadow: 0 30px 80px -30px rgba(0,0,0,0.7), 0 0 0 1px rgba(255,255,255,0.02);
    }
    .mockup-titlebar {
        display: flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.7rem 1rem;
        border-bottom: 1px solid var(--border);
        background: #111114;
    }
    .mockup-dot { width: 10px; height: 10px; border-radius: 50%; background: #33333a; }
    .mockup-body { display: grid; grid-template-columns: 190px 1fr; min-height: 320px; }
    .mockup-sidebar { border-right: 1px solid var(--border); padding: 1.2rem 0.9rem; }
    .mockup-side-item {
        color: var(--text-muted);
        font-size: 0.82rem;
        font-weight: 600;
        padding: 0.55rem 0.7rem;
        border-radius: 7px;
        margin-bottom: 0.3rem;
    }
    .mockup-side-item.active { color: #fff; background: rgba(10,132,255,0.14); }
    .mockup-main { padding: 1.4rem; }
    .mockup-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.8rem; margin-bottom: 1.2rem; }
    .mockup-stat { border: 1px solid var(--border); border-radius: 10px; padding: 0.8rem 0.9rem; background: rgba(255,255,255,0.02); }
    .mockup-stat-label { color: var(--text-muted); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.3rem; }
    .mockup-stat-value { color: #fff; font-size: 1.15rem; font-weight: 800; }
    .mockup-stat-value.up { color: #34d399; }
    .mockup-chart {
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 1rem;
        display: flex;
        align-items: flex-end;
        gap: 0.5rem;
        height: 120px;
        background: rgba(255,255,255,0.015);
    }
    .mockup-bar { flex: 1; background: linear-gradient(180deg, #2f9bff, #0A84FF); border-radius: 4px 4px 0 0; opacity: 0.85; }

    /* ---- How it works ---- */
    .steps-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.4rem;
        max-width: 1000px;
        margin: 0 auto;
        position: relative;
    }
    .step-card { text-align: center; padding: 0 0.5rem; }
    .step-number {
        width: 42px; height: 42px;
        border-radius: 50%;
        border: 1px solid rgba(10,132,255,0.4);
        background: rgba(10,132,255,0.1);
        color: var(--blue);
        font-weight: 800;
        font-size: 1rem;
        display: flex; align-items: center; justify-content: center;
        margin: 0 auto 1rem auto;
    }
    .step-title { color: #fff; font-weight: 700; font-size: 1.02rem; margin-bottom: 0.5rem; }
    .step-desc { color: var(--text-muted); font-size: 0.9rem; line-height: 1.55; max-width: 260px; margin: 0 auto; }

    /* ---- Final CTA banner ---- */
    .cta-banner {
        max-width: 1000px;
        margin: 0 auto;
        border: 1px solid rgba(10,132,255,0.35);
        border-radius: 18px;
        padding: 3rem 2rem;
        text-align: center;
        background:
            radial-gradient(circle at 30% 0%, rgba(10,132,255,0.16), transparent 60%),
            rgba(255,255,255,0.02);
    }
    .cta-title { color: #fff; font-size: 1.7rem; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 0.6rem; }
    .cta-sub { color: var(--text-muted); font-size: 0.98rem; margin-bottom: 1.6rem; }

    /* ---- Section shells ---- */
    .section { padding: 4.5rem 1rem; }
    .section-kicker {
        text-align: center;
        color: var(--blue);
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        margin-bottom: 0.8rem;
    }
    .section-title {
        text-align: center;
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: var(--text);
        margin-bottom: 0.7rem;
    }
    .section-sub {
        text-align: center;
        color: var(--text-muted);
        font-size: 1rem;
        max-width: 560px;
        margin: 0 auto 3rem auto;
    }
    .section-divider { border: none; border-top: 1px solid var(--border); margin: 0; }

    /* ---- Feature grid ---- */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.1rem;
        max-width: 1100px;
        margin: 0 auto;
    }
    .feature-card {
        background: rgba(255,255,255,0.02);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.6rem;
        transition: border-color 0.15s ease, transform 0.15s ease;
    }
    .feature-card:hover { border-color: rgba(10,132,255,0.4); transform: translateY(-2px); }
    .feature-icon { font-size: 1.6rem; margin-bottom: 0.8rem; }
    .feature-title { color: #fff; font-weight: 700; font-size: 1.02rem; margin-bottom: 0.4rem; }
    .feature-desc { color: var(--text-muted); font-size: 0.9rem; line-height: 1.5; }

    /* ---- Examples ---- */
    .example-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.1rem;
        max-width: 1100px;
        margin: 0 auto;
    }
    .example-card {
        background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.00));
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.8rem;
        min-height: 150px;
    }
    .example-title { color: #fff; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; }
    .example-desc { color: var(--text-muted); font-size: 0.9rem; line-height: 1.55; }

    /* ---- Pricing cards (container-key based) ---- */
    div[class*="st-key-plan_"] {
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 1.8rem 1.6rem 1.6rem 1.6rem !important;
        background: rgba(255,255,255,0.02);
        height: 100%;
    }
    .st-key-plan_premium {
        border: 1px solid var(--blue) !important;
        background: rgba(10,132,255,0.06) !important;
        box-shadow: 0 0 0 1px rgba(10,132,255,0.25), 0 12px 30px -12px rgba(10,132,255,0.35);
    }
    .plan-badge {
        display: inline-block;
        color: var(--blue);
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        margin-bottom: 0.6rem;
    }
    .plan-name { color: #fff; font-size: 1.15rem; font-weight: 700; margin-bottom: 0.3rem; }
    .plan-desc { color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1.1rem; min-height: 34px; }
    .plan-price { color: #fff; font-size: 2.1rem; font-weight: 800; }
    .plan-period { color: var(--text-muted); font-size: 0.85rem; }
    .plan-features { list-style: none; padding: 0; margin: 1.2rem 0 1.3rem 0; }
    .plan-features li {
        color: var(--text);
        font-size: 0.88rem;
        padding: 0.35rem 0;
        border-top: 1px solid var(--border);
    }
    .plan-features li:first-child { border-top: none; }
    .plan-features li::before { content: "✓  "; color: var(--blue); font-weight: 700; }

    /* ---- FAQ ---- */
    div[data-testid="stExpander"] {
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        background: rgba(255,255,255,0.02) !important;
        margin-bottom: 0.6rem;
    }
    div[data-testid="stExpander"] summary { color: var(--text) !important; font-weight: 600 !important; }
    div[data-testid="stExpander"] p { color: var(--text-muted) !important; }

    /* ---- Footer ---- */
    .footer-wrap {
        border-top: 1px solid var(--border);
        padding: 3.5rem 1.5rem 2rem 1.5rem;
        margin-top: 1rem;
    }
    .footer-top {
        max-width: 1100px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1.6fr 1fr 1fr 1fr;
        gap: 2rem;
        padding-bottom: 2.2rem;
    }
    .footer-brand { color: #fff; font-size: 1.05rem; font-weight: 800; margin-bottom: 0.6rem; }
    .footer-tagline { color: var(--text-muted); font-size: 0.86rem; line-height: 1.55; max-width: 260px; }
    .footer-col-title { color: #fff; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.06em; margin-bottom: 0.9rem; text-transform: uppercase; }
    .footer-col a {
        display: block;
        color: var(--text-muted);
        text-decoration: none;
        font-size: 0.87rem;
        margin-bottom: 0.65rem;
        transition: color 0.15s ease;
    }
    .footer-col a:hover { color: #fff; }
    .footer-bottom {
        max-width: 1100px;
        margin: 0 auto;
        border-top: 1px solid var(--border);
        padding-top: 1.4rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
    }
    .footer-rights { color: #6f6f78; font-size: 0.82rem; }
    .footer-legal a {
        color: #6f6f78;
        text-decoration: none;
        font-size: 0.82rem;
        margin-left: 1.3rem;
    }
    .footer-legal a:hover { color: var(--text-muted); }

    /* ---- Auth forms ---- */
    .st-key-auth_card {
        border: 1px solid var(--border);
        border-radius: 14px;
        background: rgba(255,255,255,0.02);
        padding: 2.2rem 2rem !important;
        margin-top: 1rem;
    }
    .auth-title { color: #fff; font-size: 1.6rem; font-weight: 800; margin-bottom: 1.4rem; text-align: center; }
    .auth-switch { text-align: center; color: var(--text-muted); font-size: 0.88rem; margin-top: 1rem; }

    @media (max-width: 900px) {
        .feature-grid, .example-grid, .steps-grid { grid-template-columns: 1fr; }
        .hero-title { font-size: 2.2rem; }
        .mockup-body { grid-template-columns: 1fr; }
        .mockup-sidebar { display: none; }
        .footer-top { grid-template-columns: 1fr 1fr; }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# 5. BASE DE DATOS
# ============================================================
@st.cache_resource
def init_connection():
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

supabase = init_connection()

# ============================================================
# 6. NAVBAR
# ============================================================
with st.container(key="navbar"):
    col_logo, col_links, col_lang, col_login, col_cta = st.columns([2, 4, 0.8, 1.1, 1.3])

    with col_logo:
        st.markdown('<div class="nav-logo">👑 Katanith</div>', unsafe_allow_html=True)

    with col_links:
        if st.session_state.current_view == 'home' and not st.session_state.user:
            st.markdown(
                f"""<div class="nav-links-wrap">
                        <a class="nav-link" href="#features">{t['nav_features']}</a>
                        <a class="nav-link" href="#pricing">{t['nav_pricing']}</a>
                        <a class="nav-link" href="#faq">{t['nav_faq']}</a>
                    </div>""",
                unsafe_allow_html=True,
            )

    with col_lang:
        if st.button(t["lang_switch"], key="lang_toggle"):
            st.session_state.lang = 'es' if st.session_state.lang == 'en' else 'en'
            st.rerun()

    if st.session_state.user:
        with col_login:
            st.markdown(
                f"<div style='color:#9a9aa3; text-align:right; padding-top:8px; font-size:0.88rem;'>"
                f"{st.session_state.user.email.split('@')[0]}</div>",
                unsafe_allow_html=True,
            )
        with col_cta:
            if st.button(t["logout"], type="primary", key="logout_btn"):
                supabase.auth.sign_out()
                st.session_state.user = None
                st.session_state.current_view = 'home'
                st.rerun()
    else:
        with col_login:
            if st.button(t["login"], key="login_nav_btn"):
                st.session_state.current_view = 'login'
                st.rerun()
        with col_cta:
            if st.button(t["signup"], type="primary", key="signup_nav_btn"):
                st.session_state.current_view = 'signup'
                st.rerun()

# Espaciador para compensar que la navbar ahora es "fixed" (fuera del flujo normal)
st.markdown('<div class="nav-spacer"></div>', unsafe_allow_html=True)

# ============================================================
# 7. LANDING PAGE
# ============================================================
if st.session_state.current_view == 'home' and not st.session_state.user:

    # --- Hero ---
    st.markdown(
        f"""
        <div class="hero-wrap">
            <div class="hero-badge">{t['hero_badge']}</div>
            <div class="hero-title">{t['hero_title_a']}<br><span class="accent">{t['hero_title_b']}</span></div>
            <div class="hero-sub">{t['hero_sub']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _, c1, c2, _ = st.columns([3, 1.3, 1.3, 3])
    with c1:
        if st.button(t["hero_cta_primary"], type="primary", key="hero_cta_primary", use_container_width=True):
            st.session_state.current_view = 'signup'
            st.rerun()
    with c2:
        st.markdown(
            f'<a class="nav-link" style="border:1px solid var(--border); border-radius:8px; '
            f'padding:0.5rem 1.1rem; display:inline-block; width:100%; box-sizing:border-box; '
            f'text-align:center; font-weight:600;" href="#features">{t["hero_cta_secondary"]}</a>',
            unsafe_allow_html=True,
        )
    st.markdown(f"<div style='text-align:center;'><span class='hero-note'>{t['hero_note']}</span></div>", unsafe_allow_html=True)

    trust_html = "".join(f"<div class='trust-item'>✓ {label}</div>" for _, label, _ in t["features"][:3])
    st.markdown(f"<div class='trust-bar'>{trust_html}</div>", unsafe_allow_html=True)

    # --- Product mockup (pure CSS/HTML, no external image) ---
    side_html = "".join(
        f"<div class='mockup-side-item{' active' if i == 0 else ''}'>{item}</div>"
        for i, item in enumerate(t["mockup_side"])
    )
    stats_html = "".join(
        f"""<div class="mockup-stat">
                <div class="mockup-stat-label">{label}</div>
                <div class="mockup-stat-value{' up' if up else ''}">{value}</div>
            </div>"""
        for label, value, up in t["mockup_stats"]
    )
    bar_heights = [38, 55, 42, 70, 60, 85, 66, 92, 78, 100, 88, 96]
    bars_html = "".join(f"<div class='mockup-bar' style='height:{h}%;'></div>" for h in bar_heights)
    st.markdown(
        f"""
        <div class="mockup-wrap">
            <div class="mockup-window">
                <div class="mockup-titlebar">
                    <div class="mockup-dot"></div><div class="mockup-dot"></div><div class="mockup-dot"></div>
                </div>
                <div class="mockup-body">
                    <div class="mockup-sidebar">{side_html}</div>
                    <div class="mockup-main">
                        <div class="mockup-stats">{stats_html}</div>
                        <div class="mockup-chart">{bars_html}</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<hr class='section-divider' style='margin-top:4rem;'>", unsafe_allow_html=True)

    # --- Features ---
    st.markdown('<div id="features"></div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="section">
            <div class="section-kicker">{t['features_kicker']}</div>
            <div class="section-title">{t['features_title']}</div>
            <div class="section-sub">{t['features_sub']}</div>
            <div class="feature-grid">
        """,
        unsafe_allow_html=True,
    )
    cards_html = "".join(
        f"""<div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-desc">{desc}</div>
            </div>"""
        for icon, title, desc in t["features"]
    )
    st.markdown(cards_html + "</div></div>", unsafe_allow_html=True)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # --- Examples / use cases ---
    st.markdown(
        f"""
        <div class="section">
            <div class="section-kicker">{t['examples_kicker']}</div>
            <div class="section-title">{t['examples_title']}</div>
            <div class="example-grid">
        """,
        unsafe_allow_html=True,
    )
    ex_html = "".join(
        f"""<div class="example-card">
                <div class="example-title">{title}</div>
                <div class="example-desc">{desc}</div>
            </div>"""
        for title, desc in t["examples"]
    )
    st.markdown(ex_html + "</div></div>", unsafe_allow_html=True)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # --- How it works ---
    st.markdown(
        f"""
        <div class="section" style="padding-bottom:2rem;">
            <div class="section-kicker">{t['steps_kicker']}</div>
            <div class="section-title">{t['steps_title']}</div>
            <div class="steps-grid">
        """,
        unsafe_allow_html=True,
    )
    steps_html = "".join(
        f"""<div class="step-card">
                <div class="step-number">{i+1}</div>
                <div class="step-title">{title}</div>
                <div class="step-desc">{desc}</div>
            </div>"""
        for i, (title, desc) in enumerate(t["steps"])
    )
    st.markdown(steps_html + "</div></div>", unsafe_allow_html=True)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # --- Pricing ---
    st.markdown('<div id="pricing"></div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="section" style="padding-bottom:2rem;">
            <div class="section-kicker">{t['pricing_kicker']}</div>
            <div class="section-title">{t['pricing_title']}</div>
            <div class="section-sub">{t['pricing_sub']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    price_cols = st.columns(3, gap="medium")
    plan_keys = ["plan_free", "plan_premium", "plan_ultimate"]
    for col, plan, key in zip(price_cols, t["plans"], plan_keys):
        with col:
            with st.container(key=key):
                badge = f'<div class="plan-badge">{t["most_popular"]}</div>' if plan["highlight"] else ""
                features_li = "".join(f"<li>{f}</li>" for f in plan["features"])
                st.markdown(
                    f"""
                    {badge}
                    <div class="plan-name">{plan['name']}</div>
                    <div class="plan-desc">{plan['desc']}</div>
                    <span class="plan-price">{plan['price']}</span>
                    <span class="plan-period">{plan['period']}</span>
                    <ul class="plan-features">{features_li}</ul>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button(plan["cta"], type="primary" if plan["highlight"] else "secondary",
                             key=f"{key}_cta", use_container_width=True):
                    st.session_state.current_view = 'signup'
                    st.rerun()

    st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # --- FAQ ---
    st.markdown('<div id="faq"></div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="section" style="padding-bottom:2rem;">
            <div class="section-kicker">{t['faq_kicker']}</div>
            <div class="section-title">{t['faq_title']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    _, faq_col, _ = st.columns([1, 3, 1])
    with faq_col:
        for q, a in t["faq"]:
            with st.expander(q):
                st.write(a)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)

    # --- Final CTA banner ---
    st.markdown('<div class="section" style="padding-top:1rem;">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="cta-banner">
            <div class="cta-title">{t['cta_title']}</div>
            <div class="cta-sub">{t['cta_sub']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    _, cta_col, _ = st.columns([2, 1.2, 2])
    with cta_col:
        if st.button(t["hero_cta_primary"], type="primary", key="cta_banner_btn", use_container_width=True):
            st.session_state.current_view = 'signup'
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Footer ---
    footer_product_links = f"""
        <a href="#features">{t['nav_features']}</a>
        <a href="#pricing">{t['nav_pricing']}</a>
    """
    footer_company_links = f"""
        <a href="#">{t['footer_contact']}</a>
        <a href="#faq">{t['nav_faq']}</a>
    """
    footer_legal_links = f"""
        <a href="#">{t['footer_privacy']}</a>
        <a href="#">{t['footer_terms']}</a>
    """
    st.markdown(
        f"""
        <div class="footer-wrap">
            <div class="footer-top">
                <div>
                    <div class="footer-brand">👑 Katanith</div>
                    <div class="footer-tagline">{t['footer_tagline']}</div>
                </div>
                <div class="footer-col">
                    <div class="footer-col-title">{t['footer_col_product']}</div>
                    {footer_product_links}
                </div>
                <div class="footer-col">
                    <div class="footer-col-title">{t['footer_col_company']}</div>
                    {footer_company_links}
                </div>
                <div class="footer-col">
                    <div class="footer-col-title">{t['footer_col_legal']}</div>
                    {footer_legal_links}
                </div>
            </div>
            <div class="footer-bottom">
                <div class="footer-rights">{t['footer_rights']}</div>
                <div class="footer-legal">
                    <a href="#">{t['footer_privacy']}</a>
                    <a href="#">{t['footer_terms']}</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# 8. LOGIN / SIGNUP
# ============================================================
elif st.session_state.current_view in ['login', 'signup']:
    st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)
    _, center_col, _ = st.columns([1, 1.3, 1])
    with center_col:
        with st.container(key="auth_card"):
            if st.session_state.current_view == 'login':
                st.markdown(f"<div class='auth-title'>{t['login_title']}</div>", unsafe_allow_html=True)
                email = st.text_input(t["email"], key="login_email")
                password = st.text_input(t["password"], type="password", key="login_password")

                if st.button(t["signin_btn"], type="primary", use_container_width=True, key="signin_submit"):
                    try:
                        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                        st.session_state.user = res.user
                        st.session_state.current_view = 'home'
                        st.rerun()
                    except Exception:
                        st.error(t["login_error"])

                st.markdown(f"<div class='auth-switch'>{t['no_account']}</div>", unsafe_allow_html=True)
                if st.button(t["signup_link"], key="switch_to_signup", use_container_width=True):
                    st.session_state.current_view = 'signup'
                    st.rerun()

            else:
                st.markdown(f"<div class='auth-title'>{t['signup_title']}</div>", unsafe_allow_html=True)
                email = st.text_input(t["email"], key="signup_email")
                password = st.text_input(t["password"], type="password", key="signup_password")

                if st.button(t["signup_btn"], type="primary", use_container_width=True, key="signup_submit"):
                    try:
                        supabase.auth.sign_up({"email": email, "password": password})
                        st.success(t["signup_success"])
                    except Exception as e:
                        st.error(str(e))

                st.markdown(f"<div class='auth-switch'>{t['have_account']}</div>", unsafe_allow_html=True)
                if st.button(t["login_link"], key="switch_to_login", use_container_width=True):
                    st.session_state.current_view = 'login'
                    st.rerun()

# ============================================================
# 9. DASHBOARD (usuario logueado)
# ============================================================
if st.session_state.user:
    st.markdown(
        """<style>[data-testid="collapsedControl"] {display: block;} [data-testid="stSidebar"] {display: block;}</style>""",
        unsafe_allow_html=True,
    )
    st.title(t["welcome"])
    st.write(t["sidebar_hint"])