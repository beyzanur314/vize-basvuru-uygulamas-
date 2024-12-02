# İtalya Schengen Vize Randevu Bildirimi

Bu Python projesi, Schengen Vize başvuruları için İtalya Konsolosluğu'ndan İstanbul'daki randevu bilgilerini çekmek ve bu bilgiler değiştiğinde telefonunuza bildirim göndermek için Pushbullet API'sini kullanır.

## Proje Açıklaması

Bu proje, Schengen Vize başvuruları için İtalya'nın İstanbul konsolosluğundaki "Turistlik Vize" ve "Standart Hizmet" randevu durumlarını kontrol eder. Eğer bir randevu tarihi mevcutsa, bir telefon bildirim gönderilir. Bildirimler, Pushbullet API'si aracılığıyla telefonunuza iletilir.

## Özellikler

- İtalya konsolosluğunda İstanbul'daki "Turistlik Vize" ve "Standart Hizmet" için randevu tarihi kontrolü yapar.
- Eğer randevu tarihi varsa, Pushbullet üzerinden bildirim gönderilir.
- Pushbullet API ile telefon bildirimleri gönderebilirsiniz.

## Gereksinimler

- Python 3.x
- `requests` kütüphanesi
- `pushbullet.py` kütüphanesi

## Kurulum

1. **Python ve gerekli kütüphaneleri yükleyin**:

   Python 3.x yüklü olmalıdır. Aşağıdaki komutları kullanarak gerekli kütüphaneleri yükleyebilirsiniz:

   ```bash
   pip install requests pushbullet.py
