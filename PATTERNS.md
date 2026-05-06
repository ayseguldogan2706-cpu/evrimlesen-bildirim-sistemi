# PATTERNS.md

Bu dosya her fazda uygulanan tasarim oruntulerini aciklamak icin guncellenecektir.

## Faz 0

Faz 0'da bilerek tasarim oruntusu uygulanmadi. Amac, baslangic kodundaki sorunlari gorup sonraki fazlarda bu sorunlari kontrollu sekilde cozmekti.

## Faz 1 - Factory Method

**Nerede kullanildi?**  
`BildirimFabrikasi`, istenen kanal adina gore `EpostaKanali`, `SmsKanali` veya `PushKanali` nesnesi olusturur. `BildirimSistemi` artik kanal siniflarini dogrudan bilmek yerine fabrikadan nesne ister.

**Neden secildi?**  
Baslangic kodunda hangi bildirim kanalinin kullanilacagina `if-elif` zinciriyle karar veriliyordu. Bu karar ana gonderim metodunun icinde oldugu icin yeni kanal eklemek mevcut metodu buyutuyordu. Factory Method, nesne olusturma sorumlulugunu daha merkezi ve degistirilebilir bir yere tasidi.

**Ne kazandirdi?**  
Kanal secimi ile gonderim akisi birbirinden ayrildi. `BildirimSistemi` daha kucuk ve okunur hale geldi. Yeni kanal ekleme ihtiyaci dogdugunda ana gonderim akisini degistirmek yerine fabrika kaydi guncellenebilir.

## Faz 2 - Adapter

**Nerede kullanildi?**  
`SmsServisAdapteri` ve `PushServisAdapteri`, `HariciSmsServisi` ve `HariciPushServisi` siniflarini ortak `BildirimKanali` arayuzune uydurur.

**Neden secildi?**  
Dis servislerin metot adlari ve donus bicimleri sistemin bekledigi `gonder(istek)` yapisina uymuyordu. Adapter, dis servisin ic yapisini ana sisteme yaymadan bu farki kapatmak icin secildi.

**Ne kazandirdi?**  
Sistem dis SMS ve push servislerinin ayrintilarini bilmeden bildirim gonderebilir hale geldi. Dis servis degistiginde ana bildirim akisi yerine sadece adapter sinifi etkilenir.

## Faz 2 - Facade

**Nerede kullanildi?**  
`BildirimMerkezi`, e-posta, SMS, push ve toplu gonderim islemlerini tek bir kolay kullanim noktasi olarak sunar.

**Neden secildi?**  
Factory, kanal siniflari ve adapterler sistemin ic tasarimini olusturur. Kullanici veya demo kodunun bu ayrintilari bilmesi gereksizdir. Facade, bu karmaşayi daha sade bir arayuz arkasina alir.

**Ne kazandirdi?**  
Demo ve dis kullanim kodu daha okunur hale geldi. Bildirim gondermek isteyen taraf `BildirimMerkezi` uzerinden islem yapar; fabrika ve adapter ayrintilari icerde kalir.
