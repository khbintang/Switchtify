- [ X ] Membuat sebuah proyek Django baru.
 1. Membuat repositori baru di github dengan nama Switchtify
 2. Membuat direktori lokal dan menambahkan file README.md dan mengisinya dengan checklist-checklist
 3. Mengcommit perubahan dan menghubungkan direktori lokal dengan repository di github dengan membuat branch baru, mengkoneksikan repositori github dengan menggunakan url repositorinya
 4. Mengpush ke github
 5. Mengclone repository ke laptop saya dan mengpushnya
 6. Mengaktivasi virtual enviroment
 7. Membuat requirements.txt, menginstall dependenciesnya dan membuat project Django dengan nama Switchtify
 8. Menambahkan "localhost" dan "127.0.0.1" ke ALLOWED_HOST di settings.py dan merun server Django nya
 9. Mengupload proyek tersebut ke github
 10. Membuat proyek baru di PWS dengan nama Switchtify dan menambahkan url deploymentnnya kedalam settings.py

- [ X ] Membuat aplikasi dengan nama `main` pada proyek tersebut.
1. Menjalankan perintah python manage.py startapp main dann membuat aplikasi main pada proyek Switchtify dan mendaftarkan aplikasi main kedalam proyek Switchtify dengan menambahkan main kedalam INSTALLED_APPS dalam settings.py
2. Menambahkan main.html dalam folder templates yang berada pada main

- [ X ] Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.

- [ X ] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
  - `name`
  - `price`
  - `type`
  - 'sound_profile'
  - 'lube'
  1. Mengubah berkas models.py dengan mengisinya classnya dengan nama, harga, dan deskripsi produk

- [ X ] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Menambahkan context dengan isi nama, harga, dan deskripsi produk dalam views.py

- [ X ] Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
1. Membuat berkas urls.py dalam direktori main dan mengisi kodenya dengan rute url untuk mengarahkan ke tampilan main di dalam variabel urlpatterns

- [ X ] Melakukan deployment ke PWS terhadap aplikasi yang sudah di-deploy sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Membuat project baru lagi di PWS dengan nama switchtify lalu mendeploy ke project tersebut.

- [ X ] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
  - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara **step-by-step** (bukan hanya sekadar mengikuti tutorial).
    Sudah saya tulis di atas di tiap checkpoint

  - Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas *html*.
  1. Client Request
   |
   V
  2. urls.py (Mencocokkan URL yang diminta dengan pola yang sesuai)
   |
   V
  3. views.py (Menangani logika aplikasi, memanggil models jika diperlukan)
   |
   V
  4. models.py (Mengambil atau memproses data dari/ke database)
   |
   V
  5. views.py (Mengirimkan data ke template HTML)
   |
   V
  6. HTML Template (Merender data ke dalam bentuk tampilan yang diinginkan)
   |
   V
  7. Response to Client (Mengirimkan tampilan HTML yang dirender ke klien)


  - Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
    Fungsi Git adalah untuk keep track antar perubahan pada program dan memungkinkan kita untuk menyimpan tiap versi kode

  - Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Menurut saya mengapa Django dipilih sebagai framework pertama dalam pembelajaran pengembangan perangkat lunak karena learning curve yang tidak terlalu tinggi dan kemudahan pagi penggunanya dan dokumentasi yang diberikan juga lengkap. Dengan alasan tersebut Django mempermudah pemula untuk belajar konsep penting sehingga kita dapat lebih efisien dalam membangun aplikasi web.

  - Mengapa model pada Django disebut sebagai ORM?
  Model pada Django disebut ORM (Object-Relational Mapping) karena berfungsi menghubungkan objek Python dengan tabel database. Dengan ORM, kita bisa mengelola data database menggunakan metode Python tanpa perlu menulis SQL secara manual.
