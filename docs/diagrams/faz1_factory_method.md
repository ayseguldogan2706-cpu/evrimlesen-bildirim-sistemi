# Faz 1 Factory Method UML

## Once

```mermaid
classDiagram
    class BildirimSistemi {
        +bildirim_gonder(kanal, alici, mesaj, oncelik)
    }
    class BildirimKaydi
    BildirimSistemi --> BildirimKaydi
```

Baslangicta `BildirimSistemi`, kanal secimini ve kanal davranislarini kendi icinde tutuyordu.

## Sonra

```mermaid
classDiagram
    class BildirimSistemi {
        +bildirim_gonder(kanal, alici, mesaj, oncelik)
    }
    class BildirimFabrikasi {
        +kanal_olustur(kanal)
        +kanal_ekle(kanal, kanal_sinifi)
    }
    class BildirimKanali {
        <<abstract>>
        +gonder(istek)
    }
    class EpostaKanali {
        +gonder(istek)
    }
    class SmsKanali {
        +gonder(istek)
    }
    class PushKanali {
        +gonder(istek)
    }
    class BildirimIstegi
    class GonderimSonucu

    BildirimSistemi --> BildirimFabrikasi
    BildirimFabrikasi --> BildirimKanali
    BildirimKanali <|-- EpostaKanali
    BildirimKanali <|-- SmsKanali
    BildirimKanali <|-- PushKanali
    BildirimKanali --> BildirimIstegi
    BildirimKanali --> GonderimSonucu
```

Factory Method ile hangi kanal nesnesinin olusturulacagi `BildirimFabrikasi` sinifina tasindi.

