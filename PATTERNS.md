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
