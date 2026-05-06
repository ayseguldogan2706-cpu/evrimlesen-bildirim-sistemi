class HariciSmsServisi:
    def sms_yolla(self, telefon, metin, api_anahtari):
        if not api_anahtari:
            return {"basari": False, "hata": "SMS API anahtari yok."}
        return {"basari": True, "takip_no": f"SMS-{telefon[-4:]}"}


class HariciPushServisi:
    def push_yayinla(self, cihaz_anahtari, baslik, icerik, uygulama_kodu):
        if not uygulama_kodu:
            return {"durum": "red", "sebep": "Push uygulama kodu yok."}
        return {"durum": "kabul", "islem_no": f"PUSH-{cihaz_anahtari[-5:]}"}

