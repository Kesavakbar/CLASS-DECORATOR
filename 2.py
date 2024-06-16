class BumbuDapur:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    @classmethod
    def tambah_bumbu(cls, nama, harga):
        return cls(nama, harga, stok=0)

    @staticmethod
    def cek_stok(stok):
        if stok > 0:
            return "Stok tersedia"
        else:
            return "Stok habis"

    @property
    def info(self):
        return f"{self.nama} - Harga: {self.harga} - Stok: {self.stok}"

bumbu1 = BumbuDapur("Garam", 5000, 10)
bumbu2 = BumbuDapur("Lada", 8000, 14)
bumbu3 = BumbuDapur.tambah_bumbu("Micin", 9500)

print(BumbuDapur.cek_stok(bumbu1.stok)) 

print(bumbu1.info) 
print(bumbu2.info)  
print(bumbu3.info)
