def hitung_gaji_karyawan(nama, jam_kerja, golongan):
    if golongan == 'a':
        upah_per_jam = 5000
    elif golongan == 'b':
        upah_per_jam = 7000
    elif golongan == 'c':
        upah_per_jam = 8000
    elif golongan == 'd':
        upah_per_jam = 10000
    else: 
        return "golongan tidak valid"
    
    if jam_kerja > 48:
        uang_lembur = (jam_kerja-48)*4000
    else:
        uang_lembur = 0
    gaji_total = (jam_kerja*upah_per_jam) + uang_lembur
    return f"nama:  {nama}\nGaji mingguan: {gaji_total}"

nama = input("masukkan nama: ")
golongan = input("masukkan golongan(a/b/c/d): ")
jam_kerja = int(input("masukkan jam kerja: "))

gaji = hitung_gaji_karyawan(nama, jam_kerja, golongan)
print(gaji)
