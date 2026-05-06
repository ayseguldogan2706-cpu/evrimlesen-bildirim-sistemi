from dataclasses import dataclass
from datetime import datetime


@dataclass
class BildirimIstegi:
    kanal: str
    alici: str
    mesaj: str
    oncelik: str = "normal"


@dataclass
class GonderimSonucu:
    kanal: str
    alici: str
    mesaj: str
    oncelik: str
    basarili: bool
    detay: str
    zaman: str

    @classmethod
    def olustur(cls, istek, basarili, detay):
        return cls(
            kanal=istek.kanal,
            alici=istek.alici,
            mesaj=istek.mesaj,
            oncelik=istek.oncelik,
            basarili=basarili,
            detay=detay,
            zaman=datetime.now().isoformat(timespec="seconds"),
        )

