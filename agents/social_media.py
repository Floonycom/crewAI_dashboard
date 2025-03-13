import json
import os
from crewai import Agent
from config.openai_config import generate_response

class SocialMediaAgent:
    def __init__(self):
        self.agent = Agent(
            name="Agent Social Media",
            role="assistant",
            backstory="Tu es un expert en community management et en engagement digital. "
                      "Ta mission est de maximiser la portée et l'impact des contenus publiés.",
            description="Expert en engagement et visibilité sur les réseaux sociaux.",
            goal="Maximiser la portée des contenus en les adaptant aux plateformes.",
            method=self.optimize_posts
        )

    def optimize_posts(self):
        # 📌 Récupération des anciens posts
        past_posts = self.load_past_posts()

        prompt = f"""
        Analyse les performances des 3 publications ayant eu le plus d'engagement.
        Pour chaque post, reformule-le en version optimisée pour maximiser son impact.
        Propose des adaptations spécifiques pour Instagram, LinkedIn et Twitter.
        Suggère de nouveaux formats engageants basés sur les tendances actuelles.
        {json.dumps(past_posts, indent=2, ensure_ascii=False)}
        """

        print("📊 Optimisation des posts en cours...")
        result = generate_response(prompt, model="gpt-4-turbo", max_tokens=800)

        # 📌 Sauvegarde des posts optimisés dans un fichier JSON
        output_dir = "data/exports"
        output_file = os.path.join(output_dir, "social_media_posts.json")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump({"optimized_posts": result}, f, indent=4, ensure_ascii=False)
            print(f"✅ Posts optimisés sauvegardés dans : {output_file}")

            # 📌 Vérification après écriture
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                print(f"✅ Fichier JSON bien créé : {output_file}")
            else:
                print("❌ Erreur : Le fichier JSON n'a pas été généré ou est vide.")

        except Exception as e:
            print(f"❌ Erreur lors de l'écriture du fichier JSON : {e}")

        return result

    def load_past_posts(self):
        """Charge les posts précédents depuis `contenu.json` et `reporting.json`"""
        data_sources = ["data/exports/contenu.json", "data/exports/reporting.json"]
        past_posts = []

        for file_path in data_sources:
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                        if "posts" in data:
                            past_posts.extend(data["posts"])
                        elif "analysis" in data:
                            past_posts.append(data["analysis"])
                    except json.JSONDecodeError:
                        print(f"❌ Erreur : Le fichier {file_path} est mal formé.")

        return past_posts if past_posts else ["Aucun post trouvé"]

# 🔥 Ajout d’un test d’exécution directe
if __name__ == "__main__":
    agent = SocialMediaAgent()
    
    print("🚀 Lancement de l'agent Social Media...")
    optimized_posts = agent.optimize_posts()

    if optimized_posts:
        print("✅ Posts optimisés générés avec succès.")
    else:
        print("❌ Aucun post optimisé généré.")
