from .fabrika import BildirimFabrikasi
from .modeller import BildirimIstegi, GonderimSonucu
from .olaylar import BildirimOlayi, GonderimGecmisi, OlayYayinci


class BildirimSistemi:
    def __init__(self, fabrika=None, olay_yayinci=None):
        self.fabrika = fabrika or BildirimFabrikasi()
        self.olay_yayinci = olay_yayinci or OlayYayinci()
        self.gecmis_dinleyicisi = GonderimGecmisi()
        self.olay_yayinci.dinleyici_ekle(self.gecmis_dinleyicisi)
        self.gonderim_gecmisi = self.gecmis_dinleyicisi.kayitlar

    def bildirim_gonder(self, kanal, alici, mesaj, oncelik="normal"):
        istek = BildirimIstegi(kanal=kanal, alici=alici, mesaj=mesaj, oncelik=oncelik)
        try:
            kanal_nesnesi = self.fabrika.kanal_olustur(kanal)
            sonuc = kanal_nesnesi.gonder(istek)
        except ValueError as hata:
            sonuc = GonderimSonucu.olustur(istek, False, str(hata))
        self.olay_yayinci.yayinla(BildirimOlayi("gonderim_tamamlandi", sonuc))
        return sonuc

    def dinleyici_ekle(self, dinleyici):
        self.olay_yayinci.dinleyici_ekle(dinleyici)

    def dinleyici_cikar(self, dinleyici):
        self.olay_yayinci.dinleyici_cikar(dinleyici)

    def toplu_bildirim_gonder(self, kanal, alicilar, mesaj, oncelik="normal"):
        sonuclar = []
        for alici in alicilar:
            sonuclar.append(self.bildirim_gonder(kanal, alici, mesaj, oncelik))
        return sonuclar

    def gecmis_yazdir(self):
        for kayit in self.gonderim_gecmisi:
            durum = "basarili" if kayit.basarili else "basarisiz"
            print(f"{kayit.zaman} | {kayit.kanal} | {durum} | {kayit.detay}")
