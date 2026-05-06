from .fabrika import BildirimFabrikasi
from .modeller import BildirimIstegi, GonderimSonucu


class BildirimSistemi:
    def __init__(self, fabrika=None):
        self.gonderim_gecmisi = []
        self.fabrika = fabrika or BildirimFabrikasi()

    def bildirim_gonder(self, kanal, alici, mesaj, oncelik="normal"):
        istek = BildirimIstegi(kanal=kanal, alici=alici, mesaj=mesaj, oncelik=oncelik)
        try:
            kanal_nesnesi = self.fabrika.kanal_olustur(kanal)
            sonuc = kanal_nesnesi.gonder(istek)
        except ValueError as hata:
            sonuc = GonderimSonucu.olustur(istek, False, str(hata))
        self.gonderim_gecmisi.append(sonuc)
        return sonuc

    def toplu_bildirim_gonder(self, kanal, alicilar, mesaj, oncelik="normal"):
        sonuclar = []
        for alici in alicilar:
            sonuclar.append(self.bildirim_gonder(kanal, alici, mesaj, oncelik))
        return sonuclar

    def gecmis_yazdir(self):
        for kayit in self.gonderim_gecmisi:
            durum = "basarili" if kayit.basarili else "basarisiz"
            print(f"{kayit.zaman} | {kayit.kanal} | {durum} | {kayit.detay}")
