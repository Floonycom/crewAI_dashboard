from crewai import Agent
from config.openai_config import generate_response

class ManagerAgent:
    def __init__(self):
        self.agent = Agent(
            name="Agent Manager",
            role="assistant",
            backstory="Tu es le superviseur stratégique de l'équipe de marketing digital. "
                      "Tu t'assures que tous les agents fonctionnent efficacement ensemble.",
            description="Superviseur stratégique du marketing digital.",
            goal="Optimiser la performance de chaque agent et améliorer continuellement la stratégie.",
            method=self.oversee_operations
        )

    def oversee_operations(self, performance_reports):
        prompt = f"""
        Évalue l’efficacité de chaque agent, ajuste les prompts et propose des améliorations stratégiques.
        Basé sur les données suivantes : {performance_reports}.
        """
        return generate_response(prompt, model="gpt-4-turbo", max_tokens=300)
