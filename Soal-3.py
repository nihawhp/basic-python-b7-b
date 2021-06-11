teori = float(input("Masukkan nilai ujian teori : "))
praktek = float(input("Masukkan nilai ujian praktek : "))

if teori >= 7.0 and praktek >= 7.0:
    print("SELAMAT ANDA LULUS!") 

elif praktek <= 7.0 and teori >= 7.0:
    print("Anda harus mengulang ujian praktek.") 

elif teori <= 7.0 and praktek >= 7.0:
    print("Anda harus mengulang ujian teori") 

else:
    print("Anda harus mengulang ujian teori dan praktek.")
