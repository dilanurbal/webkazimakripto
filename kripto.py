import requests
from bs4 import BeautifulSoup

def fiyatlari_cek():
    url = "https://coinmarketcap.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    def fiyat_bul(coin_adi):
        satir = soup.find("p", string=coin_adi).find_parent("tr")
        fiyat_td = satir.find_all("td")[3]   # 3. sütun fiyat
        fiyat = fiyat_td.text.strip()
        return fiyat

    btc = fiyat_bul("Bitcoin")
    eth = fiyat_bul("Ethereum")
    bnb = fiyat_bul("BNB")

    return {
        "bitcoin": btc,
        "ethereum": eth,
        "bnb": bnb
    }
