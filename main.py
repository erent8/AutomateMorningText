from credentials import mobile_number # 'credentials' adlı dosyadan 'mobile_number' değişkenini import et

import requests # 'requests' modülünü import et
import schedule # 'schedule' modülünü import et
import time # 'time' modülünü import et

def send_message(): # 'send_message' adında bir fonksiyon tanımla
    resp = requests.post('https://textbelt.com/text', { # 'requests' modülü ile bir POST isteği yap ve response'u 'resp' adlı değişkene ata
        'phone' : mobile_number, # 'mobile_number' değişkenini 'phone' parametresi olarak gönder
        'message': 'Hey, Good morning', # Gönderilecek mesajı belirle
        'key': 'textbelt' # API anahtarını belirle
    })
    print(resp.json()) # Response'un JSON formatındaki verisini konsola yazdır

# schedule.every() .day.at('06:00').do(send_message) # Her gün saat 06:00'da 'send_message' fonksiyonunu çalıştırmak için bir schedule (zamanlama) tanımlaması yapılabilir.
schedule.every(10).seconds.do(send_message) # 10 saniyede bir 'send_message' fonksiyonunu çalıştırmak için bir schedule (zamanlama) tanımlaması yap

while True: # Sonsuz döngü
    schedule.run_pending() # schedule'daki bekleyen görevleri çalıştır
    time.sleep(1) # 1 saniye bekle (bu sayede sonsuz döngü çok fazla CPU kaynağı kullanmayacak) 
