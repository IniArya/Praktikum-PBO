# Sistem Manajemen Operasional dan Pelayanan Warnet

Nama: [ISI NAMA LENGKAP]
NIM: [ISI NIM]
Kelas: [ISI KELAS]

## Deskripsi Program

Program ini mensimulasikan operasional dan pelayanan warnet. Program mengelola pengguna (Admin, Operator, Pelanggan), komputer, paket penggunaan, dan transaksi. Posttest ini melanjutkan konsep inheritance dan encapsulation dari posttest sebelumnya, lalu menambahkan Abstraksi dan Polimorfisme.

## Class Diagram

![Class Diagram](class_diagram.png)

### Penjelasan Relasi

Asosiasi: Transaksi ke Pelanggan, Operator, Komputer, dan Paket. Transaksi hanya menyimpan referensi ke objek-objek tersebut, sedangkan objek itu sudah ada sebelumnya dan tetap hidup walaupun transaksinya tidak ada.

Agregasi: Admin ke Komputer. Admin mengelola daftar Komputer lewat method tambah_komputer(), tetapi objek Komputer dibuat di luar Admin dan tetap ada walaupun Admin dihapus. Karena itu relasinya agregasi, bukan komposisi.

Komposisi: Transaksi ke Struk. Objek Struk dibuat di dalam constructor Transaksi dan hanya dipakai oleh Transaksi tersebut, sehingga Struk tidak punya arti tanpa Transaksi dan ikut hilang bersamanya. Karena itu relasinya komposisi, bukan agregasi.

## Penerapan Abstraksi

Abstract class Pengguna (memakai ABC) memiliki dua abstract method, yaitu get_peran() dan hak_akses(), serta satu method konkret jalankan() yang dipakai bersama. Subclass yang mengimplementasikan semua abstract method: Admin, Operator, dan Pelanggan.
Abstract class Paket (memakai ABC) memiliki dua abstract method, yaitu hitung_biaya() dan keunggulan(), serta satu method konkret info() yang dipakai bersama. Subclass yang mengimplementasikan semua abstract method: PaketReguler, PaketVIP, PaketMember, dan PaketMalam.
Konsep inheritance tetap dipakai: setiap subclass memanggil super().**init**(...), memiliki atribut unik (level_akses pada Admin, shift pada Operator, saldo pada Pelanggan, biaya_ruangan pada PaketVIP, diskon_persen pada PaketMember), dan seluruh atribut dibuat private dengan akses lewat property.
Bukti abstract class tidak dapat diinstansiasi ada pada fungsi main() menggunakan try-except TypeError, dengan hasil output pada screenshot di bagian Screenshot Output.

## Penerapan Polimorfisme

Polimorfisme via pewarisan: method hitung_biaya() di-override oleh PaketReguler, PaketVIP, PaketMember, dan PaketMalam dengan perhitungan berbeda, lalu dipanggil dalam satu loop pada daftar_paket. Method get_peran() dan hak_akses() juga di-override oleh Admin, Operator, dan Pelanggan, dan dipanggil lewat satu loop.
Duck typing: class Struk dan LaporanHarian tidak berhubungan lewat pewarisan, tetapi sama-sama memiliki method cetak(). Keduanya dipanggil lewat satu fungsi yang sama, yaitu cetak_dokumen().
Operator overloading: **str** pada Pengguna dan Transaksi, serta **add**, **radd**, dan **lt** pada Transaksi.
Larangan anti-pattern: program tidak memakai rantai if/elif yang mengecek type() atau string jenis. Setiap objek menentukan perilakunya sendiri lewat method.

## Nilai Plus: Penerapan SOLID

Open Closed Principle (OCP): jenis paket baru cukup dibuat sebagai subclass baru dari Paket tanpa mengubah kode Transaksi atau kode lama lainnya.
Dependency Inversion Principle (DIP): class Transaksi bergantung pada abstraksi Paket (memanggil hitung_biaya()), bukan pada class paket tertentu, sehingga paket apa pun bisa dipakai.

## Screenshot Output

Bukti abstract class tidak bisa diinstansiasi:

![Screenshot 1 - Abstract class tidak bisa diinstansiasi](https://i.imgur.com/kRKJcnq.png)

Polimorfisme pewarisan pada Pengguna dan Paket:

![Screenshot 2 - Polimorfisme pengguna dan paket](https://i.imgur.com/DwBxnek.png)

Agregasi, transaksi, dan operator overloading:

![Screenshot 3 - Transaksi dan operator overloading](https://i.imgur.com/kRKJcnq.png)

Duck typing:

![Screenshot 4 - Duck typing](https://i.imgur.com/lspIZjP.png)
