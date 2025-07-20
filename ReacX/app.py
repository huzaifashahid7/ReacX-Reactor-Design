import streamlit as st
from components.inputs import get_user_inputs
from components.calculations import calculate_values
from components.plot import show_plot
import streamlit.components.v1 as components
import streamlit as st
import os

# ✅ Load custom CSS
css_file_path = os.path.join(os.path.dirname(_file_), "custom.css")

if os.path.exists(css_file_path):
    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("⚠ custom.css file not found. Skipping styles.")

# ✅ Google Analytics integration
components.html("""
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NBX8Z31PKY"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-NBX8Z31PKY');
</script>
""", height=0)

# Page config
st.set_page_config(
    page_title="ReacX – Reactor Visualizer",
    page_icon="🧪",
    layout="wide"
)

# Load custom CSS
try:
    with open("style/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("⚠️ Custom CSS file not found. Skipping style.")

# Header
st.markdown("<a id='home'></a>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; margin-top: 25px;">
    <h1 style="font-weight: 700; font-family: 'Times New Roman', serif;">ReacX – Chemical Reaction Engineering Visualizer</h1>
    <h4 style="color: #555; margin-top: 8px; font-family: 'Times New Roman', serif;">
        Solve, simulate and visualize CSTR, PFR & Batch reactors with ease.
    </h4>
</div>
""", unsafe_allow_html=True)

# Input Section
st.subheader("Reactor Configuration")
user_inputs = get_user_inputs()
st.session_state["user_inputs"] = user_inputs

if st.button("Reset All Inputs"):
    st.session_state.clear()
    st.experimental_rerun()

# Output Section
st.subheader("Results and Graph")
if user_inputs:
    results = calculate_values(user_inputs)
    if results is not None:
        st.success(results["text_result"])
        show_plot(user_inputs, results)
else:
    st.warning("Please enter all valid inputs to see results.")

# ABOUT SECTION
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("""
<h3 style='font-family: "Times New Roman", serif; font-weight: bold; color:#000'>
     About ReacX
</h3>
""", unsafe_allow_html=True)
st.markdown("""
<p style='font-size:18px; text-align: left; font-family: "Times New Roman", serif;'>
Welcome to ReacX — a dynamic and lightweight Streamlit-based web app designed to showcase my front-end skills. This project reflects my understanding of modern web design principles, component-based architecture, and responsive layouts. <br>

I developed this to demonstrate how an elegant UI/UX can be achieved using simplicity, functionality, and clean code. Every section of this app is made from scratch using React and CSS with a strong focus on readability and performance.<br>
Whether you are here to explore my work or simply browsing through, I hope you enjoy the experience. Feel free to connect through the channels below.
</p>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# CONTACT SECTION
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("""
<h3 style='font-family: "Times New Roman", serif; font-weight: bold; color: #000;'>
    Contact
</h3>
""", unsafe_allow_html=True)
st.markdown("""
<div class='contact-item' style='font-family: "Times New Roman", serif;'>
    <img src='https://cdn-icons-png.flaticon.com/512/732/732200.png' class='icon'/>
    <a href="mailto:huzaifashahid569@gmail.com">huzaifashahid569@gmail.com</a>
</div>
<div class='contact-item' style='font-family: "Times New Roman", serif;'>
    <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' class='icon'/>
    <a href="https://www.linkedin.com/in/huzaifashahid7" target="_blank">linkedin.com/in/huzaifashahid7</a>
</div>
<div class='contact-item' style='font-family: "Times New Roman", serif;'>
    <img src='https://cdn-icons-png.flaticon.com/512/25/25231.png' class='icon'/>
    <a href="https://github.com/huzaifashahid7" target="_blank">github.com/huzaifashahid7</a>
</div>
<div class='contact-item' style='font-family: "Times New Roman", serif;'>
    <img src='https://cdn-icons-png.flaticon.com/512/684/684908.png' class='icon'/>
    Location: Kolkata, India
</div>
<div class='contact-item' style='font-family: "Times New Roman", serif;'>
    <img src='https://cdn-icons-png.flaticon.com/512/64/64572.png' class='icon'/>
    Developer: Huzaifa Shahid
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center; margin-top:50px; padding:15px 0; font-size:14px; color:#555; border-top:1px solid #ddd; background-color:#f1f1f1; font-family: 'Times New Roman', serif;">
  © 2025 ReacX by Huzaifa Shahid | AI Data Engineer | Jadavpur University
</div>
""", unsafe_allow_html=True)
