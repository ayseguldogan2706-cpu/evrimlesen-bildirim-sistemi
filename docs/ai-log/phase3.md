# Faz 3 AI Log

## Pair programming ozeti

Yaklasik 30 dakikalik AI pair programming oturumunda asil olarak iki konu uzerinde calistim: gonderim sonrasi olaylarin nasil ayrilacagi ve gonderim davranisinin nasil degistirilebilir yapilacagi. Once Observer icin olay yayinci ve dinleyici yapisini tartistim. Sonra Strategy icin `BildirimMerkezi` uzerinden degistirilebilir bir gonderim politikasi kurmanin daha anlasilir olacagina karar verdim.

## AI'a sordugum temel promptlar

> Bildirim sistemi artik Factory, Adapter ve Facade kullaniyor. Faz 3'te en az iki Behavioral oruntu uygulamam gerekiyor. Gonderimden sonra loglama/gecmis tutma icin Observer uygun mu? Gonderim politikasini degistirmek icin Strategy mi Command mi daha dogru olur?

> Acik/Kapali Prensibi'ni bu projede nasil gosterebilirim? Yeni davranis eklemek icin mevcut kodu degistirmedigimi testle nasil kanitlarim?

## AI yanitinin ozeti

AI, gonderim tamamlandiktan sonra farkli nesnelerin tepki vermesi gerektigi icin Observer'in uygun oldugunu soyledi. Gonderim politikasinda ise Strategy ve Command arasinda Strategy'nin daha sade kalacagini belirtti. Command daha cok isleri kuyruklamak, geri almak veya zamanlamak icin anlamli olurdu; bu projede asil ihtiyac gonderim kuralini degistirmekti.

## Ben ne uyguladim?

Observer icin `OlayYayinci`, `BildirimOlayi` ve `GonderimGecmisi` siniflarini ekledim. `BildirimSistemi` artik sonucu dogrudan gecmise yazmak yerine olay yayinliyor. Gecmis dinleyicisi bu olayi alarak kayit tutuyor.

Strategy icin `GonderimStratejisi`, `SiraliGonderimStratejisi` ve `OncelikliGonderimStratejisi` siniflarini ekledim. `BildirimMerkezi`, tekil ve toplu gonderimleri secili strateji uzerinden yapiyor. Testlerde yeni bir strateji sinifi tanimlayarak mevcut proje kodunu degistirmeden yeni davranis eklenebildigini gosterdim.

## AI nerede yaniltti veya eksik kaldi?

AI ilk basta Command oruntusunu da eklemeyi onerdi. Bunu uygulamadim, cunku odev zaten yeterli sayida oruntu iceriyordu ve Command eklemek projeyi gereksiz buyutecekti. Ayrica Command, bu sistemde Strategy kadar dogrudan bir problemi cozmuyordu. Bu nedenle iki Behavioral oruntuyle kalmak daha net ve savunulabilir oldu.

Command icin kuyruklama, geri alma, zamanlanmis calistirma veya her bildirimi ayri bir komut nesnesi olarak saklama gibi bir ihtiyac tanimlamamistim. Bu ihtiyaclar yokken Command eklemek sadece "bir oruntu daha kullanildi" gibi duracakti. Strategy ise gercek soruna daha dogrudan cevap verdi: ayni bildirim altyapisi korunurken gonderim politikasinin degisebilmesi.

AI ayrica davranislari cok hizli ayri siniflara bolmeyi onerdi. Bunu sinirli tuttum; cunku amac her yardimci islemi soyutlamak degil, Faz 3'te genisletilebilir davranisi gostermekti. Bu nedenle Observer sadece gonderim sonrasi olaylara, Strategy ise gonderim politikasina odaklandi.

## AI olmadan bu faz ne kadar surerdi?

AI olmadan bu fazin yaklasik 4-5 saat surecegini dusunuyorum. AI, Observer ve Strategy arasindaki sorumluluk ayrimini tartismada yardimci oldu. Yine de hangi oruntuyu uygulayip hangisini reddedecegime ben karar verdim; cunku fazla oruntu eklemek odevin okunurlugunu azaltabilirdi.

Kod ve dokumantasyon degisikliklerini commit ederken de fazin parcalarini mantiksal olarak ayirdim: once davranissal oruntuler, sonra test/CI, sonra dokumantasyon. Bu ayrim, hangi degisikligin hangi odev gereksinimini karsiladigini daha kolay gostermek icindi.
