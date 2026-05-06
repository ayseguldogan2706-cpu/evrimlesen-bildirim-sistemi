# Faz 2 AI Log

## AI'a sordugum prompt

> Bu bildirim sisteminde SMS ve push gonderimi gercekte farkli dis servislerle yapilacak. Dis servislerin metot adlari sistemin bekledigi `gonder(istek)` arayuzune uymuyor. Adapter pattern burada uygun mu, yoksa Facade mi? Farkini acikla.

## AI yanitinin ozeti

AI, Adapter ve Facade'in farkli sorunlari cozdügünü soyledi. Adapter'in uyumsuz dis servis arayuzlerini ortak bildirim arayuzune cevirmek icin uygun oldugunu, Facade'in ise sistemin ic karmasikligini kullaniciya daha sade gostermek icin uygun oldugunu belirtti.

## Ben ne uyguladim?

Ben iki oruntuyu da ayri amaclarla uyguladim. `SmsServisAdapteri` ve `PushServisAdapteri`, dis servislerin farkli metotlarini `gonder(istek)` yapisina cevirdi. Sonra `BildirimMerkezi` sinifini ekleyerek e-posta, SMS, push ve toplu gonderim icin kolay bir kullanim noktasi olusturdum.

## AI'in eksik veya yanlis kalan tarafi

AI ilk basta Facade'in tek basina yeterli olabilecegini dusundurdu. Ancak sadece Facade kullanilsaydi dis servislerin uyumsuz metot adlari ve farkli cevap bicimleri yine sistemin icinde kalacakti. Bu nedenle Facade, Adapter'in yerine gecmedi; sadece Adapter ile duzenlenen alt sistemi daha kolay kullanilir hale getirdi.

## Alternatifleri neden reddettim?

Bridge bu faz icin gereksiz soyutlama olurdu, cunku bildirim kanali ile uygulama platformu gibi iki bagimsiz boyut yoktu. Decorator da dis servis uyumsuzlugunu cozmezdi; sadece var olan davranisin etrafina ek isler koymaya yarardi. Bu yuzden Adapter ve Facade daha dogru secim oldu.

