import praw
import time
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- 1. GARDE LE ROBOT EN VIE SUR RENDER ---
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ROBOT ACTIF")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# --- 2. CONNEXION A REDDIT ---
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="script:1tpe_bot:v1.0",
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

# --- 3. CONFIGURATION DE TA CHASSE ---
MOTS_CLES = ["argent", "revenus", "perdre du poids", "musculation"]
MESSAGE = "Salut ! J'ai vu que tu cherchais une solution. J'ai trouvé ce guide sur 1TPE qui aide bien : http://bit.ly/ton-lien-ici"

print("🚀 MACHINE LANCEE ET CONNECTEE A REDDIT !")

while True:
    try:
        # Le robot regarde les 25 derniers posts sur tout Reddit
        for submission in reddit.subreddit("all").new(limit=25):
            titre = submission.title.lower()
            for mot in MOTS_CLES:
                if mot in titre:
                    print(f"🎯 Cible trouvée : {submission.title}")
                    # Ici tu peux ajouter submission.reply(MESSAGE) plus tard
        
        print("Scan fini. Pause de 15 minutes...")
        time.sleep(900) 
    except Exception as e:
        print(f"Petite erreur : {e}")
        time.sleep(60)
