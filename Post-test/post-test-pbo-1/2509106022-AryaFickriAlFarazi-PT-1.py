from abc import ABC, abstractmethod
from datetime import datetime

# CLASS 1: PENGGUNA (Abstract Class - induk Admin, Operator, Pelanggan)
class Pengguna(ABC):
    nama_instansi = "Warnet Mas Amba"
    total_pengguna = 0
    versi_sistem = "1.69.67"

    def __init__(self, nama, username, password):
        self.__nama = None
        self.__username = None
        self.__password = None

        self.nama = nama
        self.username = username
        self.password = password

        Pengguna.total_pengguna += 1
        self._id_pengguna = Pengguna.total_pengguna

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama_baru):
        if not isinstance(nama_baru, str) or not nama_baru.strip():
            raise ValueError("Nama tidak boleh kosong.")
        self.__nama = nama_baru.strip()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username_baru):
        if not Pengguna.validasi_username(username_baru):
            raise ValueError("Username tidak valid (harus alfanumerik, minimal 4 karakter).")
        self.__username = username_baru

    @property
    def password(self):
        # Password asli tidak ditampilkan langsung
        return "*" * len(self.__password)

    @password.setter
    def password(self, password_baru):
        if not password_baru or len(password_baru) < 6:
            raise ValueError("Password minimal 6 karakter.")
        self.__password = password_baru

    def cek_password(self, input_password):
        return self.__password == input_password

    @abstractmethod
    def tampilkan_info(self):
        pass

    @classmethod
    def info_total_pengguna(cls):
        return f"Pengguna: {cls.total_pengguna}"

    @staticmethod
    def validasi_username(username):
        return isinstance(username, str) and username.isalnum() and len(username) >= 4


# CLASS 2: ADMIN (turunan Pengguna)
class Admin(Pengguna):
    def __init__(self, nama, username, password, level_akses="Super Admin"):
        super().__init__(nama, username, password)
        self.level_akses = level_akses

    def tampilkan_info(self):
        return (f"[ADMIN] ID:{self._id_pengguna} | Nama:{self.nama} | "
                f"Username:{self.username} | Level Akses:{self.level_akses}")

    def ubah_diskon_paket(self, kelas_paket, diskon_baru):

        kelas_paket.ubah_diskon(diskon_baru)
        print(f"Diskon member: {diskon_baru}%")


# CLASS 3: OPERATOR (turunan Pengguna)
class Operator(Pengguna):
    def __init__(self, nama, username, password, shift="Pagi"):
        super().__init__(nama, username, password)
        self.shift = shift

    def tampilkan_info(self):
        return (f"[OPERATOR] ID:{self._id_pengguna} | Nama:{self.nama} | "
                f"Username:{self.username} | Shift:{self.shift}")

    def aktifkan_komputer(self, komputer):
        komputer.status = "Aktif"
        print(f"{komputer.nomor_komputer} aktif")


# CLASS 4: PELANGGAN (turunan Pengguna)
class Pelanggan(Pengguna):
    def __init__(self, nama, username, password, saldo_awal=0):
        super().__init__(nama, username, password)
        self.__saldo = None
        self.saldo = saldo_awal

    def tampilkan_info(self):
        return (f"[PELANGGAN] ID:{self._id_pengguna} | Nama:{self.nama} | "
                f"Username:{self.username} | Saldo:Rp{self.__saldo:,.0f}")

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai):
        if not isinstance(nilai, (int, float)) or nilai < 0:
            raise ValueError("Saldo tidak boleh negatif atau bukan berupa angka.")
        self.__saldo = nilai

    def top_up(self, jumlah):
        if not isinstance(jumlah, (int, float)) or jumlah <= 0:
            raise ValueError("Jumlah top up harus lebih dari 0.")
        self.saldo = self.__saldo + jumlah

    def bayar(self, jumlah):

        if jumlah <= self.__saldo:
            self.saldo = self.__saldo - jumlah
            return True
        return False


