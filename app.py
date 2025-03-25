import streamlit as st
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import plotly.express as px

def load_json_data(file_path):
    """Charge des données JSON depuis un fichier"""
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        return None
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier {file_path}: {e}")
        return None

def load_csv_data(file_path):
    """Charge des données CSV depuis un fichier"""
    try:
        if os.path.exists(file_path):
            return pd.read_csv(file_path)
        return None
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier {file_path}: {e}")
        return None

st.set_page_config(page_title="Tableau de bord CrewAI", layout="wide")

st.title("Tableau de bord CrewAI - Marketing & Communication 🚀")

# Sidebar pour la navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Sélectionner une page", ["Dashboard", "Leads", "Emails", "Reporting", "Contenu", "Social Media", "Recommandations"])

# Chargement des données
data_folder = "data"
leads_json = load_json_data(os.path.join(data_folder, "leads.json"))
leads_csv = load_csv_data(os.path.join(data_folder, "leads.csv"))
emails_data = load_json_data(os.path.join(data_folder, "emails.json"))
reporting_data = load_json_data(os.path.join(data_folder, "reporting.json"))
content_data = load_json_data(os.path.join(data_folder, "contenu.json"))
social_data = load_json_data(os.path.join(data_folder, "social_media_posts.json"))
manager_data = load_json_data(os.path.join(data_folder, "manager_recommendations.json"))

if page == "Dashboard":
    st.header("Aperçu global des performances")
    
    # Afficher les KPIs principaux
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Leads générés", "100", "+5%")
    
    with col2:
        st.metric("Taux d'ouverture emails", "45%", "+2%")
    
    with col3:
        st.metric("Engagement social media", "72%", "+8%")
    
    # Graphique d'exemple
    st.subheader("Performance des campagnes")
    data = {
        'Campagne': ['Email', 'Social Media', 'Contenu', 'SEO'],
        'Performance': [45, 72, 60, 55]
    }
    df = pd.DataFrame(data)
    fig = px.bar(df, x='Campagne', y='Performance', color='Performance')
    st.plotly_chart(fig, use_container_width=True)

elif page == "Leads":
    st.header("Analyse des Leads")
    
    if leads_json:
        st.subheader("Stratégie d'acquisition des leads")
        st.write(leads_json.get("leads", "Aucune donnée disponible"))
    
    if leads_csv is not None:
        st.subheader("Liste des leads qualifiés")
        st.dataframe(leads_csv)

elif page == "Emails":
    st.header("Campagnes d'Emails")
    
    if emails_data:
        st.write(emails_data)

elif page == "Reporting":
    st.header("Reporting et Analyses")
    
    if reporting_data:
        st.markdown(reporting_data.get("analysis", "Aucune analyse disponible"))

elif page == "Contenu":
    st.header("Stratégie de Contenu")
    
    if content_data:
        st.write(content_data)

elif page == "Social Media":
    st.header("Stratégie Social Media")
    
    if social_data:
        st.write(social_data)

elif page == "Recommandations":
    st.header("Recommandations de l'Agent Manager")
    
    if manager_data:
        st.markdown(manager_data.get("recommendations", "Aucune recommandation disponible"))

if __name__ == "__main__":
    import os
    st.sidebar.write(f"Streamlit version: {st.__version__}")
    st.sidebar.write(f"Chemin d'exécution: {os.getcwd()}")
