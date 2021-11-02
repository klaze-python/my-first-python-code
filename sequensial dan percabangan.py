"""
sequensial
"""

print('ibu berkata,"pergi ke toko"')
print('budi menjawab"baik bu, apa yang harus saya beli?"')
print('ibu menjawab,"beli 1 botol susu dan jika ada telur beli 6."')
print("maka budi pergi ke toko")
print("budi mulai berbelanja")


"""
percabangan
"""

jumlah_botol_susu = 12
jumlah_telur = 10
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 10:
    print("budi mengecek harganya dan cukup")
    if jumlah_telur < 6:
        print("budi membeli 1 botol susu")
    else:
        print("budi membeli 6 botol susu")
else:
    print("budi tidak jadi membeli 1 botol susu")

print("budi pulang ke rumah")
print("menyerahkan hasilnya kepada ibu")