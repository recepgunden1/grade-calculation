def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not_1 = int(liste[1])
    not_2 = int(liste[2])
    not_3 = int(liste[3])
    son_not = not_1 * (3/10) + not_2 * (3/10) + not_3 * (4/10)

    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"
    
    return isim + "----------------> " + harf + "\n"

with open("dosya.txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
    with open("notlar.txt", "w", encoding="utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)

with open("notlar.txt", "r", encoding="utf-8") as file3:
    gecenler = []
    kalanlar = []
    for satir in file3:
        not_bilgisi = satir.split(" ")[-1].strip()
        if not_bilgisi == "FF":
            kalanlar.append(satir)
        else:
            gecenler.append(satir)

with open("gecenler.txt", "w", encoding="utf-8") as file4:
    for gecen in gecenler:
        file4.write(gecen)

with open("kalanlar.txt", "w", encoding="utf-8") as file5:
    for kalan in kalanlar:
        file5.write(kalan)
