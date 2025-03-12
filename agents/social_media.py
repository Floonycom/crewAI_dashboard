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

    def optimize_posts(self, past_posts):
        prompt = f"""
        Analyse les performances des 3 meilleures publications passées et reformule-les en version optimisée.
        Suggère de nouveaux formats engageants.
        {past_posts}
        """
        return generate_response(prompt, model="gpt-4-turbo", max_tokens=250)
