print ("Selamat datang!")
print ("Menu")
print ("1. Daftar Kontak")
print ("2. Tambah Kontak")
print ("3. Keluar")

contact = ["Nama: Ismy","No Telepon: 0898765432","Nama: Davis","No Telepon: 08673252421","Nama: Selena","No Telepon: 0823544746","Nama: There","No Telepon: 08635236423"]
menu = int(input("Pilih menu: ")) 
if menu==1:
    print ("Daftar kontak ")
    for n in contact:
        print (n)

if menu==2:
    print ("Tambah kontak ")
    a = input("Nama: ") 
    b = int(input("No Telepon: "))
    c = "Nama: {}".format(a)
    d = "No Telepon: {}".format(b)
    contact.append(c)
    contact.append(d)
    for n in contact:
        print(n) 
        print("Kontak berhasil ditambahkan")

elif menu==3:
    print ("Program selesai, sampai jumpa!")

elif menu!=1 and menu!=2 and menu!=3:
    print ("Menu tidak tersedia")