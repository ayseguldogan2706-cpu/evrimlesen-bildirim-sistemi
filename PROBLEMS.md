# PROBLEMS.md

## Faz 0 - Baslangic Kodunda Gordugum Tasarim Sorunlari

1. **Tek sinif cok fazla is yapiyor.** `BildirimSistemi` hem kanal secimini, hem dogrulamayi, hem gonderimi, hem de gecmis tutmayi yonetiyor. Bu durum sinifin degismesine sebep olabilecek nedenleri artiriyor.

2. **Kanal secimi `if-elif` zincirine bagli.** Yeni bir bildirim kanali eklemek icin `bildirim_gonder` metodunun icine yeni bir kosul eklemek gerekiyor. Bu, mevcut calisan kodu degistirerek hata yapma riskini artiriyor.

3. **Nesne olusturma ve karar verme ayni yerde.** Sistem hangi kanal icin hangi davranisin kullanilacagina metot icinde karar veriyor. Bu sorumluluk ayri bir fabrika yapisina tasinmadigi icin kod esnek degil.

4. **Dis servis farklari kodun icine gomulu.** SMS API anahtari ve push uygulama kodu ayni sinifta tutuluyor. Gercek bir SMS veya push servisi farkli metotlarla calisirsa bu sinif daha da buyur.

5. **Gonderim sonrasi olaylar genisletilebilir degil.** Basarili veya basarisiz gonderimden sonra loglama, raporlama ya da baska bir islem eklemek icin yine ana metodu degistirmek gerekir.

6. **Gonderim kurallari sabit davranisa bagli.** Oncelikli gonderim veya toplu gonderim gibi kurallar ana sinifin icine gomulmus durumda. Farkli bir gonderim politikasi eklemek icin mevcut kod degismek zorunda kalir.

7. **Test etmek zorlasiyor.** Her kanal ayni metot icinde oldugu icin sadece SMS veya sadece e-posta davranisini tek basina test etmek daha zordur. Kucuk bir degisiklik birden fazla kanali etkileyebilir.

## AI ile Karsilastirma

### AI'a sordugum prompt

> Bu kodda hangi tasarim sorunlarini goruyorsun? Hangi tasarim oruntuleri bu sorunlari cozebilir? Her sorun icin kisa bir aciklama yaz.

### AI yanitinin ozeti

AI, kodda tek sinifin fazla sorumluluk aldigini, `if-elif` zincirinin yeni kanal eklemeyi zorlastirdigini, nesne olusturma kararinin ayri bir yapida olmamasini, dis servislerin ortak arayuze baglanmadigini ve gonderim sonrasi olaylarin genisletilebilir olmadigini soyledi. Cozum olarak Factory Method, Adapter, Facade, Observer ve Strategy oruntulerinin uygun olabilecegini belirtti.

### Benim listem ile farklar

Ben ozellikle test edilebilirlik ve toplu/oncelikli gonderim kurallarinin sabit davranisa baglanmasi uzerinde durdum. AI ise oruntu isimlerini daha erken onerdi. Bu fark yararli oldu; cunku ben once kodun somut sorunlarini yazdim, sonra hangi oruntunun hangi sorunu kapatabilecegini daha net eslestirdim.

