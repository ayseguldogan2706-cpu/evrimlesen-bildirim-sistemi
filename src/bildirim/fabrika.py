from .adapterler import PushServisAdapteri, SmsServisAdapteri
from .kanallar import EpostaKanali


class BildirimFabrikasi:
    def __init__(self):
        self.kanal_siniflari = {
            "eposta": EpostaKanali,
            "sms": SmsServisAdapteri,
            "push": PushServisAdapteri,
        }

    def kanal_olustur(self, kanal):
        try:
            return self.kanal_siniflari[kanal]()
        except KeyError as hata:
            raise ValueError(f"Bilinmeyen bildirim kanali: {kanal}") from hata

    def kanal_ekle(self, kanal, kanal_sinifi):
        self.kanal_siniflari[kanal] = kanal_sinifi
