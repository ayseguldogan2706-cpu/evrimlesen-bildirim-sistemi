# A - Bildirim Sistemi

Bu projede **A - Bildirim Sistemi** konusu secildi. Baslangic kodunda e-posta, SMS ve push bildirimleri tek bir sinif icinde `if-elif` zincirleriyle yonetilir. Bu konu, tasarim oruntulerinin neden gerekli oldugunu gostermek icin uygundur; cunku yeni bir bildirim turu veya gonderim kurali eklemek baslangicta mevcut kodu degistirmeyi zorunlu kilar.

**Ogrenci:** 221229031 Ayşegül Doğan  
**Ders:** Yazilim Tasarim Oruntuleri  
**Ogretim Uyesi:** Dr. Öğr. Üyesi Burak YILMAZ

## Proje Durumu

Bu dal, Faz 0 baslangic kodunu icerir. Kod bilerek sade ve tasarim oruntusu kullanmadan yazilmistir. Amac, sonraki fazlarda tasarim sorunlarini adim adim cozmek ve sistemin nasil evrimlestigini gostermektir.

## Calistirma

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e . -r requirements-dev.txt
python -m bildirim.demo
```

## Fazlar

- Faz 0: Baslangic kodu ve tasarim sorunlari analizi.
- Faz 1: Creational oruntu ile nesne olusturma sorumlulugunun ayrilmasi.
- Faz 2: Structural oruntuler ile dis servis uyumu ve kullanim kolayligi.
- Faz 3: Behavioral oruntuler ile genisletilebilir davranis yapisi.

