from .dis_servisler import HariciPushServisi, HariciSmsServisi
from .kanallar import BildirimKanali
from .modeller import GonderimSonucu


class SmsServisAdapteri(BildirimKanali):
    kanal_adi = "sms"

    def __init__(self, servis=None, api_anahtari="demo-sms-anahtari"):
        self.servis = servis or HariciSmsServisi()
        self.api_anahtari = api_anahtari

    def gonder(self, istek):
        if not istek.alici or not istek.mesaj:
            return GonderimSonucu.olustur(istek, False, "Alici ve mesaj bos olamaz.")

        temiz_numara = istek.alici.replace(" ", "")
        if not temiz_numara.startswith("+90") or len(temiz_numara) < 13:
            return GonderimSonucu.olustur(istek, False, "SMS numarasi gecersiz.")

        cevap = self.servis.sms_yolla(temiz_numara, istek.mesaj, self.api_anahtari)
        if not cevap["basari"]:
            return GonderimSonucu.olustur(istek, False, cevap["hata"])

        detay = f"SMS servisi ile gonderildi: {cevap['takip_no']}"
        if istek.oncelik == "yuksek":
            detay = detay + " Oncelikli olarak isaretlendi."
        return GonderimSonucu.olustur(istek, True, detay)


class PushServisAdapteri(BildirimKanali):
    kanal_adi = "push"

    def __init__(self, servis=None, uygulama_kodu="demo-push-uygulama"):
        self.servis = servis or HariciPushServisi()
        self.uygulama_kodu = uygulama_kodu

    def gonder(self, istek):
        if not istek.alici or not istek.mesaj:
            return GonderimSonucu.olustur(istek, False, "Alici ve mesaj bos olamaz.")
        if len(istek.alici) < 8:
            return GonderimSonucu.olustur(istek, False, "Push cihaz anahtari gecersiz.")

        cevap = self.servis.push_yayinla(istek.alici, "Bildirim", istek.mesaj, self.uygulama_kodu)
        if cevap["durum"] != "kabul":
            return GonderimSonucu.olustur(istek, False, cevap["sebep"])

        detay = f"Push servisi ile gonderildi: {cevap['islem_no']}"
        if istek.oncelik == "yuksek":
            detay = detay + " Oncelikli olarak isaretlendi."
        return GonderimSonucu.olustur(istek, True, detay)

