import requests

TOKEN = "SEU TOKEN AQUI"
CHAT_ID = "-1003877210073"

mensagem = """
🔥 OFERTA IMPERDÍVEL 🔥

💰 Preço baixou agora!
📦 Mercado Livre com entrega rápida

👉 Compre aqui:
https://SEU_LINK_DE_AFILIADO

⚠️ Pode acabar a qualquer momento!
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": mensagem
})
