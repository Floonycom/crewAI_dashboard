import json
import os
from crewai import Agent
from config.openai_config import generate_response

class EmailingAgent:
    def __init__(self):
        self.agent = Agent(
            name="Agent Emailing",
            role="assistant",
            backstory="Tu es un expert en email marketing et en nurturing de prospects. "
                      "Ta mission est d'améliorer les taux d'ouverture et de conversion.",
            description="Expert en email marketing et nurturing.",
            goal="Maximiser le taux d’ouverture (>40%) et le taux de conversion (>10%).",
            method=self.create_emails
        )

    def create_emails(self, audience_segment):
        results = {}  # 🔹 Initialisation correcte de la variable `results`
        
        prompts = {
            "email_v1": f"""
            Rédige un email de relance optimisé pour un taux d’ouverture maximal (Version A).
            Segmente le message en fonction de l’audience : {audience_segment}.
            Inclut un appel à l’action clair et un objet percutant.
            """,
            "email_v2": f"""
            Rédige une deuxième version de l'email (Version B) avec un ton plus direct et une offre limitée.
            Segmente le message en fonction de l’audience : {audience_segment}.
            """,
            "email_v3": f"""
            Rédige une troisième version de l’email (Version C) avec une approche storytelling.
            Segmente le message en fonction de l’audience : {audience_segment}.
            """
        }

        for key, prompt in prompts.items():
            print(f"📢 Génération de l'email : {key}...")
            results[key] = generate_response(prompt, model="gpt-4-turbo", max_tokens=500)

        # 📌 Sauvegarde des résultats dans un fichier JSON
        output_dir = "data/exports"
        output_file = os.path.join(output_dir, "emails.json")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=4, ensure_ascii=False)
            print(f"✅ Emails sauvegardés dans : {output_file}")

            # 📌 Vérification après écriture
            if os.path.exists(output_file):
                print(f"✅ Fichier JSON bien créé : {output_file}")
            else:
                print("❌ Erreur : Le fichier JSON n'a pas été généré.")

        except Exception as e:
            print(f"❌ Erreur lors de l'écriture du fichier JSON : {e}")

        return results

# 🔥 Ajout d’un test d’exécution directe
if __name__ == "__main__":
    agent = EmailingAgent()
    audience_segment = "Leads chauds ayant montré un intérêt mais n’ayant pas encore converti"

    print("🚀 Lancement de l'agent Emailing...")
    email_results = agent.create_emails(audience_segment)

    if email_results:
        print("✅ Emails générés avec succès.")
    else:
        print("❌ Aucun email généré.")
