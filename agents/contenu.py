import json
import os
from crewai import Agent
from config.openai_config import generate_response

class ContenuAgent:
    def __init__(self):
        self.agent = Agent(
            name="Agent Contenu",
            role="assistant",
            backstory="Tu es un expert en marketing de contenu spécialisé dans le bien-être et le fitness. "
                      "Tu produis du contenu optimisé SEO pour attirer et engager une audience cible.",
            description="Rédacteur expert en fitness et bien-être.",
            goal="Produire des contenus engageants et optimisés SEO.",
            method=self.create_content
        )

    def create_content(self, topic):
        # 🔹 Séparation en trois requêtes pour un rendu plus détaillé
        prompts = {
            "article": f"Rédige un article de blog de 1000 mots structuré en 3 parties sur le sujet : {topic}.",
            "carousels": f"Génère 2 carrousels Instagram/LinkedIn en format texte avec hashtags sur le sujet : {topic}.",
            "video_script": f"Écris un script de vidéo courte engageante pour TikTok et Reels sur le sujet : {topic}."
        }

        # 🔹 Générer chaque partie séparément
        results = {}
        for key, prompt in prompts.items():
            print(f"📢 Génération du contenu : {key}...")
            results[key] = generate_response(prompt, model="gpt-4-turbo", max_tokens=800)

        # 🔹 Sauvegarde des résultats dans un fichier JSON
        output_dir = "data/exports"
        output_file = os.path.join(output_dir, "contenu.json")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=4, ensure_ascii=False)
            print(f"✅ Contenu généré et sauvegardé dans : {output_file}")
        except Exception as e:
            print(f"❌ Erreur lors de l'écriture du fichier JSON : {e}")

        # 📌 Vérification après l'écriture
        if os.path.exists(output_file):
            print(f"✅ Fichier JSON bien créé : {output_file}")
        else:
            print("❌ Erreur : Le fichier JSON n'a pas été généré.")

        return results

# 🔥 Ajout d’un test d’exécution directe
if __name__ == "__main__":

    agent = ContenuAgent()
    topic = "Les bienfaits du sport sur la santé mentale"

    print("🚀 Lancement de l'agent Contenu...")
    content_result = agent.create_content(topic)

    if content_result:
        print("✅ Contenu généré avec succès.")
    else:
        print("❌ Aucun contenu généré.")
