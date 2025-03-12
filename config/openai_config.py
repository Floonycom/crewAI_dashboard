import os
from dotenv import load_dotenv
import openai

# Charger la clé API depuis .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialisation du client OpenAI (nouvelle API)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt, model="gpt-4-turbo", max_tokens=300, temperature=0.7):
    """ Génère une réponse OpenAI optimisée avec la nouvelle API """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Tu es un assistant spécialisé en communication et marketing digital."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].message.content.strip()
