import logging
import sys
from workflows.crew import ActiveSquareCrew

def main():
    """Point d'entrée principal du projet CrewAI"""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    try:
        logging.info("🚀 Démarrage de CrewAI...")
        crew = ActiveSquareCrew()
        crew.run()
        logging.info("✅ CrewAI a terminé son exécution avec succès.")
    except Exception as e:
        logging.error(f"❌ Erreur lors de l'exécution de CrewAI : {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
