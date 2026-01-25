from kripto import fiyatlari_cek
from Veriler import kaydet_json

def main():
    print("Veriler çekiliyor...")

    fiyatlar = {
        "bitcoin": fiyatlari_cek(coin_adi="Bitcoin"),
        "ethereum": fiyatlari_cek(coin_adi="Ethereum"),
        "bnb": fiyatlari_cek(coin_adi="BNB")
    }

    print("Fiyatlar alındı:", fiyatlar)

    print("JSON dosyasına kaydediliyor...")
    kaydet_json(fiyatlar)

if __name__ == '__main__':
    main()
