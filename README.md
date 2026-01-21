# Canlı Kripto Fiyat Takip Uygulaması

Bu proje, CoinMarketCap sitesinden kripto para fiyatlarını çekerek WebSocket üzerinden tarayıcıda canlı olarak gösteren bir uygulamadır. Bitcoin, Ethereum ve BNB fiyatları anlık olarak görüntülenebilir.

Kullanılan Teknolojiler:  
Python, Requests, BeautifulSoup, WebSockets, HTML, TailwindCSS

Kurulum:  
Gerekli kütüphaneleri yüklemek için:  
pip install -r requirements.txt

Çalıştırma:  
WebSocket sunucusunu başlatın:  
python server.py  
Ardından index.html dosyasını tarayıcıda açın. Canlı fiyatları ekranda göreceksiniz.

Dosya Yapısı:
index.html  
ws_server.py
kripto.py  
Veriler.py  
veriler.json  
requirements.txt  
README.md  

Fonksiyonlar sabit değerler yerine parametre alacak şekilde yazılmıştır:  
def fiyatlari_cek(url="https://coinmarketcap.com/", coin_adi="Bitcoin")  
Bu sayede farklı coin’ler kolayca çekilebilir ve kod daha esnek olur.

Not:  
CoinMarketCap site yapısı değişirse scraper çalışmayabilir. Daha stabil bir sistem için API kullanımı önerilir.

Geliştirici:  
Dilanur Bal  
Bilgisayar Mühendisliği Öğrencisi
