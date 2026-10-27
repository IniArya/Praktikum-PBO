from abc import ABC, abstractmethod

class Pengguna(ABC):
    def __init__(self, id_pengguna, nama):
        self.__id_pengguna = id_pengguna
        self.__nama = nama

    @property
    def id_pengguna(self):
        return self.__id_pengguna

    @property
    def nama(self):
        return self.__nama

    @abstractmethod
    def get_peran(self):
        pass

    @abstractmethod
    def hak_akses(self):
        pass

    def jalankan(self):
        print(f"{self.get_peran()} {self.nama} aktif")
        print("Hak akses:", ", ".join(self.hak_akses()))

    def __str__(self):
        return f"[{self.get_peran()}] {self.id_pengguna} - {self.nama}"

class Admin(Pengguna):
    def __init__(self, id_pengguna, nama, level_akses):
        super().__init__(id_pengguna, nama)
        self.__level_akses = level_akses
        self.__daftar_komputer = []

    @property
    def level_akses(self):
        return self.__level_akses

    @property
    def daftar_komputer(self):
        return list(self.__daftar_komputer)

    def tambah_komputer(self, komputer):
        self.__daftar_komputer.append(komputer)

    def get_peran(self):
        return "Admin"

    def hak_akses(self):
        return ["kelola komputer", "kelola paket", "lihat laporan"]

class Operator(Pengguna):
    def __init__(self, id_pengguna, nama, shift):
        super().__init__(id_pengguna, nama)
        self.__shift = shift
        self.__jumlah_dilayani = 0

    @property
    def shift(self):
        return self.__shift

    @property
    def jumlah_dilayani(self):
        return self.__jumlah_dilayani

    def catat_transaksi(self):
        self.__jumlah_dilayani += 1

    def get_peran(self):
        return "Operator"

    def hak_akses(self):
        return ["layani pelanggan", "proses transaksi"]

