from agents.acquisition import AcquisitionAgent
from agents.contenu import ContenuAgent
from agents.social_media import SocialMediaAgent
from agents.emailing import EmailingAgent
from agents.reporting import ReportingAgent
from agents.manager import ManagerAgent

def test_agents():
    acquisition = AcquisitionAgent()
    print("🟢 Test Acquisition : ", acquisition.collect_leads("Sport et bien-être"))

    contenu = ContenuAgent()
    print("🟢 Test Contenu : ", contenu.create_content("Musculation et nutrition"))

    social = SocialMediaAgent()
    print("🟢 Test Social Media : ", social.optimize_posts("Liste des posts populaires"))

    emailing = EmailingAgent()
    print("🟢 Test Emailing : ", emailing.create_emails("Prospects VIP"))

    reporting = ReportingAgent()
    print("🟢 Test Reporting : ", reporting.analyze_data("Analyse des campagnes"))

    manager = ManagerAgent()
    print("🟢 Test Manager : ", manager.oversee_operations("Rapport hebdomadaire"))

if __name__ == "__main__":
    test_agents()
