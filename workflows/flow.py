import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
from workflows.crew import ActiveSquareCrew
def main():
    print("🚀 Lancement du CrewAI...")
    # Initialisation du CrewAI
    crew = ActiveSquareCrew()
    # Exécution de toutes les tâches définies dans CrewAI
    result = crew.crew.kickoff()
    print("✅ Workflow terminé avec succès !")
    print("📊 Résultats :", result)
if __name__ == "__main__":
    main()
