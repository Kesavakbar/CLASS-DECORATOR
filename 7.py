from collections import namedtuple

Buah = namedtuple("Buah", ("nama", "warna", "rasa"))

apel = Buah("Apel", "Merah", "Manis dan segar")
pisang = Buah("Pisang", "Kuning", "Manis dan lembut")
jeruk = Buah("Jeruk", "Oranye", "Asam dan segar")

print("Informasi Buah:")
print(apel.nama, "-", apel.warna, "-", apel.rasa)
print(pisang.nama, "-", pisang.warna, "-", pisang.rasa)
print(jeruk.nama, "-", jeruk.warna, "-", jeruk.rasa)
