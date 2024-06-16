from collections import namedtuple

Orang = namedtuple("Orang", "nama anak")

@classmethod
def tampilkan_info(cls, self):
    print("Nama:", self.nama)
    print("Nama anak:")
    for i, anak in enumerate(self.anak, 1):
        print(f"{i}. {anak}")

Orang.tampilkan_info = tampilkan_info

john = Orang("John Doe", ["Timmy", "Jimmy"])
print(john)
print(id(john.anak))
john.anak.append("Tina")
print(john)
print(id(john.anak))
Orang.tampilkan_info(john)