# CLASS 5: KOMPUTER (class mandiri, tidak diturunkan dari class lain)
class Komputer:
    nama_instansi = "Warnet Mas Amba"
    total_komputer = 0
    spesifikasi_minimum = "Intel i3, RAM 8GB, SSD 256GB"

    STATUS_VALID = ["Aktif", "Nonaktif", "Maintenance", "Terpakai"]

    def __init__(self, nomor_komputer, spesifikasi):
        self.nomor_komputer = nomor_komputer
        self.spesifikasi = spesifikasi
        self.__status = "Nonaktif"

        Komputer.total_komputer += 1

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        if status_baru not in Komputer.STATUS_VALID:
            raise ValueError(f"Status '{status_baru}' tidak valid. "
                              f"Pilihan: {Komputer.STATUS_VALID}")
        self.__status = status_baru

    def tampilkan_status(self):
        return f"{self.nomor_komputer} | Spek: {self.spesifikasi} | Status: {self.__status}"

    @classmethod
    def dari_dictionary(cls, data):

        return cls(data["nomor_komputer"], data["spesifikasi"])

    @staticmethod
    def validasi_spesifikasi(spesifikasi):
        return isinstance(spesifikasi, str) and "RAM" in spesifikasi

# CLASS 6: PAKET (Abstract Class - induk dari jenis paket berbeda)
class Paket(ABC):
    nama_instansi = "Warnet Maju Jaya"
    diskon_member = 0
    total_objek_paket = 0

    def __init__(self, nama_paket, harga_per_jam):
        self.nama_paket = nama_paket
        self.__harga_per_jam = None
        self.harga_per_jam = harga_per_jam
        Paket.total_objek_paket += 1

    @property
    def harga_per_jam(self):
        return self.__harga_per_jam

    @harga_per_jam.setter
    def harga_per_jam(self, harga_baru):
        if not isinstance(harga_baru, (int, float)) or harga_baru <= 0:
            raise ValueError(f"Harga paket '{self.nama_paket}' harus berupa angka positif.")
        self.__harga_per_jam = harga_baru

    @abstractmethod
    def hitung_biaya(self, durasi_jam):
        pass

    @classmethod
    def ubah_diskon(cls, diskon_baru):

        if not isinstance(diskon_baru, (int, float)) or not (0 <= diskon_baru <= 100):
            raise ValueError("Diskon member harus berupa angka antara 0-100.")
        cls.diskon_member = diskon_baru

    @classmethod
    def info_total_paket(cls):
        return f"Paket: {cls.total_objek_paket}"

    @staticmethod
    def validasi_durasi(durasi_jam):
        return isinstance(durasi_jam, (int, float)) and durasi_jam > 0


class PaketReguler(Paket):
    def __init__(self):
        super().__init__("Reguler", 4000)

    def hitung_biaya(self, durasi_jam):
        subtotal = self.harga_per_jam * durasi_jam
        return subtotal - (subtotal * Paket.diskon_member / 100)


class PaketVIP(Paket):
    def __init__(self):
        super().__init__("VIP", 7000)

    def hitung_biaya(self, durasi_jam):
        subtotal = self.harga_per_jam * durasi_jam
        subtotal -= subtotal * 0.05
        return subtotal - (subtotal * Paket.diskon_member / 100)


class PaketGaming(Paket):
    def __init__(self):
        super().__init__("Gaming", 10000)

    def hitung_biaya(self, durasi_jam):
        subtotal = 5000 + (self.harga_per_jam * durasi_jam)
        return subtotal - (subtotal * Paket.diskon_member / 100)

