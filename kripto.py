import requests
from bs4 import BeautifulSoup

def fiyatlari_cek(url="https://coinmarketcap.com/", coin_adi="Bitcoin"):
    headers = {"User-Agent": "Mozilla/5.0"}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    satir = soup.find("p", string=coin_adi)

    if satir is None:
        return None

    satir = satir.find_parent("tr")
    fiyat_td = satir.find_all("td")[3]
    return fiyat_td.text.strip()



