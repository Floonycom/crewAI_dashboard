from crewai import Agent
from config.openai_config import generate_response

class ContenuAgent:
    def __init__(self):
        self.agent = Agent(
            name="Agent Contenu",
            role="assistant",
            backstory="Tu es un expert en marketing de contenu spécialisé dans le bien-être et le fitness. "
                      "Tu produis du contenu optimisé SEO pour attirer et engager une audience cible.",
            description="Rédacteur expert en fitness et bien-être.",
            goal="Produire des contenus engageants et optimisés SEO.",
            method=self.create_content
        )

    def create_content(self, topic):
        prompt = f"""
        Rédige un article de blog de 1000 mots structuré en 3 parties sur le sujet : {topic}. 
        Génère ensuite 2 carrousels Instagram/LinkedIn et un script de vidéo courte.
        """
        return generate_response(prompt, model="gpt-4-turbo", max_tokens=300)