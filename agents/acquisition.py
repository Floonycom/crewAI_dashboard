import json
import os
from crewai import Agent
from config.openai_config import generate_response

class AcquisitionAgent:
    def __init__(self):
        self.agent = Agent(
            name="Agent Acquisition",
            role="assistant",
            backstory="Tu es un expert en prospection digitale et conversion de leads. "
                      "Tu travailles pour une salle de sport premium et ton objectif est "
                      "de maximiser l'acquisition de nouveaux clients.",
            description="Expert en prospection B2B/B2C pour une salle de sport premium.",
            goal="Identifier et convertir 80 leads B2B et 150 leads B2C par mois avec un taux de conversion de 20%.",
            method=self.collect_leads
        )

    def collect_leads(self, query):
        prompt = f"""
        Tu es un expert en prospection digitale. Identifie 20 leads qualifiés (10 B2B et 10 B2C) pour une salle de sport premium.
        - Utilise LinkedIn Sales Navigator pour les B2B.
        - Utilise Meta Ads et Google Ads pour les B2C.
        - Pour chaque lead, donne : Nom, Entreprise (si B2B), Email, Téléphone, Score de priorité (Haute/Moyenne/Basse).
        - Classe les leads par ordre de priorité.
        {query}
        """

        print("📢 Recherche des leads en cours...")
        result = generate_response(prompt, model="gpt-4-turbo", max_tokens=800)

        # 📌 Vérification du résultat généré
        if not result:
            print("❌ Erreur : Aucun lead généré.")
            return None

        print(f"✅ Leads trouvés : {result}")

        # 📌 Sauvegarde des résultats dans un fichier JSON
        output_dir = "data/exports"
        output_file = os.path.join(output_dir, "leads.json")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump({"leads": result}, f, indent=4, ensure_ascii=False)
            print(f"✅ Leads sauvegardés dans : {output_file}")
        except Exception as e:
            print(f"❌ Erreur lors de l'écriture du fichier JSON : {e}")

        return result

# 🔥 Ajout d’un test d’exécution directe
if __name__ == "__main__":
    agent = AcquisitionAgent()
    query = "Leads qualifiés pour salle de sport premium"

    print("🚀 Lancement de l'agent Acquisition...")
    leads_result = agent.collect_leads(query)

    if leads_result:
        print("✅ Leads générés avec succès.")
    else:
        print("❌ Aucun lead généré.")
