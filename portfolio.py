import streamlit as st

with st.sidebar:
    st.title("📌 Marietou NDIAYE")
    st.header("    Développeuse d'applications et géomaticienne")
    st.title("📞 Contact")
    st.write("📧 Email: marietou.ndiaye@email.com")
    st.write("📱 Téléphone: +221 77 XXX XX XX")
    st.write("🔗 LinkedIn: linkedin.com/in/nom")
    st.write("💻 GitHub: github.com/nom")
    
st.header("👩🏽‍💻 À propos de moi")
st.write(
        """
        👋 Je suis  géomaticienne et technicienne
        supérieure en développement et administration d'applications web,
        passionnée par l’analyse spatiale,
        les systèmes d’information géographique (SIG) et les outils numériques.
        J’aime transformer les données géographiques en solutions utiles
        grâce à la cartographie et à la programmation.
        """
    )

st.header("🛠️ Compétences")
col1,col2=st.columns(2)
with col1: 
    st.subheader("🌍 Géomatique & SIG")
    st.write("* Outils SIG")
    st.write("* Topographie")
    st.write("* Cartographie thématique")
    st.write("* Projections cartographiques")
with col2:
    st.subheader("💻 Informatique")
    st.write("* Suite bureautique")
    st.write("* Python")
    st.write("* Oracle / XML / UML")
    st.write("* SQL / PostgreSQL ")
    st.write("* Technologie web ")
 
st.header("📂 Projets") 


st.header("🎓 Formations")
st.write(
        """
        * Brevet de Technicien Supérieur /Géomatique                
        * Licence /Développement et administration d'applications web
        * EFL /English as a Foreign Language DAUST
        * Baccalauréat
        """
    )

st.success("Merci d’avoir visité mon portfolio 😊")
    
    