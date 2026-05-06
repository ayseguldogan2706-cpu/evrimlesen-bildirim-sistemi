from abc import ABC, abstractmethod

from .modeller import GonderimSonucu


class BildirimKanali(ABC):
    kanal_adi = "bilinmeyen"

    @abstractmethod
    def gonder(self, istek):
        raise NotImplementedError


class EpostaKanali(BildirimKanali):
    kanal_adi = "eposta"

    def gonder(self, istek):
        if not istek.alici or not istek.mesaj:
            return GonderimSonucu.olustur(istek, False, "Alici ve mesaj bos olamaz.")
        if "@" not in istek.alici:
            return GonderimSonucu.olustur(istek, False, "E-posta adresi gecersiz.")
        detay = f"E-posta gonderildi: {istek.alici}"
        if istek.oncelik == "yuksek":
            detay = detay + " Oncelikli olarak isaretlendi."
        return GonderimSonucu.olustur(istek, True, detay)


