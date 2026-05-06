import pytest

from bildirim import BildirimFabrikasi, BildirimIstegi, BildirimMerkezi, BildirimSistemi
from bildirim.adapterler import SmsServisAdapteri
from bildirim.kanallar import EpostaKanali


def test_fabrika_dogru_kanal_nesnesi_olusturur():
    fabrika = BildirimFabrikasi()

    assert isinstance(fabrika.kanal_olustur("eposta"), EpostaKanali)
    assert isinstance(fabrika.kanal_olustur("sms"), SmsServisAdapteri)


def test_fabrika_bilinmeyen_kanali_reddeder():
    fabrika = BildirimFabrikasi()

    with pytest.raises(ValueError, match="Bilinmeyen bildirim kanali"):
        fabrika.kanal_olustur("faks")


def test_adapter_dis_servis_hatasini_ortak_sonuca_cevirir():
    class HataliSmsServisi:
        def sms_yolla(self, telefon, metin, api_anahtari):
            return {"basari": False, "hata": "SMS servisi kapali."}

    adapter = SmsServisAdapteri(servis=HataliSmsServisi())
    istek = BildirimIstegi("sms", "+90 555 111 2233", "Deneme")

    sonuc = adapter.gonder(istek)

    assert sonuc.basarili is False
    assert sonuc.detay == "SMS servisi kapali."


def test_facade_eposta_gonderimini_sadelestirir():
    merkez = BildirimMerkezi()

    sonuc = merkez.eposta_gonder("aysegul@example.com", "Merhaba")

    assert sonuc.basarili is True
    assert sonuc.kanal == "eposta"
    assert len(merkez.gecmis()) == 1


def test_observer_gonderim_olayini_dinleyiciye_iletir():
    class TestDinleyici:
        def __init__(self):
            self.olaylar = []

        def olay_al(self, olay):
            self.olaylar.append(olay)

    sistem = BildirimSistemi()
    dinleyici = TestDinleyici()
    sistem.dinleyici_ekle(dinleyici)

    sonuc = sistem.bildirim_gonder("eposta", "aysegul@example.com", "Merhaba")

    assert dinleyici.olaylar[0].ad == "gonderim_tamamlandi"
    assert dinleyici.olaylar[0].sonuc == sonuc


def test_strategy_yeni_davranis_eklerken_mevcut_kodu_degistirmez():
    class MesajiBuyutenStrateji:
        def gonder(self, sistem, kanal, alicilar, mesaj, oncelik):
            sonuclar = []
            for alici in alicilar:
                sonuclar.append(sistem.bildirim_gonder(kanal, alici, mesaj.upper(), oncelik))
            return sonuclar

    merkez = BildirimMerkezi(strateji=MesajiBuyutenStrateji())

    sonuc = merkez.eposta_gonder("aysegul@example.com", "ocp gosterimi")

    assert sonuc.basarili is True
    assert sonuc.mesaj == "OCP GOSTERIMI"


def test_gecersiz_girdi_basarili_sonuc_uretmez():
    merkez = BildirimMerkezi()

    sonuc = merkez.sms_gonder("", "Mesaj")

    assert sonuc.basarili is False
    assert sonuc.detay == "Alici ve mesaj bos olamaz."

