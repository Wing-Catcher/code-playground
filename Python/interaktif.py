print("=== === === === ===")
print("Program Rapor")
print("=== === === === ===")

nilai = input("Masukkan nilai siswa: ") # hasilnya akan string
# mengubah nilai menjadi int
nilai = float(nilai)

#logika
if (nilai < 80):
    print("Predikat siswa C " + str(nilai) + " <-")
elif (nilai < 90):
    print("Predikat siswa B " + str(nilai) + " <-")
elif (nilai >= 90):
    print("Predikat siswa A " + str(nilai) + " <-")
else:
    print("Invalid")