import streamlit as st
import yfinance as yf
from sentiment_engine import SentimentEngine

# --- PAGE SETUP ---
st.set_page_config(page_title="Global Macro Stress Tracker", layout="wide")

# Custom CSS for perfect alignment
st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] {
        align-items: flex-start !important;
    }
    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #FFFFFF;
        margin-bottom: 10px;
    }
    .section-header {
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
        color: #1E88E5;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">🛡️ Global Macro Stress & Sentiment Model</p>', unsafe_allow_html=True)
st.markdown("---")

engine = SentimentEngine()

def get_market_change(ticker):
    try:
        # Fetching data for S&P Global 1200 or Commodities
        data = yf.Ticker(ticker).history(period="5d")
        if len(data) >= 2:
            prev, curr = data['Close'].iloc[-2], data['Close'].iloc[-1]
            return ((curr - prev) / prev) * 100
    except: pass
    return 0.0

# --- DATA FETCHING ---
with st.spinner('Syncing Global Asset Data...'):
    res = engine.get_scores()
    # UPDATED: S&P Global 1200 Index Ticker
    global_equity_change = get_market_change("^SPV1200") 
    bcom_change = get_market_change("DBC") 

# --- ROW 1: THE THREE MAIN INDICATORS ---
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 📍 1. Weighted Sentiment")
    w_senti = res['weighted_sentiment']
    st.markdown(f"<h1 style='text-align: center; color: #1E88E5; font-size: 50px; margin: 0;'>{w_senti:.4f}</h1>", unsafe_allow_html=True)
    st.progress((w_senti + 1) / 2)
    st.caption("Directional Mood Index (Psychology)")

with c2:
    st.markdown("### ⚠️ 2. News-People Divergence")
    div = res['divergence']
    st.markdown(f"<h1 style='text-align: center; color: #FFA500; font-size: 50px; margin: 0;'>{div:.4f}</h1>", unsafe_allow_html=True)
    st.progress(min(div / 0.5, 1.0))
    st.caption("Friction & Volatility Meter (Conviction)")

with c3:
    st.markdown("### 🛡️ 3. Macro Stress (GMSI)")
    # GMSI Formula using S&P Global 1200 change
    gmsi_score = (0.30 * w_senti) + (0.35 * (bcom_change/100)) - (0.35 * (global_equity_change/100))
    st.markdown(f"<h1 style='text-align: center; color: #FF4B4B; font-size: 50px; margin: 0;'>{gmsi_score:.4f}</h1>", unsafe_allow_html=True)
    st.progress(min(abs(gmsi_score) * 10, 1.0))
    st.caption("Systemic Risk Composite (Global Economy)")

st.markdown("---")

# --- ROW 2: TECHNICAL EXPLANATION ---
st.markdown('<p class="section-header">🔍 Project Intelligence: The Triple Index Model</p>', unsafe_allow_html=True)

col_exp1, col_exp2, col_exp3 = st.columns(3)

with col_exp1:
    st.markdown("#### **Index 1: Weighted Sentiment (WS)**")
    st.latex(r"WS = (News \times 0.35) + (Public \times 0.65)")
    st.write("""
    **The Human Pulse:** Captures digital sentiment from Reddit.
    - **News (r/worldnews):** Global institutional anchor.
    - **Public (r/wallstreetbets):** Retail drive and emotion.
    """)

with col_exp2:
    st.markdown("#### **Index 2: News-People Divergence**")
    st.latex(r"Div = |Avg.News - Avg.Public|")
    st.write(f"""
    **The Friction Meter:** Measures trend conviction.
    - **High Score:** Conflict between headlines and hype.
    - **Low Score:** Stable and aligned market narrative.
    """)

with col_exp3:
    st.markdown("#### **Index 3: Macro Stress (GMSI)**")
    st.latex(r"GMSI = 0.30(WS) + 0.35(BCOM) - 0.35(\Delta Eq)")
    st.write("""
    **The Economic Shield:** Aggregates sentiment with hard assets.
    - Factors in mood, inflation (BCOM), and global equity health.
    """)

st.markdown("---")

# --- ROW 3: VARIABLE GLOSSARY (ALWAYS OPEN) ---
st.markdown('<p class="section-header">📖 Variable Glossary & Technical Definitions</p>', unsafe_allow_html=True)

st.markdown("""
| Variable | Full Name | Technical Description |
| :--- | :--- | :--- |
| **WS** | **Weighted Sentiment** | Composite score from VADER NLP analysis on live Reddit threads. |
| **Div** | **Divergence** | The absolute gap between news facts and retail sentiment. |
| **GMSI** | **Global Macro Stress Indicator** | Proprietary model for measuring multi-asset systemic risk. |
| **BCOM** | **Bloomberg Commodity Index** | Tracked via **DBC ETF**; represents raw material inflation. |
| **$\Delta$Eq** | **Delta Equity (S&P Global 1200)** | Percentage change in the **S&P Global 1200**, covering 70% of world market cap. |
| **VADER** | **Sentiment Model** | Lexical model used for scoring text intensity and polarity. |
""")

if st.sidebar.button('Run Real-Time Macro Scan'):
    st.rerun()