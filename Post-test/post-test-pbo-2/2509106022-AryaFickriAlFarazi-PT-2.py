from abc import ABC, abstractmethod

#Composition
class Spesifikasi:
    def __init__(self, prosesor, ram):
        self.__prosesor = prosesor
        self.__ram = ram

    def __str__(self):
        return f"{self.__prosesor}, RAM {self.__ram} GB"


class Komputer:
    def __init__(self, nomor, prosesor, ram):
        self.__nomor = nomor
        self.__status = "Available"
        self.__spesifikasi = Spesifikasi(prosesor, ram)  #composition

    def get_nomor(self):
        return self.__nomor

    def is_available(self):
        return self.__status == "Available"

    def pakai(self):
        self.__status = "In use"

    def info(self):
        print(f"PC {self.__nomor}, {self.__status}, {self.__spesifikasi}")


#Inheritance: Pengguna
class Pengguna(ABC):
    def __init__(self, id_pengguna, nama, password):
        self._id_pengguna = id_pengguna  #protected
        self._nama = nama                #protected
        self.__password = password       #private

    def get_nama(self):
        return self._nama

    @abstractmethod
    def tampilkan_role(self):
        pass

    def info(self):
        print(f"ID {self._id_pengguna}, nama {self._nama}")


class Admin(Pengguna):
    def __init__(self, id_pengguna, nama, password, access_level):
        super().__init__(id_pengguna, nama, password)
        self.__access_level = access_level
        self.__daftar_komputer = []  #aggregation

    def tambah_komputer(self, komputer):
        self.__daftar_komputer.append(komputer)

    def lihat_komputer(self):
        for k in self.__daftar_komputer:
            k.info()

    def tampilkan_role(self):
        return "Admin"

    def info(self):  #override
        super().info()
        print(f"Role {self.tampilkan_role()}, access level {self.__access_level}")
        print(f"Jumlah PC yang dikelola: {len(self.__daftar_komputer)}")


class Operator(Pengguna):
    def __init__(self, id_pengguna, nama, password, shift):
        super().__init__(id_pengguna, nama, password)
        self.__shift = shift

    def tampilkan_role(self):
        return "Operator"

    def info(self):  #override
        super().info()
        print(f"Role {self.tampilkan_role()}, shift {self.__shift}")


class Pelanggan(Pengguna):
    def __init__(self, id_pengguna, nama, password, saldo):
        super().__init__(id_pengguna, nama, password)
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def kurangi_saldo(self, jumlah):
        if jumlah > self.__saldo:
            return False
        self.__saldo -= jumlah
        return True

    def tampilkan_role(self):
        return "Pelanggan"

    def info(self):  #override
        super().info()
        print(f"Role {self.tampilkan_role()}, saldo Rp{self.__saldo:,}")


#Inheritance: Paket(polymorphism)
class Paket(ABC):
    def __init__(self, nama_paket, harga_per_jam):
        self.__nama_paket = nama_paket
        self.__harga_per_jam = harga_per_jam

    def get_nama(self):
        return self.__nama_paket

    def get_harga_per_jam(self):
        return self.__harga_per_jam

    @abstractmethod
    def hitung_harga(self, durasi):
        pass


class PaketReguler(Paket):
    def __init__(self):
        super().__init__("Paket Reguler", 5000)
        self.__fasilitas = "PC standar"

    def hitung_harga(self, durasi):
        return self.get_harga_per_jam() * durasi


class PaketVIP(Paket):
    def __init__(self):
        super().__init__("Paket VIP", 10000)
        self.__biaya_minuman = 3000  #biaya tetap

    def hitung_harga(self, durasi):  #override dengan logika berbeda
        return self.get_harga_per_jam() * durasi + self.__biaya_minuman


#Association
class Transaksi:
    def __init__(self, id_trx, pelanggan, operator, komputer, paket, durasi):
        self.__id_trx = id_trx
        self.__pelanggan = pelanggan
        self.__operator = operator
        self.__komputer = komputer
        self.__paket = paket
        self.__durasi = durasi
        self.__total = 0

    def proses(self):
        if not self.__komputer.is_available():
            print("Transaksi gagal, PC sedang digunakan.")
            return False
        self.__total = self.__paket.hitung_harga(self.__durasi)
        if not self.__pelanggan.kurangi_saldo(self.__total):
            print("Transaksi gagal, saldo kurang.")
            return False
        self.__komputer.pakai()
        return True

    def cetak_struk(self):
        print(f"Struk transaksi {self.__id_trx}")
        print(f"Pelanggan: {self.__pelanggan.get_nama()}")
        print(f"Operator: {self.__operator.get_nama()}")
        print(f"PC: {self.__komputer.get_nomor()}")
        print(f"Paket: {self.__paket.get_nama()}")
        print(f"Durasi: {self.__durasi} jam")
        print(f"Total: Rp{self.__total:,}")


#Proram Main
if __name__ == "__main__":
    #Komputer dibuat di luar Admin(aggregation)
    pc1 = Komputer(1, "Intel i3", 8)
    pc2 = Komputer(2, "Intel i5", 16)

    admin = Admin("A01", "Budi", "admin123", "Full")
    admin.tambah_komputer(pc1)
    admin.tambah_komputer(pc2)

    operator = Operator("O01", "Sari", "op123", "Siang")
    pelanggan = Pelanggan("P01", "Andi", "andi123", 50000)

    print("Info user")
    for p in [admin, operator, pelanggan]:
        p.info()
        print()

    print("Daftar PC")
    admin.lihat_komputer()

    print()
    print("Harga paket untuk 2 jam")
    for paket in [PaketReguler(), PaketVIP()]:
        print(f"{paket.get_nama()}: Rp{paket.hitung_harga(2):,}")

    print()
    print("Transaksi")
    trx = Transaksi(1, pelanggan, operator, pc1, PaketVIP(), 2)
    if trx.proses():
        trx.cetak_struk()

    print()
    print("Kondisi setelah transaksi")
    pelanggan.info()
    admin.lihat_komputer()