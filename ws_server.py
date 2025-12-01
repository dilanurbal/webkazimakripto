import asyncio
import websockets
import requests
from bs4 import BeautifulSoup
import json

# ---- CANLI FİYAT ÇEKME ----
def fiyatlari_cek():
    url = "https://coinmarketcap.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    def fiyat_bul(coin_adi):
        satir = soup.find("p", string=coin_adi).find_parent("tr")
        fiyat_td = satir.find_all("td")[3]
        return fiyat_td.text.strip()

    return {
        "bitcoin": fiyat_bul("Bitcoin"),
        "ethereum": fiyat_bul("Ethereum"),
        "bnb": fiyat_bul("BNB")
    }

# ---- WEBSOCKET YAYIN ----
async def yayin(websocket):
    while True:
        try:
            fiyatlar = fiyatlari_cek()
            await websocket.send(json.dumps(fiyatlar))
        except Exception as e:
            print("Hata:", e)

        await asyncio.sleep(3)  # 3 saniyede bir güncelle

async def main():
    print("WebSocket sunucusu çalışıyor: ws://localhost:8001")
    async with websockets.serve(yayin, "localhost", 8001):
        await asyncio.Future()  # sonsuza kadar çalıştırır

asyncio.run(main())
