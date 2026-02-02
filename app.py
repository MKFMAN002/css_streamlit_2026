# researcher_profile.py
import streamlit as st
from datetime import datetime
import pandas as pd
import altair as alt

# ───────────────────────────────────────────────
# PAGE CONFIG
# ───────────────────────────────────────────────
st.set_page_config(
    page_title="Comfort Mankele – Research Portfolio",
    page_icon="🌌",
    layout="wide",
)

# ───────────────────────────────────────────────
# CUSTOM CSS + ICONS (Font Awesome)
# ───────────────────────────────────────────────
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
body {
    background-color: #0b1220;
}

.hero {
    padding: 60px 40px;
    border-radius: 18px;
    background: linear-gradient(120deg, #0f172a, #020617);
    border: 1px solid #1e293b;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 3rem;
    color: #e5e7eb;
    margin-bottom: 10px;
}

.hero p {
    font-size: 1.2rem;
    color: #94a3b8;
}

.section {
    background: #020617;
    border: 1px solid #1e293b;
    border-radius: 16px;
    padding: 30px;
    margin-bottom: 30px;
}

.section h2 {
    color: #38bdf8;
    margin-bottom: 15px;
}

.card {
    background: #0b1220;
    border: 1px solid #1e293b;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 15px;
}

.nav-item i {
    margin-right: 8px;
    color: #38bdf8;
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# HERO HEADER
# ───────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>Comfort Mankele</h1>
    <p>Astrophysics Researcher • Radio Astronomy • Data Science</p>
    <p>Pretoria, South Africa • Last updated: Feb 2026</p>
</div>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# TOP NAVIGATION (NO EMOJIS)
# ───────────────────────────────────────────────
tabs = st.tabs(["Home", "Education", "Skills", "Research", "Projects", "Contact"])

# ───────────────────────────────────────────────
# HOME
# ───────────────────────────────────────────────
with tabs[0]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="nav-item"><i class="fa-solid fa-house"></i> Home</h2>', unsafe_allow_html=True)

    st.write("""
    I am an MSc (**Astrophysics and Space Science**) student at the University of Pretoria, 
    specializing in **radio astronomy** and multi-wavelength data analysis.

    **Focus areas:**
    - Developing data reduction and calibration pipelines  
    - Imaging NenuFAR measurement sets  
    - Radio galaxy spectral index mapping  
    - Multi-wavelength overlays (radio, optical, X-ray)  
    - FITS cube processing  
    """)

    st.info("Open to research collaborations and data projects.")
    st.markdown('</div>', unsafe_allow_html=True)

# ───────────────────────────────────────────────
# EDUCATION
# ───────────────────────────────────────────────
with tabs[1]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="nav-item"><i class="fa-solid fa-graduation-cap"></i> Education</h2>', unsafe_allow_html=True)

    st.markdown("""
    **BSc Honours in Astrophysics**  
    University of Pretoria  

    **BSc Astrophysics & Space Science**  
    University of Pretoria  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ───────────────────────────────────────────────
# SKILLS
# ───────────────────────────────────────────────
with tabs[2]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="nav-item"><i class="fa-solid fa-screwdriver-wrench"></i> Skills</h2>', unsafe_allow_html=True)

    skills = pd.DataFrame({
        "Skill": ["Python", "CASA", "Altair/Matplotlib", "Git", "Pandas", "SQL", "Linux", "Multi-wavelength"],
        "Level": [90, 85, 80, 75, 88, 70, 78, 82]
    })

    chart = alt.Chart(skills).mark_bar().encode(
        x=alt.X("Level:Q", scale=alt.Scale(domain=[0, 100])),
        y=alt.Y("Skill:N", sort="-x"),
        tooltip=["Skill", "Level"]
    ).properties(height=350)

    st.altair_chart(chart, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ───────────────────────────────────────────────
# RESEARCH
# ───────────────────────────────────────────────
with tabs[3]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="nav-item"><i class="fa-solid fa-flask"></i> Research</h2>', unsafe_allow_html=True)

    for item in [
        "Radio galaxy spectral index mapping",
        "Multi-wavelength image overlays",
        "Flux extraction pipelines",
        "Interactive astronomy dashboards",
        "Machine learning in astrophysics",
    ]:
        st.markdown(f"- {item}")

    st.markdown('</div>', unsafe_allow_html=True)

# ───────────────────────────────────────────────
# PROJECTS
# ───────────────────────────────────────────────
with tabs[4]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="nav-item"><i class="fa-solid fa-diagram-project"></i> Projects</h2>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**Radio Galaxy Spectral Index Dashboard**")
    st.write("""
    - FITS image processing  
    - Spectral index heatmaps  
    - Radio contours  
    - Streamlit dashboard  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**Multi-wavelength Visualisation Toolkit**")
    st.write("Overlay radio, optical and X-ray images for galaxy studies.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ───────────────────────────────────────────────
# CONTACT
# ───────────────────────────────────────────────
with tabs[5]:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="nav-item"><i class="fa-solid fa-envelope"></i> Contact</h2>', unsafe_allow_html=True)

    with st.form("contact"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        if st.form_submit_button("Send"):
            if not all([name, email, msg]):
                st.warning("Fill in all fields.")
            else:
                st.success("Message received (demo only).")

    st.markdown("**Links**")
    st.markdown("- GitHub: https://github.com/ComfortMankele")
    st.markdown("- LinkedIn: https://www.linkedin.com/in/comfort-mankele/")
    st.markdown('</div>', unsafe_allow_html=True)

# ───────────────────────────────────────────────
# FOOTER
# ───────────────────────────────────────────────
st.caption(f"© {datetime.now().year} Comfort Mankele • Streamlit Portfolio")