class Pelanggan(Pengguna):
    def __init__(self, id_pengguna, nama, saldo=0):
        super().__init__(id_pengguna, nama)
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def top_up(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def kurangi_saldo(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        return False

    def get_peran(self):
        return "Pelanggan"

    def hak_akses(self):
        return ["pakai komputer", "top up saldo"]

class Komputer:
    def __init__(self, nomor):
        self.__nomor = nomor
        self.__dipakai = False

    @property
    def nomor(self):
        return self.__nomor

    @property
    def dipakai(self):
        return self.__dipakai

    def gunakan(self):
        self.__dipakai = True

    def lepas(self):
        self.__dipakai = False

class Paket(ABC):
    def __init__(self, nama, tarif_per_jam):
        self.__nama = nama
        self.__tarif_per_jam = tarif_per_jam

    @property
    def nama(self):
        return self.__nama

    @property
    def tarif_per_jam(self):
        return self.__tarif_per_jam

    @abstractmethod
    def hitung_biaya(self, durasi_jam):
        pass

    @abstractmethod
    def keunggulan(self):
        pass

    def info(self):
        print(f"Paket {self.nama}, tarif dasar Rp{self.tarif_per_jam}/jam, {self.keunggulan()}")

class PaketReguler(Paket):
    def __init__(self):
        super().__init__("Reguler", 5000)

    def hitung_biaya(self, durasi_jam):
        return self.tarif_per_jam * durasi_jam

    def keunggulan(self):
        return "komputer standar"

class PaketVIP(Paket):
    def __init__(self, biaya_ruangan):
        super().__init__("VIP", 10000)
        self.__biaya_ruangan = biaya_ruangan

    def hitung_biaya(self, durasi_jam):
        return self.tarif_per_jam * durasi_jam + self.__biaya_ruangan

    def keunggulan(self):
        return f"ruangan ber-AC, biaya ruangan Rp{self.__biaya_ruangan}"

class PaketMember(Paket):
    def __init__(self, diskon_persen):
        super().__init__("Member", 5000)
        self.__diskon_persen = diskon_persen

    def hitung_biaya(self, durasi_jam):
        total = self.tarif_per_jam * durasi_jam
        return total - total * self.__diskon_persen // 100

    def keunggulan(self):
        return f"diskon {self.__diskon_persen} persen"

class PaketMalam(Paket):
    def __init__(self):
        super().__init__("Malam", 4000)

    def hitung_biaya(self, durasi_jam):
        lebih = max(0, durasi_jam - 6)
        return 15000 + lebih * self.tarif_per_jam

    def keunggulan(self):
        return "harga 15000 untuk 6 jam"

class Struk:
    def __init__(self, transaksi):
        self.__transaksi = transaksi

    def cetak(self):
        t = self.__transaksi
        print(f"Struk {t.id_transaksi}: {t.pelanggan.nama}, paket {t.paket.nama}, "
              f"{t.durasi} jam, total Rp{t.total}")


class Transaksi:
    def __init__(self, id_transaksi, pelanggan, operator, komputer, paket, durasi):
        self.__id_transaksi = id_transaksi
        self.__pelanggan = pelanggan
        self.__operator = operator
        self.__komputer = komputer
        self.__paket = paket
        self.__durasi = durasi
        self.__total = paket.hitung_biaya(durasi)
        self.__struk = Struk(self)

    @property
    def id_transaksi(self):
        return self.__id_transaksi

    @property
    def pelanggan(self):
        return self.__pelanggan

    @property
    def paket(self):
        return self.__paket

    @property
    def durasi(self):
        return self.__durasi

    @property
    def total(self):
        return self.__total

    def proses(self):
        if self.__komputer.dipakai:
            print("Komputer sedang dipakai")
            return False
        if not self.__pelanggan.kurangi_saldo(self.__total):
            print(f"Saldo {self.__pelanggan.nama} tidak cukup")
            return False
        self.__komputer.gunakan()
        self.__operator.catat_transaksi()
        return True

    def cetak(self):
        self.__struk.cetak()

    def __add__(self, other):
        return self.total + other.total

    def __radd__(self, other):
        return other + self.total

    def __lt__(self, other):
        return self.total < other.total

    def __str__(self):
        return f"Transaksi {self.id_transaksi} total Rp{self.total}"

class LaporanHarian:
    def __init__(self, daftar_transaksi):
        self.__daftar = daftar_transaksi

    def cetak(self):
        pendapatan = sum(self.__daftar)
        print(f"Laporan harian: {len(self.__daftar)} transaksi, pendapatan Rp{pendapatan}")

def cetak_dokumen(dokumen):
    dokumen.cetak()

def main():
    print("1. Bukti abstract class tidak bisa diinstansiasi")
    for kelas, args in ((Pengguna, ("U00", "Tes")), (Paket, ("Tes", 1000))):
        try:
            kelas(*args)
        except TypeError as e:
            print(f"TypeError pada {kelas.__name__}: {e}")

    print("\n2. Polimorfisme pewarisan: pengguna")
    admin = Admin("A01", "Budi", 3)
    operator = Operator("O01", "Sari", "Pagi")
    pelanggan = Pelanggan("P01", "Ryaa", 50000)
    for pengguna in [admin, operator, pelanggan]:
        print(pengguna)
        pengguna.jalankan()

    print("\n3. Polimorfisme pewarisan: paket (durasi 7 jam)")
    daftar_paket = [PaketReguler(), PaketVIP(5000), PaketMember(20), PaketMalam()]
    for paket in daftar_paket:
        paket.info()
        print(f"Biaya 7 jam: Rp{paket.hitung_biaya(7)}")

    print("\n4. Agregasi Admin dan Komputer")
    pc1, pc2 = Komputer(1), Komputer(2)
    admin.tambah_komputer(pc1)
    admin.tambah_komputer(pc2)
    print("Jumlah komputer dikelola admin:", len(admin.daftar_komputer))

    print("\n5. Transaksi")
    t1 = Transaksi("T01", pelanggan, operator, pc1, PaketMember(20), 3)
    t2 = Transaksi("T02", pelanggan, operator, pc2, PaketVIP(5000), 2)
    for t in [t1, t2]:
        print(t)
        if t.proses():
            print("Transaksi berhasil, sisa saldo Rp" + str(pelanggan.saldo))
    print("Total dua transaksi:", t1 + t2)
    print("t1 lebih kecil dari t2:", t1 < t2)

    print("\n6. Duck typing")
    laporan = LaporanHarian([t1, t2])
    for dokumen in [t1, laporan]:
        cetak_dokumen(dokumen)

if __name__ == "__main__":
    main()