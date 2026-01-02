import praw
import time
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# --- PARTIE POUR GARDER RENDER GRATUIT ---
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Robot de Zack en ligne")

def run_health_check():
    # Render utilise souvent le port 10000 par défaut
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

threading.Thread(target=run_health_check, daemon=True).start()

# --- TON ROBOT REDDIT ---
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="script:1tpe_bot:v1.0 (by /u/" + os.getenv("REDDIT_USERNAME", "Zack") + ")",
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

# Configuration (à adapter selon tes besoins)
MOTS_CLES = ["argent", "revenus", "perte de poids", "musculation"]
MESSAGE = "Salut ! J'ai vu que tu cherchais une solution. J'ai testé ce guide sur 1TPE et c'est top : http://bit.ly/ton-lien"

print("🚀 MACHINE LANCEE POUR " + os.getenv("REDDIT_USERNAME", "Zack"))

def scan_reddit():
    try:
        for submission in reddit.subreddit("all").new(limit=25):
            for mot in MOTS_CLES:
                if mot in submission.title.lower():
                    print(f"Match trouvé : {submission.title}")
                    # Ajoute ici ta logique pour commenter ou MP
        print("Scan terminé, pause de 15 min...")
    except Exception as e:
        print(f"Erreur : {e}")

while True:
    scan_reddit()
    time.sleep(900) # Pause de 15 min
