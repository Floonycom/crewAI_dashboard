import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from crewai import Crew, Task
from agents.acquisition import AcquisitionAgent
from agents.emailing import EmailingAgent
from agents.reporting import ReportingAgent
from agents.contenu import ContenuAgent
from agents.social_media import SocialMediaAgent
from agents.manager import ManagerAgent
from config.openai_config import generate_response  # ✅ Import OpenAI

class ActiveSquareCrew:
    def __init__(self):
        # Initialisation des agents avec leur rôle et backstory
        self.agent_acquisition = AcquisitionAgent().agent
        self.agent_emailing = EmailingAgent().agent
        self.agent_reporting = ReportingAgent().agent
        self.agent_contenu = ContenuAgent().agent
        self.agent_social = SocialMediaAgent().agent
        self.agent_manager = ManagerAgent().agent

        # Définition des tâches associées aux agents
        self.task_acquisition = Task(
            description="Trouver et qualifier 100 leads par mois en utilisant LinkedIn Sales Navigator et Airtable.",
            agent=self.agent_acquisition,
            expected_output="Liste des 10 nouveaux leads qualifiés sous format JSON ou CSV."
        )

        self.task_emailing = Task(
            description="Envoyer des campagnes email personnalisées et optimiser les taux d’ouverture et conversion.",
            agent=self.agent_emailing,
            expected_output="Deux versions d'un email de relance avec objets différents (A/B testing)."
        )

        self.task_reporting = Task(
            description="Analyser les performances des campagnes marketing et proposer des ajustements.",
            agent=self.agent_reporting,
            expected_output="Rapport synthétique des performances avec recommandations stratégiques."
        )

        self.task_contenu = Task(
            description="Créer des articles SEO, des carrousels pour réseaux sociaux et des scripts vidéo.",
            agent=self.agent_contenu,
            expected_output="Article structuré, 3 carrousels LinkedIn/Instagram, 1 email résumé, et un script vidéo."
        )

        self.task_social = Task(
            description="Optimiser la publication des contenus et analyser l'engagement social.",
            agent=self.agent_social,
            expected_output="Liste des 5 posts optimisés, suggestions de nouveaux formats, et rapport de performance."
        )

        self.task_manager = Task(
            description="Superviser les campagnes et adapter les stratégies en fonction des performances.",
            agent=self.agent_manager,
            expected_output="Synthèse des KPIs et ajustements stratégiques pour améliorer les résultats."
        )

        # Création du Crew avec les agents et leurs tâches
        self.crew = Crew(
            agents=[
                self.agent_acquisition,
                self.agent_emailing,
                self.agent_reporting,
                self.agent_contenu,
                self.agent_social,
                self.agent_manager
            ],
            tasks=[
                self.task_acquisition,
                self.task_emailing,
                self.task_reporting,
                self.task_contenu,
                self.task_social,
                self.task_manager
            ],
            llm=generate_response  # ✅ On utilise OpenAI comme moteur LLM
        )

    # Méthode pour exécuter le workflow
    def run(self):
        print("🚀 Lancement du CrewAI...")
        result = self.crew.kickoff()  # ✅ Utilisation de kickoff() avec CrewAI 0.105.0
        print("✅ Résultat :", result)

# Exécution du workflow si ce fichier est lancé directement
if __name__ == "__main__":
    crew_instance = ActiveSquareCrew()
    crew_instance.run()
