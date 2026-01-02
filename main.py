from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Petit serveur pour garder Render content (Gratuit)
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Robot en ligne")

def run_health_check():
    server = HTTPServer(('0.0.0.0', 10000), HealthCheckHandler)
    server.serve_forever()

# Lance le serveur dans un fil séparé
threading.Thread(target=run_health_check, daemon=True).start() import time

# TES INFOS
ID_1TPE = "zackbizzza"
REDDIT_USER = "Academic_Painting866"
REDDIT_PASS = "Mirza76200"

def bot_run():
    print(f"🚀 MACHINE LANCEE POUR {ID_1TPE}")
    print(f"Connecté à Reddit : {REDDIT_USER}")
    
    while True:
        print(f"[{time.strftime('%H:%M:%S')}] Scan en cours...")
        time.sleep(1800)

if __name__ == "__main__":
    bot_run()
