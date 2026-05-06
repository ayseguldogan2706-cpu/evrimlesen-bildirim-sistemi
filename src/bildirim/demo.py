from .basit_sistem import BildirimSistemi


def main():
    sistem = BildirimSistemi()
    ornekler = [
        ("eposta", "aysegul@example.com", "Odev bildirimi hazir.", "normal"),
        ("sms", "+90 555 111 2233", "Teslim tarihi yaklasiyor.", "yuksek"),
        ("push", "cihaz-12345", "Yeni bildirim var.", "normal"),
        ("faks", "02120000000", "Desteklenmeyen kanal.", "normal"),
    ]

    for kanal, alici, mesaj, oncelik in ornekler:
        sonuc = sistem.bildirim_gonder(kanal, alici, mesaj, oncelik)
        durum = "BASARILI" if sonuc.basarili else "BASARISIZ"
        print(f"{durum}: {sonuc.detay}")

    print("\nGonderim gecmisi")
    sistem.gecmis_yazdir()


if __name__ == "__main__":
    main()

