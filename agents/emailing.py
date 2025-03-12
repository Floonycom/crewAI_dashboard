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
        prompt = f"""
        Rédige une version courte d’un email de relance optimisé pour un taux d’ouverture maximal.
        Segmente le message en fonction de l’audience : {audience_segment}.
        """
        return generate_response(prompt, model="gpt-4-turbo", max_tokens=200)
