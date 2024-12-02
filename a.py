import requests
import json

# API URL'si
url = "https://api.schengenvisaappointments.com/api/visa-list/?format=json"
response = requests.get(url)

# API'ye başarılı şekilde istek yapılmışsa
if response.status_code == 200:
    data = response.json()  # JSON verisini çözümle
    for entry in data:
        country = entry.get("mission_country", "Bilinmiyor")  # Ülke bilgisi
        city = entry.get("city", "Bilinmiyor")  # Şehir bilgisi
        appointment_date = entry.get("appointment_date")  # Randevu tarihi
        visa_type = entry.get("visa_type", "Bilinmiyor")  # Vize türü
        service_type = entry.get("service_type", "Bilinmiyor")  # Hizmet türü
        
        # İtalya ve İstanbul, turistlik vize ve standart hizmet türünü kontrol et
        if country == "İtalya" and city == "İstanbul":
            if visa_type == "Turistlik Vize" and service_type == "Standart Hizmet":
                if appointment_date:
                    print(f"İtalya İstanbul - Turistlik Vize ve Standart Hizmet için randevu tarihi: {appointment_date}")
                else:
                    print("İtalya İstanbul - Turistlik Vize ve Standart Hizmet için mevcut randevu yok.")
            else:
                print(f"{country} İstanbul - Vize türü veya hizmet türü uygun değil.")
        else:
            print(f"{country} için İstanbul'da uygun vize veya hizmet türü bulunmamaktadır.")
else:
    print(f"Hata: {response.status_code}")
