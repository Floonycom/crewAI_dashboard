import os
import openai
from dotenv import load_dotenv

# 📌 Charger la clé API OpenAI depuis `.env` (Force le chargement)
dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
load_dotenv(dotenv_path)

# 📌 Vérifier si la clé OpenAI est bien récupérée
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("❌ Erreur : Clé OpenAI non trouvée. Vérifie ton fichier .env !")

# 🔹 Initialisation du client OpenAI
client = openai.Client(api_key=OPENAI_API_KEY)

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
