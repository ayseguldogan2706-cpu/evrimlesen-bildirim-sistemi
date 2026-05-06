from .basit_sistem import BildirimSistemi
from .stratejiler import SiraliGonderimStratejisi


class BildirimMerkezi:
    def __init__(self, sistem=None, strateji=None):
        self.sistem = sistem or BildirimSistemi()
        self.strateji = strateji or SiraliGonderimStratejisi()

    def eposta_gonder(self, alici, mesaj, oncelik="normal"):
        return self.bildirim_gonder("eposta", alici, mesaj, oncelik)

    def sms_gonder(self, alici, mesaj, oncelik="normal"):
        return self.bildirim_gonder("sms", alici, mesaj, oncelik)

    def push_gonder(self, alici, mesaj, oncelik="normal"):
        return self.bildirim_gonder("push", alici, mesaj, oncelik)

    def bildirim_gonder(self, kanal, alici, mesaj, oncelik="normal"):
        return self.strateji.gonder(self.sistem, kanal, [alici], mesaj, oncelik)[0]

    def toplu_gonder(self, kanal, alicilar, mesaj, oncelik="normal"):
        return self.strateji.gonder(self.sistem, kanal, alicilar, mesaj, oncelik)

    def strateji_degistir(self, strateji):
        self.strateji = strateji

    def gecmis(self):
        return list(self.sistem.gonderim_gecmisi)

    def gecmis_yazdir(self):
        self.sistem.gecmis_yazdir()
