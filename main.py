import os
import time
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# 1. SERVEUR DE SURVIE POUR RENDER
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ROBOT ACTIF")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    print(f"Serveur lancé sur le port {port}")
    server.serve_forever()

# Lancement du serveur dans un coin
threading.Thread(target=run_server, daemon=True).start()

# 2. LOGIQUE DU ROBOT
print("🚀 TENTATIVE DE CONNEXION REDDIT...")

# On affiche juste un message pour tester
while True:
    print("Zack, le robot tourne et attend tes instructions !")
    time.sleep(60)
