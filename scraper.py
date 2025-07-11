import requests, datetime, os

URL = "https://https://www.win2day.at/promotions-gewinnspiele/gewinner-des-tages"          # ← deine Seite
PROXY = {
    "http":  "http://195.225.232.248:3128",   # ← AT‑Proxy
    "https": "http://195.225.232.248:3128",
}

html   = requests.get(URL, proxies=PROXY, timeout=20).text
stamp  = datetime.datetime.utcnow().strftime("%Y-%m-%d")
fname  = f"snapshot_{stamp}.html"

os.makedirs("snapshots", exist_ok=True)
with open(f"snapshots/{fname}", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Gespeichert: {fname}")
