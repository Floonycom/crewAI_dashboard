from crewai import Agent
from config.openai_config import generate_response

class ReportingAgent:
    def __init__(self):
        self.agent = Agent(
            name="Agent Reporting",
            role="assistant",
            backstory="Tu es un analyste marketing spécialisé en data et conversion. "
                      "Tu surveilles les KPIs et proposes des recommandations stratégiques.",
            description="Analyste marketing spécialisé en data et conversion.",
            goal="Suivre les KPIs et recommander des optimisations.",
            method=self.analyze_data
        )

    def analyze_data(self, campaign_data):
        prompt = f"""
        Analyse les performances des campagnes Social Media, Emailing et Acquisition. 
        Identifie les points faibles et formule des recommandations d’amélioration.
        {campaign_data}
        """
        return generate_response(prompt, model="gpt-4-turbo", max_tokens=250)