# CLASS 7: TRANSAKSI
class Transaksi:
    nama_instansi = "Warnet Maju Jaya"
    total_transaksi = 0
    mata_uang = "IDR"

    def __init__(self, pelanggan, komputer, paket, durasi_jam):
        self.pelanggan = pelanggan
        self.komputer = komputer
        self.paket = paket
        self.__durasi_jam = None
        self.durasi_jam = durasi_jam

        Transaksi.total_transaksi += 1
        self.id_transaksi = Transaksi.total_transaksi
        self.waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def durasi_jam(self):
        return self.__durasi_jam

    @durasi_jam.setter
    def durasi_jam(self, jam):
        if not Transaksi.validasi_durasi(jam):
            raise ValueError("Durasi transaksi harus berupa angka positif.")
        self.__durasi_jam = jam

    def proses_transaksi(self):

        if self.komputer.status != "Aktif":
            raise ValueError(
                f"Komputer {self.komputer.nomor_komputer} sedang tidak tersedia "
                f"(status saat ini: '{self.komputer.status}')."
            )

        total_biaya = self.paket.hitung_biaya(self.durasi_jam)
        berhasil = self.pelanggan.bayar(total_biaya)

        if berhasil:
            self.komputer.status = "Terpakai"
            print(f"Transaksi #{self.id_transaksi}: berhasil, total Rp{total_biaya:,.0f}")
        else:
            print(f"Transaksi #{self.id_transaksi}: saldo tidak cukup (Rp{total_biaya:,.0f})")

        return berhasil

    @classmethod
    def info_total_transaksi(cls):
        return f"Transaksi: {cls.total_transaksi}"

    @staticmethod
    def validasi_durasi(durasi_jam):
        return isinstance(durasi_jam, (int, float)) and durasi_jam > 0

