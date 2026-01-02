import time

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
