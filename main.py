import fileMethod

nama=fileMethod.ticket_method("Nama")
nama.intro(39)

print(" ______________________________________ ")
print("|   SELAMAT DATANG DI KONSER JUSTIN BIBIR   |")
print("|___________________________________________|")
print("|         Kursi           |    Harga        |")
print("|1. VVIP					 | Rp 1.000.000    |")
print("|2. Festival 	         | Rp 850.000      |")
print("|3. Tribune			     | Rp 500.000      |")
print("|___________________________________________|")


def book():
    pax = int(input("Jumlah Penonton = "))
    print("Masukan nama Penonton : ")
    for i in range(int(pax)):
        i += 1
        n = input("Penonton ke- {} ".format(i))
    tot = pax * harga
    print("Total Harga Rp ", tot)
    print("__________")
    email = input("Masukkan Alamat Email Anda: ")
    print("----------")
    print("Terima Kasih Telah Membeli Tiket Konser Justin Bibir")
    print("E-Ticket Anda Akan Dikirimkan Melalui Email ", email)
    print("----------")


kursi = int(input("Masukan Pilihan Kursi : "))
if (kursi == 1):
    harga = 1000000
    book()
elif (kursi == 2):
    harga = 850000
    book()
elif (kursi == 3):
    harga = 500000
    book()
else:
    print("Tidak Ada Pilihan Kursi .")
