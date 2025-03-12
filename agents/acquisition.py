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
        Tu es un expert en prospection. Identifie 10 leads qualifiés pour une salle de sport premium. 
        Utilise LinkedIn Sales Navigator et segmente les leads en haute/moyenne/basse priorité.
        {query}
        """
        return generate_response(prompt, model="gpt-4-turbo", max_tokens=300)