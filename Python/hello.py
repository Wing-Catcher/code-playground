# String (Teks)
nama = "John Doe"
angka_string = "1234"

# Int / Integer (Angka)
umur = 45

# Float (Desimal)
tinggi = 190.21
berat_badan = 200

# Menampilkan informasi dasar
print("Namaku adalah: " + nama + " <- Ini String")
print("Umurku : " + str(umur) + " <- Ini Int")
# str(variable_int) = mengubah data tipe int ke string
print("Tinggiku: " + str(tinggi) + " <- ini Float")
# str(variable_float) = mengubah data tipe float ke string

# Soal 1: Menampilkan hobi
hobi = "Bermain Rubik"
print("Hobiku adalah " + hobi)

# Soal 2: Konversi angka ke string dan gabungkan dengan teks
angka = 99.99
print("Angka favoritku adalah " + str(angka))

# Soal 3: Mengganti nama dan menampilkan pesan
nama = "Raffy"
print("Halo, namaku adalah " + nama)

# Challenge: Menampilkan semua data
# Input data pribadi
nama = "Raffy Ahmad Jaliyyan"
umur = 16
tinggi = 175.5
hobi = "Programmer dan Cubing"

# Menampilkan data dalam satu kalimat
print(
    "Halo, namaku adalah " + nama + 
    ", aku berumur " + str(umur) + " tahun, " + 
    "tinggi badanku " + str(tinggi) + " cm, dan hobiku adalah " + hobi + "."
)

# =========================
# Belajar Python: Input dan Logika If
# =========================

# **1. Input Data dengan `input()`**
# Meminta input dari pengguna
nama = input("Siapa nama anda: ")
umur = input("Berapa umur anda: ")

# Menampilkan hasil input
print("Namamu adalah: " + nama)
print("Umurmu adalah: " + umur + " tahun")

# Catatan: input() mengembalikan string. Jika perlu angka, konversi dengan int() atau float().

# =========================
# **2. Logika If-Else**
# =========================

# Meminta nilai dari pengguna
nilai = input("Masukkan nilaimu: ")
nilai = int(nilai)  # Mengubah input string menjadi integer

# Logika If-Else untuk menentukan kondisi nilai
if nilai > 70:
    print("Nilaimu di atas 70, tepatnya: " + str(nilai))
elif nilai < 70:
    print("Nilaimu di bawah 70, tepatnya: " + str(nilai))
else:
    print("Input tidak valid")

# =========================
# Latihan Interaktif
# =========================

# **Soal 1: Program dengan Nama, Usia, dan Kota**
# Meminta data pengguna
nama = input("Masukkan nama kamu: ")
usia = input("Masukkan usia kamu: ")
kota = input("Masukkan kota tempat tinggal kamu: ")

# Menampilkan hasil dalam satu kalimat
print(
    "Halo, namaku " + nama +
    ". Aku berusia " + usia + " tahun " +
    "dan tinggal di " + kota + "."
)

# **Soal 2: Modifikasi Program Logika Nilai**
# Meminta nilai dari pengguna
nilai = input("Masukkan nilaimu (0-100): ")
nilai = int(nilai)  # Mengubah input string menjadi integer

# Logika nilai yang dimodifikasi
if nilai > 85:
    print("Nilaimu sangat bagus! Tepatnya: " + str(nilai))
elif 70 <= nilai <= 85:
    print("Nilaimu cukup baik! Tepatnya: " + str(nilai))
elif nilai < 70:
    print("Nilaimu perlu ditingkatkan! Tepatnya: " + str(nilai))
else:
    print("Input tidak valid")

# =========================
# Catatan:
# Kamu dapat mencoba program ini satu per satu, lalu sesuaikan inputnya
# untuk melihat bagaimana program bekerja sesuai logika yang dibuat.