# DEMONSTRASI PROGRAM
if __name__ == "__main__":
    print("\n SISTEM WARNET MAS AMBA")

    # ---------- 1. Membuat objek (minimal 2 per class) ----------
    print("\nPengguna")
    admin1 = Admin("Budi Santoso", "budiadmin", "rahasia123")
    admin2 = Admin("Siti Aminah", "sitiadmin", "sandi123", level_akses="Admin Cabang")

    operator1 = Operator("Andi Wijaya", "andiop", "operator1", shift="Pagi")
    operator2 = Operator("Rina Kusuma", "rinaop", "operator2", shift="Malam")

    pelanggan1 = Pelanggan("Dewi Lestari", "dewi01", "pass123", saldo_awal=50000)
    pelanggan2 = Pelanggan("Rian Pratama", "rian02", "pass456", saldo_awal=20000)

    for p in [admin1, admin2, operator1, operator2, pelanggan1, pelanggan2]:
        print(p.tampilkan_info())               # instance method: tampilkan_info (polymorphic)

    print("\nKomputer")
    komp1 = Komputer("PC-01", "Intel i5, RAM 16GB, SSD 512GB")
    komp2 = Komputer.dari_dictionary({"nomor_komputer": "PC-02",
                                       "spesifikasi": "Intel i7, RAM 32GB, SSD 1TB"})
    for k in [komp1, komp2]:
        print(k.tampilkan_status())              # instance method: tampilkan_status

    print("\nPaket")
    paket_reguler1, paket_reguler2 = PaketReguler(), PaketReguler()
    paket_vip1, paket_vip2 = PaketVIP(), PaketVIP()
    paket_gaming1, paket_gaming2 = PaketGaming(), PaketGaming()

    for pkt in [paket_reguler1, paket_reguler2, paket_vip1, paket_vip2,
                paket_gaming1, paket_gaming2]:
        # method sama (hitung_biaya) tapi hasil beda tiap class -> polymorphism
        print(f"{pkt.nama_paket}: Rp{pkt.hitung_biaya(3):,.0f}/3 jam")

    # ---------- 2. Class method & static method ----------
    print("\nClass method")
    print(Pengguna.info_total_pengguna())
    print(Paket.info_total_paket())
    print(Transaksi.info_total_transaksi())

    print("\nStatic method")
    print("Username:", Pengguna.validasi_username("dewi01"))
    print("Spesifikasi:", Komputer.validasi_spesifikasi(komp1.spesifikasi))
    print("Durasi:", Paket.validasi_durasi(3))

    # ---------- 3. Instance method antar-objek ----------
    print("\nAktivasi komputer")
    operator1.aktifkan_komputer(komp1)
    operator2.aktifkan_komputer(komp2)

    print("\nDiskon member")
    admin1.ubah_diskon_paket(Paket, 10)          # instance method Admin + classmethod Paket
    print(f"VIP 3 jam: Rp{paket_vip1.hitung_biaya(3):,.0f}")

    print("\nTop up & password")
    pelanggan1.top_up(20000)                     # instance method: top_up
    print(f"Saldo: Rp{pelanggan1.saldo:,}")
    print(f"Password salah: {admin1.cek_password("salahtebak")}")
    print(f"Password benar: {admin1.cek_password("rahasia123")}")

    # ---------- 4. Uji setiap setter: 1 data VALID & 1 data TIDAK VALID ----------
    print("\nUji setter")
    try:
        Pelanggan("", "cobaan", "pass123")                 # nama kosong
    except ValueError as e:
        print(f"Nama: {e}")

    try:
        Pelanggan("Coba", "ab", "pass123")                 # username < 4 karakter
    except ValueError as e:
        print(f"Username: {e}")

    try:
        admin1.password = "sandiBaru123"                   # valid
        print("Password diperbarui")
    except ValueError as e:
        print(f"Password: {e}")
    try:
        admin1.password = "123"                            # tidak valid
    except ValueError as e:
        print(f"Password: {e}")

    try:
        pelanggan2.saldo = 30000                           # valid
        print(f"Saldo: Rp{pelanggan2.saldo:,}")
    except ValueError as e:
        print(f"Saldo: {e}")
    try:
        pelanggan2.saldo = -5000                           # tidak valid
    except ValueError as e:
        print(f"Saldo: {e}")

    try:
        komp2.status = "Maintenance"                       # valid
        print(f"Status {komp2.nomor_komputer}: {komp2.status}")
    except ValueError as e:
        print(f"Status: {e}")
    try:
        komp2.status = "Rusak Berat"                       # tidak valid
    except ValueError as e:
        print(f"Status: {e}")
    komp2.status = "Aktif"                                 # kembalikan agar bisa dipakai transaksi

    try:
        paket_reguler1.harga_per_jam = 4500                # valid
        print(f"Harga: Rp{paket_reguler1.harga_per_jam:,}/jam")
    except ValueError as e:
        print(f"Harga: {e}")
    try:
        paket_reguler1.harga_per_jam = -1000                # tidak valid
    except ValueError as e:
        print(f"Harga: {e}")

    try:
        Paket.ubah_diskon(15)                               # valid
        print(f"Diskon: {Paket.diskon_member}%")
    except ValueError as e:
        print(f"Diskon: {e}")
    try:
        Paket.ubah_diskon(150)                              # tidak valid
    except ValueError as e:
        print(f"Diskon: {e}")

    # ---------- 5. Transaksi: 3 skenario wajib (masing-masing sekali) ----------
    print("\nTransaksi")
    komp1.status = "Aktif"

    # (a) Transaksi berhasil
    transaksi1 = Transaksi(pelanggan1, komp1, paket_reguler1, durasi_jam=2)
    try:
        transaksi1.proses_transaksi()
    except ValueError as e:
        print(f"Transaksi #{transaksi1.id_transaksi}: {e}")

    # (b) Gagal karena komputer tidak tersedia (komp1 sudah 'Terpakai')
    transaksi2 = Transaksi(pelanggan2, komp1, paket_vip1, durasi_jam=1)
    try:
        transaksi2.proses_transaksi()
    except ValueError as e:
        print(f"Transaksi #{transaksi2.id_transaksi}: {e}")

    # (c) Gagal karena saldo tidak cukup (komp2 Aktif, saldo pelanggan2 kurang)
    transaksi3 = Transaksi(pelanggan2, komp2, paket_gaming1, durasi_jam=5)
    try:
        transaksi3.proses_transaksi()
    except ValueError as e:
        print(f"Transaksi #{transaksi3.id_transaksi}: {e}")
    print(f"Status {komp2.nomor_komputer}: {komp2.status}")

    # Uji setter durasi_jam: 1 valid (sudah terbukti lewat transaksi1-3) + 1 tidak valid
    try:
        transaksi1.durasi_jam = -3
    except ValueError as e:
        print(f"Durasi: {e}")

    # kesimpulan akhir
    print("\n=== RINGKASAN ===")
    print(Pengguna.info_total_pengguna())
    print(f"Total komputer: {Komputer.total_komputer}")
    print(Paket.info_total_paket())
    print(Transaksi.info_total_transaksi())
    for k in [komp1, komp2]:
        print(k.tampilkan_status())
    for p in [pelanggan1, pelanggan2]:
        print(p.tampilkan_info())