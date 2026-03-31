# 🛡️ Global Macro Stress & Sentiment Model (GMSI)

An advanced **Quantitative Macro-Financial Dashboard** that synchronizes real-time social sentiment with global asset performance to measure systemic market risk.

---

## 🚀 Overview
The **Global Macro Stress Model** is built for the modern, high-frequency financial landscape. It moves beyond traditional lagging indicators by scraping raw human emotion from **Reddit** and combining it with the performance of **Global Equities** and **Commodities**.

This project identifies **"Narrative Friction"**—the gap between institutional news and retail action—to predict market reversals and systemic stress levels.

---

## 🛠️ Technical Architecture

### **1. Data Sources**
* **Institutional News:** Scraped from `r/worldnews` (Global geopolitical anchor).
* **Retail Sentiment:** Scraped from `r/wallstreetbets` (High-volatility retail pulse).
* **Equity Markets:** Real-time data from **S&P Global 1200 (`^SPV1200`)** via Yahoo Finance.
* **Commodity Markets:** Real-time data from **DBC ETF** (Proxy for the Bloomberg Commodity Index).

### **2. The Sentiment Engine (VADER)**
We utilize the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** NLP model. VADER is specifically tuned for social media syntax (emojis, slang, and capitalization), providing a **Compound Score** between:
* **-1.0:** Extreme Panic/Fear
* **0.0:** Neutral
* **+1.0:** Extreme Euphoria

---

## 📊 Mathematical Framework (The Formulas)

The dashboard calculates three proprietary indices in real-time:

### **A. Weighted Sentiment Index (WS)**
Captures the "Digital Vibe" by balancing institutional facts against retail momentum.
$$WS = (\text{Avg. WorldNews} \times 0.35) + (\text{Avg. WSB} \times 0.65)$$
* **Logic:** We assign a higher weight (65%) to retail sentiment as modern market liquidity is heavily driven by social media trends and collective retail behavior.

### **B. News-People Divergence (Div)**
Measures the conviction of a trend. It identifies if the news and the crowd are in harmony or conflict.
$$\text{Divergence} = | \text{Avg. News Score} - \text{Avg. Public Score} |$$
* **Insight:** High Divergence ($> 0.28$) indicates a "Narrative Conflict," signaling imminent volatility or a sharp market reversal.

### **C. Global Macro Stress Indicator (GMSI)**
The ultimate systemic risk score combining psychology with hard assets.
$$\text{GMSI} = 0.30(WS) + 0.35(\text{BCOM}) - 0.35(\Delta \text{Eq})$$
* **$\Delta$Eq Relationship:** We subtract Equity change because a falling market (negative change) increases the overall "Stress" score.
* **BCOM Relationship:** High commodity prices (inflationary pressure) add to the macro stress.

---

## 📖 Variable Glossary

| Variable | Full Name | Technical Description |
| :--- | :--- | :--- |
| **WS** | **Weighted Sentiment** | The primary direction of the market mood (-1 to +1). |
| **Div** | **Divergence** | The "Stress Gap" between headlines and retail hype. |
| **GMSI** | **Global Macro Stress Indicator** | A multi-asset risk composite score. |
| **BCOM** | **Bloomberg Commodity Index** | Tracked via **DBC ETF**; represents raw material inflation. |
| **$\Delta$Eq** | **Delta Equity** | Percentage change in the **S&P Global 1200** (70% of world market cap). |
| **VADER** | **Sentiment Model** | Lexical model used for scoring text intensity and polarity. |

---

## 💻 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/global-macro-stress-indicator.git](https://github.com/your-username/global-macro-stress-indicator.git)
    cd global-macro-stress-indicator
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Dashboard:**
    ```bash
    streamlit run dashboard.py
    ```

---

## 🎯 Key Indicators for Presentation
* **Rational Trend:** Low Divergence + Positive WS.
* **Market Bubble/Risk:** High Divergence + Positive WS (Hype without News support).
* **Systemic Stress:** High GMSI Score + Rising BCOM.

---

**Project by Vedant Arora** *Mathematical Sciences & Computer Science | University of Delhi*
