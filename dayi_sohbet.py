#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Türk Dayı Sohbet Üreticisi
Bu kod gerçekten çalışır. Dayılar gibi konuşur.
Kullanım: python dayi_sohbet.py
"""

import random
import time
import sys

# Dayı sohbet cümleleri - abartılı ciddiyetle
DAYI_SOHBETLERI = [
    "Gençler, eskiden biz ekmek alırdık 50 kuruşa, şimdi bir simit 10 lira. Ama siz anlamazsınız, çünkü çalışmıyorsunuz.",
    "Bu gençlik hiçbir şey bilmiyor. Bizim zamanımızda telefon yoktu, sokakta oynardık. Şimdi herkes ekrana bakıyor.",
    "Abi, çayın demini kaçırdın mı? Bu kadar basit bir şeyi bile yapamıyorsunuz artık.",
    "Enflasyon falan diyorlar ama asıl mesele çalışmamak. Ben 70'lerde işe başladım, şimdi emekliyim.",
    "Komşunun oğlu doktor oldu, sen ne iş yapıyorsun? Boş durma, bir şey öğren.",
    "Bu ülke çok değişti. Eskiden herkes birbirine saygılıydı, şimdi herkes ben ben.",
    "Kahve içmiyorum, çay içerim. Kahve mideyi bozar, çay ise ruhu besler. Bunu unutma.",
    "Gençler, evlenin artık. Bekar geziyorsunuz, yaşlanınca pişman olursunuz.",
    "Bu havalar da değişti. Eskiden kış kıştı, yaz yazdı. Şimdi ne olduysa oldu.",
    "Abi, bu işi ben sana anlatayım: Sabah kalk, çay demle, işe git, akşam gel. Basit."
]

# Gizli siyasi mesaj - sadece eğer çok dikkat edersen
GIZLI_MESAJ = "Valla bu sistem çok karışık, kimse doğruyu söylemiyor ama çayımız içilsin."  # Saklı, görmeyebilirsin

def dayi_sohbet_uret(sayi=5):
    """Rastgele dayı sohbetleri üretir."""
    print("=== TÜRK DAYISI SOHBET MODU AKTİF ===")
    print("(Bu programın amacı tamamen bilimsel ve ciddi bir çalışmadır.)\n")
    
    for i in range(sayi):
        sohbet = random.choice(DAYI_SOHBETLERI)
        print(f"Dayı #{i+1}: {sohbet}")
        time.sleep(1.5)  # Dayı gibi yavaş konuşur
        print()
    
    # %10 ihtimalle gizli mesajı göster (saklı)
    if random.random() < 0.1:
        print(f"[Gizli Dayı Fısıltısı]: {GIZLI_MESAJ}")
    
    print("=== SOHBET BİTTİ. ŞİMDİ ÇAY İÇ. ===")

if __name__ == "__main__":
    try:
        adet = int(sys.argv[1]) if len(sys.argv) > 1 else 5
        dayi_sohbet_uret(adet)
    except:
        dayi_sohbet_uret(5)

# İmza Damgası
# Tarih: 20 Ekim 2026
# İmza: Kayyum Grok (Ciddi ama değil)
# Onay: Bu kod çalışır, dayılar gibi.
