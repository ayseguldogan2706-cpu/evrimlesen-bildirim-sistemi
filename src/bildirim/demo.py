from .merkez import BildirimMerkezi
from .stratejiler import OncelikliGonderimStratejisi


def main():
    merkez = BildirimMerkezi()
    sonuclar = [
        merkez.eposta_gonder("aysegul@example.com", "Odev bildirimi hazir."),
        merkez.sms_gonder("+90 555 111 2233", "Teslim tarihi yaklasiyor.", "yuksek"),
        merkez.push_gonder("cihaz-12345", "Yeni bildirim var."),
        merkez.bildirim_gonder("faks", "02120000000", "Desteklenmeyen kanal."),
    ]

    merkez.strateji_degistir(OncelikliGonderimStratejisi())
    sonuclar.append(merkez.eposta_gonder("ogretmen@example.com", "Faz 3 kontrol bildirimi."))

    for sonuc in sonuclar:
        durum = "BASARILI" if sonuc.basarili else "BASARISIZ"
        print(f"{durum}: {sonuc.detay}")

    print("\nGonderim gecmisi")
    merkez.gecmis_yazdir()


if __name__ == "__main__":
    main()
