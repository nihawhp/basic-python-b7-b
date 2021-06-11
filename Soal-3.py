teori = float(input("Masukkan nilai ujian teori : "))
praktek = float(input("Masukkan nilai ujian praktek : "))

if teori >= 7.0 and praktek >= 7.0:
    print("SELAMAT ANDA LULUS!") #benar

if praktek <= 7.0:
    print("Anda harus mengulang ujian praktek.") #benar

if teori <= 7.0:
    print("Anda harus mengulang ujian teori") #benar

if teori < 7.0 and praktek < 7.0:
    print("Anda harus mengulang ujian teori dan praktek.")