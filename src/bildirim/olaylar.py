from dataclasses import dataclass


@dataclass
class BildirimOlayi:
    ad: str
    sonuc: object


class OlayYayinci:
    def __init__(self):
        self.dinleyiciler = []

    def dinleyici_ekle(self, dinleyici):
        self.dinleyiciler.append(dinleyici)

    def dinleyici_cikar(self, dinleyici):
        self.dinleyiciler.remove(dinleyici)

    def yayinla(self, olay):
        for dinleyici in list(self.dinleyiciler):
            dinleyici.olay_al(olay)


class GonderimGecmisi:
    def __init__(self):
        self.kayitlar = []

    def olay_al(self, olay):
        if olay.ad == "gonderim_tamamlandi":
            self.kayitlar.append(olay.sonuc)

