import subprocess
import time
import requests

def internet_working():
    try:
        r = requests.get(
            "https://www.google.com/generate_204",
            timeout=5
        )
        return r.status_code == 204
    except:
        return False

while True:
    if internet_working():
        print("✅ Internet OK")
    else:
        print("🔒 Internet blocked. Trying login...")
        subprocess.run(["python", "login.py"])

    time.sleep(60)