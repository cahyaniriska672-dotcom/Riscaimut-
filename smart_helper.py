# SMART HELPER - SOLUSI DIGITAL

while True:
    print("\n===== SMART HELPER =====")
    print("1. Kalkulator diskon")
    print("2. Pengingat minum air")
    print("3. Penghitung waktu belajar")
    print("4. Tips hidup sehat")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        harga = float(input("Masukkan harga barang: Rp"))
        diskon = float(input("Masukkan diskon (%): "))

        if harga >= 0 and 0 <= diskon <= 100:
            total = harga - (harga * diskon / 100)
            print("Harga setelah diskon: Rp", total)
        else:
            print("Input harga atau diskon tidak valid!")

    elif pilihan == "2":
        gelas = int(input("Berapa gelas air yang sudah diminum? "))
        print("Jumlah air yang diminum:", gelas, "gelas")
        if gelas < 8:
            print("Jangan lupa minum air lagi!")
        else:
            print("Bagus, target 8 gelas sudah tercapai!")

    elif pilihan == "3":
        jam = float(input("Berapa jam kamu belajar? "))
        if jam >= 0:
            menit = jam * 60
            print("Waktu belajar:", menit, "menit")
        else:
            print("Waktu tidak boleh negatif!")

    elif pilihan == "4":
        print("\nTIPS HIDUP SEHAT")
        print("1. Makan makanan bergizi")
        print("2. Tidur yang cukup")
        print("3. Rajin berolahraga")
        print("4. Minum air yang cukup")
        print("5. Jaga kebersihan diri")

    elif pilihan == "5":
        print("Terima kasih sudah menggunakan Smart Helper!")
        break

    else:
        print("Pilihan tidak valid! Pilih angka 1-5.")
