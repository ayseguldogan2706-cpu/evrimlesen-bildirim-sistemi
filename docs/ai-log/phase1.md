# Faz 1 AI Log

## AI'a sordugum prompt

> Faz 0'daki bildirim sistemi kodunda e-posta, SMS ve push gonderimi tek sinifta if-elif zinciriyle yapiliyor. Bu fazda en az bir Creational tasarim oruntusu uygulamam gerekiyor. Factory Method bu durum icin uygun mu? Kod review yapar gibi hangi riski cozdugunu ve nelere dikkat etmem gerektigini acikla.

## AI yanitinin ozeti

AI, Factory Method'un bu faz icin uygun oldugunu soyledi. Cunku sorun kanal nesnelerinin ve kanal davranislarinin ana sinif icinde secilmesiydi. Ayrica her kanal icin ortak bir arayuz kullanmam, gonderim sonucunu ortak bir modelle dondurmem ve bilinmeyen kanal hatasini acik sekilde ele almam gerektigini belirtti.

## Ben ne uyguladim?

Ben `BildirimFabrikasi` sinifini ekledim ve kanal olusturma sorumlulugunu bu sinifa tasidim. `EpostaKanali`, `SmsKanali` ve `PushKanali` siniflari ortak `BildirimKanali` arayuzunden turedi. `BildirimSistemi` artik uzun `if-elif` zinciri kullanmak yerine fabrikadan kanal nesnesi alip onun `gonder` metodunu cagiriyor.

## AI onerisiyle ayni veya farkli olan kararlarim

AI, fabrika icinde kayit sozlugu kullanmayi onerdi; bunu uyguladim cunku Python'da sade ve okunur oldu. Ancak AI'in ilk dusuncesinde tum dogrulamalari ayri dogrulama siniflarina bolmek de vardi. Bunu bu fazda uygulamadim, cunku Faz 1'in asil konusu nesne olusturma sorumluluguydu. Cok fazla degisikligi ayni faza koymak hangi oruntunun hangi sorunu cozdurdugunu belirsizlestirebilirdi.

