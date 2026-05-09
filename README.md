# A - Bildirim Sistemi

Bu projede **A - Bildirim Sistemi** konusu secildi. Baslangic kodunda e-posta, SMS ve push bildirimleri tek bir sinif icinde `if-elif` zincirleriyle yonetilir. Bu konu, tasarim oruntulerinin neden gerekli oldugunu gostermek icin uygundur; cunku yeni bir bildirim turu veya gonderim kurali eklemek baslangicta mevcut kodu degistirmeyi zorunlu kilar.

**Ogrenci:** 221229031 Ayşegül Doğan  
**Ders:** Yazilim Tasarim Oruntuleri  
**Ogretim Uyesi:** Dr. Öğr. Üyesi Burak YILMAZ

## Proje Durumu

Bu repo, bildirim sisteminin bilincli olarak sorunlu bir baslangic kodundan daha genisletilebilir bir mimariye evrilmesini gosterir. Sistem e-posta, SMS ve push bildirimi gonderebilir; dis servisleri uyarlayabilir; gonderim olaylarini dinleyicilere yayinlayabilir; gonderim davranisini strateji ile degistirebilir.

## Calistirma

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e . -r requirements-dev.txt
python -m bildirim.demo
```

Sistemde `python3-venv` yoksa test icin su komut da kullanilabilir:

```bash
python3 -m pip install --user -e . -r requirements-dev.txt
python3 -m pytest -q
```

## Test

```bash
pytest -q
```

GitHub Actions, her push ve pull request icin ayni testleri calistirir.

## Evrimlesme Akisi

- Faz 0: `BildirimSistemi`, kanal secimi, dogrulama, gonderim ve gecmis tutma islerini tek sinifta topluyordu. Bu sorunlar `PROBLEMS.md` icinde listelendi.
- Faz 1: Factory Method ile kanal nesnesi olusturma sorumlulugu ana gonderim akisindan ayrildi.
- Faz 2: Adapter ile SMS/push dis servisleri ortak arayuze uyarlandi; Facade ile sistemin dis kullanimi sade hale getirildi.
- Faz 3: Observer ile gonderim sonrasi tepkiler ayrildi; Strategy ile gonderim politikasi degistirilebilir hale getirildi ve OCP testle gosterildi.

## Kullanilan Tasarim Oruntuleri

- **Factory Method:** Bildirim kanali nesnesi olusturma sorumlulugu `BildirimFabrikasi` sinifina tasindi.
- **Adapter:** SMS ve push icin ornek dis servisler ortak bildirim arayuzune uyarlandi.
- **Facade:** `BildirimMerkezi`, sistemin ana kullanim noktasi olarak eklendi.
- **Observer:** Gonderim tamamlandiginda olay yayinlanarak gecmis ve diger dinleyiciler bilgilendirildi.
- **Strategy:** Gonderim politikasi `BildirimMerkezi` icinde degistirilebilir hale getirildi.

## Mimari Diyagram

```mermaid
classDiagram
    class BildirimMerkezi {
        +strateji_degistir(strateji)
        +eposta_gonder(alici, mesaj, oncelik)
        +sms_gonder(alici, mesaj, oncelik)
        +push_gonder(alici, mesaj, oncelik)
        +toplu_gonder(kanal, alicilar, mesaj, oncelik)
    }

    class GonderimStratejisi {
        <<abstract>>
        +gonder(sistem, kanal, alicilar, mesaj, oncelik)
    }

    class SiraliGonderimStratejisi
    class OncelikliGonderimStratejisi
    class BildirimSistemi
    class BildirimFabrikasi
    class BildirimKanali {
        <<abstract>>
        +gonder(istek)
    }
    class EpostaKanali
    class SmsServisAdapteri
    class PushServisAdapteri
    class OlayYayinci {
        +dinleyici_ekle(dinleyici)
        +yayinla(olay)
    }
    class GonderimGecmisi {
        +olay_al(olay)
    }
    class HariciSmsServisi
    class HariciPushServisi

    BildirimMerkezi --> GonderimStratejisi : Strategy
    GonderimStratejisi <|-- SiraliGonderimStratejisi
    GonderimStratejisi <|-- OncelikliGonderimStratejisi
    BildirimMerkezi --> BildirimSistemi : Facade
    BildirimSistemi --> BildirimFabrikasi : Factory Method
    BildirimSistemi --> OlayYayinci : Observer
    OlayYayinci --> GonderimGecmisi
    BildirimFabrikasi --> BildirimKanali
    BildirimKanali <|-- EpostaKanali
    BildirimKanali <|-- SmsServisAdapteri
    BildirimKanali <|-- PushServisAdapteri
    SmsServisAdapteri --> HariciSmsServisi : Adapter
    PushServisAdapteri --> HariciPushServisi : Adapter
```

## Acik/Kapali Prensibi

Testlerde yeni bir gonderim stratejisi sadece test dosyasinda tanimlanir ve `BildirimMerkezi` icine verilir. Mevcut `BildirimMerkezi`, `BildirimSistemi` veya kanal siniflari degistirilmeden yeni davranis eklenebilir. Bu durum, sistemin en az bir noktada Acik/Kapali Prensibi'ne uygun hale geldigini gosterir.
