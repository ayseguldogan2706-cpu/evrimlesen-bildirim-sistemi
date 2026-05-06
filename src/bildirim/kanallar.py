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


class SmsKanali(BildirimKanali):
    kanal_adi = "sms"

    def gonder(self, istek):
        if not istek.alici or not istek.mesaj:
            return GonderimSonucu.olustur(istek, False, "Alici ve mesaj bos olamaz.")
        temiz_numara = istek.alici.replace(" ", "")
        if not temiz_numara.startswith("+90") or len(temiz_numara) < 13:
            return GonderimSonucu.olustur(istek, False, "SMS numarasi gecersiz.")
        detay = f"SMS API ile gonderildi: {temiz_numara}"
        if istek.oncelik == "yuksek":
            detay = detay + " Oncelikli olarak isaretlendi."
        return GonderimSonucu.olustur(istek, True, detay)


class PushKanali(BildirimKanali):
    kanal_adi = "push"

    def gonder(self, istek):
        if not istek.alici or not istek.mesaj:
            return GonderimSonucu.olustur(istek, False, "Alici ve mesaj bos olamaz.")
        if len(istek.alici) < 8:
            return GonderimSonucu.olustur(istek, False, "Push cihaz anahtari gecersiz.")
        detay = f"Push bildirimi gonderildi: {istek.alici}"
        if istek.oncelik == "yuksek":
            detay = detay + " Oncelikli olarak isaretlendi."
        return GonderimSonucu.olustur(istek, True, detay)

