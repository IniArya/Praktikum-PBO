# Sistem Manajemen Operasional dan Pelayanan Warnet
Pada pengerjaan posttest kali ini saya hanya fokus pada penerapan saja tidak menggunakan CRUD
## Daftar Class
Pengguna, Admin, Operator, Pelanggan, Komputer, Spesifikasi, Paket, PaketReguler, PaketVIP, dan Transaksi.
Class Spesifikasi digunakan untuk menunjukkan relasi komposisi.

## Penerapan pada Program

### Relasi UML
1. Asosiasi
   Hubungan antar class yang saling menggunakan tapi tetap hidup sendiri-sendiri. Class Transaksi berhubungan dengan Pelanggan, Operator, Komputer, dan Paket. Objek-objek itu dibuat di luar Transaksi, lalu dikirim lewat konstruktor.

2. Agregasi
   Hubungan "memiliki" yang longgar, bagian tetap bisa hidup walau pemiliknya hilang. Class Admin memiliki daftar Komputer. Komputer dibuat di luar Admin lalu dimasukkan lewat method `tambah_komputer()`.

3. Komposisi
   Hubungan "memiliki" yang kuat, bagian ikut hilang kalau pemiliknya hilang. Class Komputer membuat objek Spesifikasi sendiri di dalam konstruktornya, jadi Spesifikasi tidak berdiri sendiri tanpa Komputer.

### Inheritance
4. Superclass dan subclass
   Class induk menurunkan atribut dan method ke class turunan. Pengguna adalah superclass untuk Admin, Operator, dan Pelanggan. Paket adalah superclass untuk PaketReguler dan PaketVIP.

5. Pemanggilan `super().__init__()`
   Subclass memanggil konstruktor superclass supaya atribut bawaan induk ikut terisi. Contohnya Admin memanggil konstruktor Pengguna untuk mengisi id, nama, dan password.

6. Atribut tambahan pada subclass
   Setiap subclass punya atribut unik yang membedakannya. Admin punya `access_level`, Operator punya `shift`, Pelanggan punya `saldo`, PaketReguler punya `fasilitas`, dan PaketVIP punya `biaya_minuman`.

7. Method overriding
   Subclass mendefinisikan ulang method milik superclass dengan perilaku berbeda. Method `info()` di Pengguna di-override oleh Admin, Operator, dan Pelanggan agar menampilkan data tambahan masing-masing. Method `hitung_harga()` di Paket diimplementasikan berbeda, dan PaketVIP menambahkan biaya minuman.

8. Atribut protected dan private
   Atribut protected (diawali satu underscore) boleh diakses subclass, sedangkan atribut private (diawali dua underscore) hanya bisa diakses class itu sendiri. Di Pengguna, `_id_pengguna` dan `_nama` dibuat protected karena dipakai subclass, sedangkan `__password` dibuat private karena hanya milik superclass.

### Empat Pilar OOP
9. Encapsulation
   Data disembunyikan dengan atribut private dan hanya bisa diakses lewat method. Contohnya saldo Pelanggan diubah lewat `kurangi_saldo()`, dan status Komputer diubah lewat `pakai()`. Datanya tidak diubah langsung dari luar class.

10. Abstraction
    Class abstrak adalah class yang tidak bisa dibuat objeknya langsung dan hanya jadi kerangka untuk turunannya. Pengguna dan Paket dibuat dengan `ABC`, dan method `tampilkan_role()` serta `hitung_harga()` ditandai `@abstractmethod`, sehingga wajib diisi oleh subclass.

11. Polymorphism
    Satu pemanggilan method bisa menghasilkan perilaku berbeda tergantung objeknya. Saat `hitung_harga(2)` dipanggil pada PaketReguler dan PaketVIP, hasilnya berbeda. Begitu juga `info()` yang dipanggil pada Admin, Operator, dan Pelanggan lewat satu perulangan.

12. Inheritance
    Class turunan mewarisi isi class induk sehingga kode tidak perlu ditulis berulang. Penjelasan lengkapnya ada pada poin 4 sampai 8.
