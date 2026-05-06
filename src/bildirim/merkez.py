from .basit_sistem import BildirimSistemi


class BildirimMerkezi:
    def __init__(self, sistem=None):
        self.sistem = sistem or BildirimSistemi()

    def eposta_gonder(self, alici, mesaj, oncelik="normal"):
        return self.sistem.bildirim_gonder("eposta", alici, mesaj, oncelik)

    def sms_gonder(self, alici, mesaj, oncelik="normal"):
        return self.sistem.bildirim_gonder("sms", alici, mesaj, oncelik)

    def push_gonder(self, alici, mesaj, oncelik="normal"):
        return self.sistem.bildirim_gonder("push", alici, mesaj, oncelik)

    def bildirim_gonder(self, kanal, alici, mesaj, oncelik="normal"):
        return self.sistem.bildirim_gonder(kanal, alici, mesaj, oncelik)

    def toplu_gonder(self, kanal, alicilar, mesaj, oncelik="normal"):
        return self.sistem.toplu_bildirim_gonder(kanal, alicilar, mesaj, oncelik)

    def gecmis(self):
        return list(self.sistem.gonderim_gecmisi)

    def gecmis_yazdir(self):
        self.sistem.gecmis_yazdir()
