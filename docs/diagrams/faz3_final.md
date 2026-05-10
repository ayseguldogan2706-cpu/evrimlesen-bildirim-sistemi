# Faz 3 Final Mimari Diyagrami

## Once

```mermaid
classDiagram
    class BildirimMerkezi {
        +eposta_gonder(alici, mesaj, oncelik)
        +sms_gonder(alici, mesaj, oncelik)
        +push_gonder(alici, mesaj, oncelik)
        +bildirim_gonder(kanal, alici, mesaj, oncelik)
        +toplu_gonder(kanal, alicilar, mesaj, oncelik)
    }

    class BildirimSistemi {
        +bildirim_gonder(kanal, alici, mesaj, oncelik)
        +toplu_bildirim_gonder(kanal, alicilar, mesaj, oncelik)
    }

    class BildirimFabrikasi {
        +kanal_olustur(kanal)
    }

    class BildirimKanali {
        <<abstract>>
        +gonder(istek)
    }

    class EpostaKanali
    class SmsServisAdapteri
    class PushServisAdapteri
    class HariciSmsServisi
    class HariciPushServisi

    BildirimMerkezi --> BildirimSistemi : Facade
    BildirimSistemi --> BildirimFabrikasi
    BildirimFabrikasi --> BildirimKanali
    BildirimKanali <|-- EpostaKanali
    BildirimKanali <|-- SmsServisAdapteri
    BildirimKanali <|-- PushServisAdapteri
    SmsServisAdapteri --> HariciSmsServisi : Adapter
    PushServisAdapteri --> HariciPushServisi : Adapter
```

Faz 2 sonunda Adapter ve Facade eklenmisti. Ancak gonderim sonrasi tepkiler ve farkli gonderim politikalari henuz ayri davranissal oruntulerle genisletilebilir hale getirilmemisti.

## Sonra

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

Final yapida kullanici `BildirimMerkezi` ile calisir. Merkez, gonderim stratejisini kullanir; sistem kanal nesnesini fabrikadan alir; adapterler dis servisleri uyumlar; Observer yapisi gonderim olaylarini dinleyicilere bildirir.
