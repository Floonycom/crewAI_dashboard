import json
import os
from crewai import Agent
from config.openai_config import generate_response

class ManagerAgent:
    def __init__(self):
        self.agent = Agent(
            name="Agent Manager",
            role="assistant",
            backstory="Tu es le superviseur stratégique de l'équipe de marketing digital. "
                      "Tu t'assures que tous les agents fonctionnent efficacement ensemble.",
            description="Superviseur stratégique du marketing digital.",
            goal="Optimiser la performance de chaque agent et améliorer continuellement la stratégie.",
            method=self.oversee_operations
        )

    def oversee_operations(self):
        # 📌 Récupération des fichiers JSON des autres agents
        data_sources = {
            "reporting": "data/exports/reporting.json",
            "leads": "data/exports/leads.json",
            "emails": "data/exports/emails.json",
            "content": "data/exports/contenu.json",
            "social_media": "data/exports/social_media_posts.json"
        }

        performance_reports = {}

        for key, file_path in data_sources.items():
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        performance_reports[key] = json.load(f)
                    except json.JSONDecodeError:
                        print(f"❌ Erreur : Le fichier {file_path} est mal formé.")
            else:
                print(f"⚠️ Attention : Le fichier {file_path} est introuvable ou vide.")

        # Vérification des performances
        prompt = f"""
        Évalue l’efficacité de chaque agent en fonction des données suivantes :
        {json.dumps(performance_reports, indent=2, ensure_ascii=False)}.
        - Propose des améliorations sur leurs méthodes de travail.
        - Ajuste dynamiquement les prompts pour améliorer les performances globales.
        """

        print("📊 Analyse en cours...")
        result = generate_response(prompt, model="gpt-4-turbo", max_tokens=800)

        # 📌 Sauvegarde des recommandations du Manager dans un fichier JSON
        output_dir = "data/exports"
        output_file = os.path.join(output_dir, "manager_recommendations.json")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump({"recommendations": result}, f, indent=4, ensure_ascii=False)
            print(f"✅ Recommandations sauvegardées dans : {output_file}")

            # 📌 Vérification après écriture
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                print(f"✅ Fichier JSON bien créé : {output_file}")
            else:
                print("❌ Erreur : Le fichier JSON n'a pas été généré ou est vide.")

        except Exception as e:
            print(f"❌ Erreur lors de l'écriture du fichier JSON : {e}")

        return result

# 🔥 Ajout d’un test d’exécution directe
if __name__ == "__main__":
    agent = ManagerAgent()
    
    print("🚀 Lancement de l'agent Manager...")
    recommendations_result = agent.oversee_operations()

    if recommendations_result:
        print("✅ Analyse et recommandations générées avec succès.")
    else:
        print("❌ Aucune recommandation générée.")

