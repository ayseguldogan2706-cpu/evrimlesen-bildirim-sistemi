from abc import ABC, abstractmethod


class GonderimStratejisi(ABC):
    @abstractmethod
    def gonder(self, sistem, kanal, alicilar, mesaj, oncelik):
        raise NotImplementedError


class SiraliGonderimStratejisi(GonderimStratejisi):
    def gonder(self, sistem, kanal, alicilar, mesaj, oncelik):
        sonuclar = []
        for alici in alicilar:
            sonuclar.append(sistem.bildirim_gonder(kanal, alici, mesaj, oncelik))
        return sonuclar


class OncelikliGonderimStratejisi(GonderimStratejisi):
    def gonder(self, sistem, kanal, alicilar, mesaj, oncelik):
        sonuclar = []
        for alici in alicilar:
            sonuclar.append(sistem.bildirim_gonder(kanal, alici, mesaj, "yuksek"))
        return sonuclar

