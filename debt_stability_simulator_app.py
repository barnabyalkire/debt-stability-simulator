
import streamlit as st

st.set_page_config(page_title="Debt Stability Simulator", layout="centered")

st.title("🇺🇸 U.S. Debt Stability Simulator")
st.markdown("Adjust the sliders to explore how economic factors impact debt stability.")

# Sidebar sliders
st.sidebar.header("Economic Inputs")

g = st.sidebar.slider("GDP Growth Rate (g) [%]", 0.0, 5.0, 2.0, 0.1)
r = st.sidebar.slider("Interest Rate (r) [%]", 0.0, 8.0, 3.0, 0.1)
debt = st.sidebar.slider("Debt-to-GDP Ratio [%]", 60, 150, 100, 1)
deficit = st.sidebar.slider("Annual Deficit (% of GDP)", 0.0, 10.0, 5.0, 0.1)
tax = st.sidebar.slider("Tax Cuts / Revenue Loss ($T)", 0.0, 5.0, 1.0, 0.1)
tariff = st.sidebar.slider("Tariff Disruption Index", 0, 10, 3, 1)
confidence = st.sidebar.slider("Investor Confidence (0–10)", 0, 10, 7, 1)

# Compute stability score
score = 100
score += (g - r) * 15         # boost if growth > rates
score -= (debt - 90) * 0.8    # penalty above 90%
score -= deficit * 2          # penalty for deficit
score -= tax * 4              # penalty for tax cuts
score -= tariff * 3           # penalty for trade disruption
score += confidence * 3       # boost for high confidence

status = "Stable" if score >= 60 else "Unstable"
color = "🟢" if score >= 60 else "🔴"

st.markdown("### Result")
st.markdown(f"**Stability Score:** {color} **{status}** ({round(score)})")

st.caption("This tool is a simulation and does not reflect actual fiscal policy outcomes.")
