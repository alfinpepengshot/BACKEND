password_benar = "12345"
max_attempts = 2
attempts = 0

while attempts < max_attempts:
    password_input = input("Masukkan password: ")
    
    if password_input == password_benar:
        print("Selamat datang bos!")
        break
    else:
        print("Password salah, coba lagi!")
        attempts += 1

if attempts == max_attempts:
    print("Terima kasih sudah menggunakan aplikasi kami")
