# app.py
import streamlit as st
from PIL import Image
import os
import pandas as pd
import plotly.express as px
from fpdf import FPDF
from streamlit_lottie import st_lottie
import json
import requests
import base64
import streamlit.components.v1 as components

# ----------------------------
# Config
# ----------------------------
st.set_page_config(
    page_title="Krishna Lal — Pro Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Load assets & Lottie
# ----------------------------
# Example Lottie URL (coding / developer animation). Replace if you have local JSON.
LOTTIE_URL = "https://assets2.lottiefiles.com/packages/lf20_jtbfg2nb.json"
def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

lottie_coding = load_lottie(LOTTIE_URL)

# ----------------------------
# Theme CSS (neon / black / purple / cyan)
# ----------------------------
css = """
<style>
:root{
  --bg1: #05060a;
  --bg2: #12061a;
  --accent: #00fff0;
  --accent2: #9b59ff;
  --muted: #98a8b9;
}
body {
  background: linear-gradient(135deg, var(--bg1) 0%, var(--bg2) 100%);
  color: #e8f7ff;
  font-family: "Segoe UI", Roboto, "Helvetica Neue", Arial;
}
.block-container {
  padding: 1rem 2rem;
}
.card {
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  border-left: 3px solid rgba(0,255,240,0.08);
  padding: 14px;
  border-radius: 12px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.6);
}
.neon {
  color: var(--accent);
  text-shadow: 0 0 8px rgba(0,255,240,0.12), 0 0 20px rgba(155,89,255,0.06);
}
.small { font-size:0.95rem; color:var(--muted); }
.badge { display:inline-block; padding:6px 10px; border-radius:999px; background: rgba(0,255,240,0.04); color:var(--accent); margin-right:6px; font-weight:600; }
.link-btn{ padding:8px 12px; border-radius:10px; background:linear-gradient(90deg, rgba(0,255,240,0.06), rgba(155,89,255,0.04)); color:var(--accent); text-decoration:none; border:1px solid rgba(255,255,255,0.02); }
.footer{ color:#9aa7b3; font-size:0.9rem; }
.progress-outer{ width:100%; background: rgba(255,255,255,0.03); border-radius:999px; padding:3px; }
.progress-inner{ height:10px; border-radius:999px; background: linear-gradient(90deg,#00fff0,#9b59ff); box-shadow: 0 4px 18px rgba(155,89,255,0.12); }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# ----------------------------
# Resume content (pulled from user's uploaded resume)
# Source: uploaded resume file (projects, education, achievements). See file reference in repo.
# ----------------------------
NAME = "Krishna Lal"
TAGLINE = "Computer Science (DS) Student | ML & Embedded Systems | Hackathon Winner"
LOCATION = "Asansol, West Bengal, India"
EMAIL = "krilal324@gmail.com"
PHONE = "+91 73629 94375"
GITHUB = "https://github.com/Krish033-source"
LINKEDIN = "https://www.linkedin.com/in/krishna-lal-5b1a22321"
LEETCODE = "https://leetcode.com/"      # replace with your profile
CODOLIO = "https://codolio.com/"        # replace with your profile

EDUCATION = [
    {
        "degree": "B.Tech – Computer Science & Engineering (Data Science)",
        "institute": "Haldia Institute of Technology, West Bengal",
        "details": "2nd Semester | SGPA: 8.88 | Expected Graduation: 2028"
    },
    {
        "degree": "Class XII",
        "institute": "Jawahar Navodaya Vidyalaya, Durgapur",
        "details": "93.4% (2024)"
    },
    {
        "degree": "Class X",
        "institute": "Jawahar Navodaya Vidyalaya, Durgapur",
        "details": "93.2% (2022)"
    }
]

PROJECTS = [
    {
        "title":"Fintrax",
        "desc":"Expense-tracking & financial analysis tool using Python & Pandas for data handling and visualization.",
        "tech":"Python, Pandas, Matplotlib, Streamlit",
        "link": GITHUB
    },
    {
        "title":"LacoPred",
        "desc":"Machine learning model to predict land prices based on key features using Scikit-learn regression techniques.",
        "tech":"Scikit-learn, Pandas, Numpy",
        "link": GITHUB
    },
    {
        "title":"CV Analyzer",
        "desc":"Python-based ML tool that parses resumes and evaluates candidate profiles against job descriptions.",
        "tech":"Python, Pandas, Flask (prototype)",
        "link": GITHUB
    }
]

ACHIEVEMENTS = [
    "1st Position – InnovateX Hackathon (CSI)",
    "3rd Position – National-Level ISTE Ideathon",
    "Technical Member – ISTE, Haldia Institute of Technology"
]

# Skills & proficiency (humanized)
SKILLS = {
    "Python": 95,
    "Streamlit": 60,
    "DSA (Python)": 80,
    "Machine Learning": 80,
    "Flask": 30,
    "MySQL": 50,
    "Cybersecurity and Networking": 70,
    "C":75,
    "Java": 50,
    "R": 50,
    "Embedded (Arduino/RPi)": 70
}

# ----------------------------
# Top header layout
# ----------------------------
col1, col2 = st.columns([1,2], gap="large")
with col1:
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='badge'>Open to Internships and Research Work</div> <div class='badge'>Freelance: ML/Data</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='height:8px'></div><div class='small'>Location</div><div style='font-weight:700'>{LOCATION}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='height:6px'></div><div class='small'>Contact</div><div style='font-weight:700'>{EMAIL}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<h1 class='neon'>{NAME}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='margin-top:0'>{TAGLINE}</h4>", unsafe_allow_html=True)
    # Lottie animation if available
    if lottie_coding:
        st_lottie(lottie_coding, height=140, key="coding")
    st.markdown("""<div class='small' style='margin-top:8px'>Built multiple ML-powered tools and embedded prototypes, enabling stakeholders to evaluate and adopt solutions within days. Proficient in Python, Streamlit, and Linux system programming, with a track record of translating concepts into working demos quickly.</div>""", unsafe_allow_html=True)

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# ----------------------------
# Short stats
# ----------------------------
stats = {
    "SGPA": "8.88",
    "Semester": "3rd",
    "Hackathons": "1st InnovateX • 3rd National Ideathon",
    "Role": "Technical Member — ISTE"
}
cols = st.columns(len(stats))
for i, (k, v) in enumerate(stats.items()):
    with cols[i]:
        st.markdown(f"<div class='card'><div class='small'>{k}</div><div style='font-weight:800;margin-top:6px'>{v}</div></div>", unsafe_allow_html=True)

st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

# ----------------------------
# Navigation buttons
# ----------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<a class='link-btn' href='#education'>Education</a>  <a class='link-btn' href='#skills'>Skills</a>  <a class='link-btn' href='#projects'>Projects</a>  <a class='link-btn' href='#achievements'>Achievements</a>  <a class='link-btn' href='#contact'>Contact</a>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# ----------------------------
# Education section
# ----------------------------
st.markdown("<a id='education'></a>", unsafe_allow_html=True)
st.header("Education")
for edu in EDUCATION:
    st.markdown("<div class='card' style='margin-bottom:10px'>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-weight:700'>{edu['degree']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='small'>{edu['institute']} • {edu['details']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# Skills & graph
# ----------------------------
st.markdown("<a id='skills'></a>", unsafe_allow_html=True)
st.header("Skills & Proficiency")
left, right = st.columns([1,1.2], gap="large")
with left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='margin-top:0'>Core Skills</h4>", unsafe_allow_html=True)
    for k, v in SKILLS.items():
        # highlight Python / Streamlit
        if k in ["Python", "Streamlit"]:
            st.markdown(f"<div style='display:flex;justify-content:space-between'><div style='font-weight:700'>{k}</div><div style='font-weight:700;color:#00fff0'>{v}%</div></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='display:flex;justify-content:space-between'><div class='small'>{k}</div><div class='small'>{v}%</div></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='progress-outer'><div class='progress-inner' style='width:{v}%;'></div></div>", unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='margin-top:0'>Skill Distribution</h4>", unsafe_allow_html=True)
    df = pd.DataFrame({"skill": list(SKILLS.keys()), "level": list(SKILLS.values())}).sort_values("level", ascending=True)
    fig = px.bar(df, x="level", y="skill", orientation="h", range_x=[0,100], height=360)
    fig.update_traces(marker=dict(color='rgba(0,255,240,0.9)', line=dict(color='rgba(155,89,255,0.2)', width=1)))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis=dict(showgrid=False), yaxis=dict(tickfont=dict(color="#ffffff")))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# Projects (cards with CTA)
# ----------------------------
st.markdown("<a id='projects'></a>", unsafe_allow_html=True)
st.header("Projects — Deployable & Impactful")
for p in PROJECTS:
    st.markdown("<div class='card' style='margin-bottom:12px'>", unsafe_allow_html=True)
    st.markdown(f"<div style='display:flex; justify-content:space-between; align-items:center'><div><h3 style='margin:0'>{p['title']}</h3><div class='small'>{p['tech']}</div></div><div><a class='link-btn' href='{p['link']}' target='_blank'>View Code</a></div></div>", unsafe_allow_html=True)
    st.markdown(f"<div style='margin-top:8px'>{p['desc']}</div><div style='font-weight:600;margin-top:8px;color:#bcdff0'>Impact: Prototype & analytics ready for demo</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# Achievements
# ----------------------------
st.markdown("<a id='achievements'></a>", unsafe_allow_html=True)
st.header("Achievements & Roles")
st.markdown("<div class='card'>", unsafe_allow_html=True)
for a in ACHIEVEMENTS:
    st.markdown(f"- {a}", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# PDF generator (downloadable resume created from app content)
# ----------------------------
from fpdf import FPDF

# ----------------- CONFIG / DATA -----------------
# Replace these with your real variables
NAME = "Krishna Lal"
TAGLINE = "Aspiring ML Engineer & Developer"
EMAIL = "krilal324@gmail.com"
LOCATION = "Asansol, India"

EDUCATION = [
    {"degree": "B.Tech CSE-DS", "institute": "HIT Haldia", "details": "2024-2028, SGPA 8.88"}
]

PROJECTS = [
    {"title": "Smart Health System", "tech": "Python, ML", "desc": "Early warning system for diseases."}
]

SKILLS = {"Python": "Advanced", "ML": "Intermediate", "DSA": "Intermediate"}
ACHIEVEMENTS = ["Member of ISTE Technical Team"]

# ----------------- FUNCTIONS -----------------
def sanitize(text: str) -> str:
    """Replace unsupported characters for FPDF (Latin-1 safe)."""
    return (text
            .replace("•", "-")
            .replace("–", "-")
            .replace("—", "-")
            .replace("’", "'")
            .replace("“", '"')
            .replace("”", '"'))

def create_pdf_bytes(name=NAME):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Header
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 8, sanitize(name), ln=1)

    pdf.set_font("Helvetica", size=11)
    pdf.cell(0, 6, sanitize(TAGLINE), ln=1)
    pdf.ln(4)

    # Contact
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 6, "Contact", ln=1)
    pdf.set_font("Helvetica", size=10)
    pdf.multi_cell(pdf.w - 2*pdf.l_margin, 6, sanitize(f"{EMAIL} - {PHONE} - {LOCATION}"))
    pdf.ln(4)

    # Education
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 6, "Education", ln=1)
    pdf.set_font("Helvetica", size=10)
    for e in EDUCATION:
        line = f"{e['degree']} - {e['institute']} - {e['details']}"
        pdf.multi_cell(pdf.w - 2*pdf.l_margin, 6, sanitize(line))
    pdf.ln(2)

    # Projects
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 6, "Projects", ln=1)
    pdf.set_font("Helvetica", size=10)
    for p in PROJECTS:
        pdf.multi_cell(pdf.w - 2*pdf.l_margin, 6, sanitize(f"{p['title']} - {p['tech']}"))
        pdf.multi_cell(pdf.w - 2*pdf.l_margin, 6, "  " + sanitize(p['desc']))
        pdf.ln(1)
    pdf.ln(2)

    # Skills
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 6, "Skills (selected)", ln=1)
    pdf.set_font("Helvetica", size=10)
    skills_line = ", ".join([sanitize(k) for k in SKILLS.keys()])
    pdf.multi_cell(pdf.w - 2*pdf.l_margin, 6, skills_line)
    pdf.ln(2)

    # Achievements
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 6, "Achievements", ln=1)
    pdf.set_font("Helvetica", size=10)
    for a in ACHIEVEMENTS:
        pdf.multi_cell(pdf.w - 2*pdf.l_margin, 6, "- " + sanitize(a))

    # Return PDF as bytes (bytearray)
    return pdf.output(dest="S")  # No encode(), already bytearray



pdf_bytes = bytes(create_pdf_bytes())

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
col_a, col_b = st.columns([1,3])
with col_a:
   st.download_button(
    label="📄 Download Resume (PDF)",
    data=pdf_bytes,
    file_name="resume.pdf",
    mime="application/pdf"
)
with col_b:
    st.markdown("<div class='card'><div style='font-weight:700'>Links & Quick Contact</div><div style='height:6px'></div>", unsafe_allow_html=True)
    st.markdown(f"<a class='link-btn' href='{LINKEDIN}' target='_blank'>LinkedIn</a>  <a class='link-btn' href='{GITHUB}' target='_blank'>GitHub</a>  <a class='link-btn' href='{LEETCODE}' target='_blank'>LeetCode</a>  <a class='link-btn' href='{CODOLIO}' target='_blank'>Codolio</a>", unsafe_allow_html=True)
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='small'>Email</div><div style='font-weight:700'>{EMAIL}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# Footer / CTA
# ----------------------------
st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
st.markdown("<div class='card'><div style='font-weight:700'>Ready for interviews & paid internships</div><div class='small' style='margin-top:6px'>I can share demo links, runnable notebook, or host a 10-minute walkthrough. Email or DM to schedule.</div>", unsafe_allow_html=True)
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>© 2025 Krishna Lal — Built with production focus • Portfolio generated from app content</div>", unsafe_allow_html=True)


