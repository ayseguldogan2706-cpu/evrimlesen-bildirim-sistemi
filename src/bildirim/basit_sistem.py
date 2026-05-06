from dataclasses import dataclass
from datetime import datetime


@dataclass
class BildirimKaydi:
    kanal: str
    alici: str
    mesaj: str
    oncelik: str
    basarili: bool
    detay: str
    zaman: str


class BildirimSistemi:
    def __init__(self):
        self.gonderim_gecmisi = []
        self.sms_api_anahtari = "demo-sms-anahtari"
        self.push_uygulama_kodu = "demo-push-uygulama"

    def bildirim_gonder(self, kanal, alici, mesaj, oncelik="normal"):
        zaman = datetime.now().isoformat(timespec="seconds")

        if not alici or not mesaj:
            sonuc = BildirimKaydi(
                kanal=kanal,
                alici=alici,
                mesaj=mesaj,
                oncelik=oncelik,
                basarili=False,
                detay="Alici ve mesaj bos olamaz.",
                zaman=zaman,
            )
            self.gonderim_gecmisi.append(sonuc)
            return sonuc

        if kanal == "eposta":
            if "@" not in alici:
                basarili = False
                detay = "E-posta adresi gecersiz."
            else:
                basarili = True
                detay = f"E-posta gonderildi: {alici}"
        elif kanal == "sms":
            temiz_numara = alici.replace(" ", "")
            if not temiz_numara.startswith("+90") or len(temiz_numara) < 13:
                basarili = False
                detay = "SMS numarasi gecersiz."
            else:
                basarili = True
                detay = f"SMS API ile gonderildi: {temiz_numara}"
        elif kanal == "push":
            if len(alici) < 8:
                basarili = False
                detay = "Push cihaz anahtari gecersiz."
            else:
                basarili = True
                detay = f"Push bildirimi gonderildi: {alici}"
        else:
            basarili = False
            detay = f"Bilinmeyen bildirim kanali: {kanal}"

        if oncelik == "yuksek" and basarili:
            detay = detay + " Oncelikli olarak isaretlendi."

        sonuc = BildirimKaydi(
            kanal=kanal,
            alici=alici,
            mesaj=mesaj,
            oncelik=oncelik,
            basarili=basarili,
            detay=detay,
            zaman=zaman,
        )
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

