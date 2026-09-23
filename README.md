SISTEM MANAJEMEN OPERASIONAL DAN PELAYANAN WARNET

1. ENCAPSULATION : Seluruh atribut penting (nama, username, password,
saldo, status, harga_per_jam, durasi_jam) bersifat private dan
hanya bisa diakses/diubah melalui @property (getter) dan
@<nama>.setter (setter) yang disertai validasi data. Validasi yang
gagal akan mem-raise ValueError, dan ditangani dengan try-except
di bagian program utama.
2. INHERITANCE   : Class "Pengguna" adalah induk dari "Admin",
"Operator", dan "Pelanggan".
3. ABSTRACTION   : Class "Pengguna" dan "Paket" dibuat sebagai
abstract class (ABC) dengan abstract method.
4. POLYMORPHISM  : Class "Paket" memiliki beberapa turunan
(PaketReguler, PaketVIP, PaketGaming) yang mengimplementasikan
method hitung_biaya() dengan cara/harga berbeda-beda.

1. Class Pengguna
* Memenuhi atribut kelas: nama_instansi, total_pengguna, versi_sistem.
* Memiliki atribut instance: nama, username, password.
* Memiliki atribut private: __nama, __username, __password.
* Memiliki instance method: cek_password() dan tampilkan_info().
* Memiliki class method: info_total_pengguna().
* Memiliki static method: validasi_username().
* Menggunakan getter dan setter dengan property.
* Memiliki validasi pada setter.
* Validasi diuji dengan data valid dan tidak valid.

2. Class Admin
* Memiliki atribut instance: level_akses.
* Mewarisi class Pengguna.
* Memiliki instance method: ubah_diskon_paket().
* Memiliki method tampilkan_info().
* Menggunakan method Paket.ubah_diskon().
* Dibuat 2 objek Admin.

3. Class Operator
* Memiliki atribut instance: shift.
* Mewarisi class Pengguna.
* Memiliki instance method: aktifkan_komputer().
* Memiliki method tampilkan_info().
* Dibuat 2 objek Operator.

4. Class Pelanggan
* Memiliki atribut instance: saldo.
* Memiliki atribut private: __saldo.
* Menggunakan getter dan setter saldo.
* Setter memiliki validasi agar saldo tidak negatif.
* Memiliki instance method: top_up() dan bayar().
* Memiliki method tampilkan_info().
* Dibuat 2 objek Pelanggan.
* Setter diuji dengan data valid dan tidak valid.

5. Class Komputer
* Memiliki atribut kelas: nama_instansi, total_komputer, spesifikasi_minimum, STATUS_VALID.
* Memiliki atribut instance: nomor_komputer dan spesifikasi.
* Memiliki atribut private: __status.
* Memiliki instance method: tampilkan_status().
* Memiliki class method: dari_dictionary().
* Memiliki static method: validasi_spesifikasi().
* Menggunakan getter dan setter status.
* Setter memiliki validasi.
* Setter diuji dengan status valid dan tidak valid.
* Dibuat 2 objek Komputer.

6. Class Paket
* Memiliki atribut kelas: nama_instansi, diskon_member, total_objek_paket.
* Memiliki atribut instance: nama_paket dan harga_per_jam.
* Memiliki atribut private: __harga_per_jam.
* Memiliki class method: ubah_diskon() dan info_total_paket().
* Memiliki static method: validasi_durasi().
* Memiliki abstract method: hitung_biaya().
* Menggunakan getter dan setter harga.
* Setter memiliki validasi.
* Setter diuji dengan harga valid dan tidak valid.

7. Class PaketReguler
* Mewarisi class Paket.
* Memiliki instance method hitung_biaya().
* Menggunakan harga per jam dan diskon member.
* Dibuat 2 objek PaketReguler.

8. Class PaketVIP
* Mewarisi class Paket.
* Memiliki instance method hitung_biaya().
* Memiliki diskon khusus VIP.
* Menggunakan diskon member.
* Dibuat 2 objek PaketVIP.

9. Class PaketGaming
* Mewarisi class Paket.
* Memiliki instance method hitung_biaya().
* Memiliki biaya awal penggunaan.
* Menggunakan diskon member.
* Dibuat 2 objek PaketGaming.

10. Class Transaksi
* Memiliki atribut kelas: nama_instansi, total_transaksi, mata_uang.
* Memiliki atribut instance: pelanggan, komputer, paket, durasi_jam, id_transaksi, waktu.
* Memiliki atribut private: __durasi_jam.
* Memiliki instance method: proses_transaksi().
* Memiliki class method: info_total_transaksi().
* Memiliki static method: validasi_durasi().
* Menggunakan getter dan setter durasi.
* Setter memiliki validasi.
* Berinteraksi dengan class Pelanggan, Komputer, dan Paket.
* Dibuat 3 objek Transaksi untuk pengujian.

11. Main Program
* Membuat minimal 2 objek untuk setiap class yang relevan.
* Menjalankan instance method.
* Menjalankan class method.
* Menjalankan static method.
* Menguji setter dengan data valid.
* Menguji setter dengan data tidak valid.
* Menguji validasi menggunakan ValueError.
* Menguji transaksi berhasil.
* Menguji transaksi dengan komputer tidak tersedia.
* Menguji transaksi dengan saldo tidak mencukupi.
