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
3. Mengubah html agar dapat muncul header dan gambar produk

- [ X ] Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.

- [ X ] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
  - `name`
  - `price`
  - `type`
  - 'sound
  1. Mengubah berkas models.py dengan mengisinya classnya dengan nama, harga, deskripsi produk, tupe, dan profil produk

- [ X ] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Menambahkan context dengan isi nama, harga, dan deskripsi produk dalam views.py
2. Melakukan add product dengan mengakses django admin interface dengan membuat product dengan isi name, description, price, type, dan sound_profile

- [ X ] Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
1. Membuat berkas urls.py dalam direktori main dan mengisi kodenya dengan rute url untuk mengarahkan ke tampilan main di dalam variabel urlpatterns

- [ X ] Melakukan deployment ke PWS terhadap aplikasi yang sudah di-deploy sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Membuat project baru lagi di PWS dengan nama switchtify lalu mendeploy ke project tersebut.
2. Mendeploy kembali project saya


- [ X ] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
  - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara **step-by-step** (bukan hanya sekadar mengikuti tutorial).
    Sudah saya tulis di atas di tiap checkpoint

  - Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas *html*.
  
Client Request
         |
         V

urls.py (Mencocokkan URL yang diminta dengan pola yang sesuai)
         |
         V

views.py (Menangani logika aplikasi, memanggil models jika diperlukan)
         |
         V

models.py (Mengambil atau memproses data dari/ke database)
         |
         V

views.py (Mengirimkan data ke template HTML)
         |
         V

HTML Template (Merender data ke dalam bentuk tampilan yang diinginkan)
         |
         V

Response to Client (Mengirimkan tampilan HTML yang dirender ke klien)

  - Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
    Fungsi Git adalah untuk keep track antar perubahan pada program dan memungkinkan kita untuk menyimpan tiap versi kode

  - Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Menurut saya mengapa Django dipilih sebagai framework pertama dalam pembelajaran pengembangan perangkat lunak karena learning curve yang tidak terlalu tinggi dan kemudahan pagi penggunanya dan dokumentasi yang diberikan juga lengkap. Dengan alasan tersebut Django mempermudah pemula untuk belajar konsep penting sehingga kita dapat lebih efisien dalam membangun aplikasi web.

  - Mengapa model pada Django disebut sebagai ORM?
  Model pada Django disebut ORM (Object-Relational Mapping) karena berfungsi menghubungkan objek Python dengan tabel database. Dengan ORM, kita bisa mengelola data database menggunakan metode Python tanpa perlu menulis SQL secara manual.

 - [ x ] Create a form input to add a model object to  the previous app.
  - Membuat base html terlebih dahulu dan menyesuaikan dengan struktur project Django saya
  - Mengedit TEMPLATES pada settings.py 
  - Menyesuaikan main.html agar memakai base.html sebagai template
  - Membuat forms.py dan mengisinya dengan fields Product saya
  - Membuat fungsi create_products pada views.py 
  - Membuat create_product.html dan mengextend ke base.html
  - Melengkapi main.html untuk mendisplay Add New Product dan tombol untuk pergi ke page tersebut
  - Run server dan mengecek pekerjaan

 - [ x ] Add 4 views to view the added objects in XML, JSON, XML by ID, and JSON by ID formats.
  - Menambahkan fungsi  show_XML dan show_JSON dengan paramater request dan show_XML_by_id dan show_JSON_by_id dengan parameter request dan id dan menambahkan returnnya sesuai dengan tipe datanya dalam views.py

 - [ x ] Create URL routing for each of the views added in point 2.
  - Menambahkan path untuk tiap fungsi diatas pada urls.py

 - [ x ]Answer the following questions in README.md in the root folder.
 - Explain why we need data delivery in implementing a platform.
   Data delivery is needed in a platform to so that there can be  communication and data exchange ensuring that  
   information flows smoothly and can be processed or acted upon in real-time.
   
 - In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
   JSON is more popular than XML due to its simpler structure and better performance in web communication.
  
 - Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.
   It checks whether the form data meets the validation rules defined for the form because it is necessary to ensure that only valid data is processed and 
   stored
   
 - Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?
    The csrf_token in Django forms helps stop cross-site request forgery (CSRF) attacks by making sure that form submissions are from trusted users. Without 
   it, an attacker could trick users into sending harmful requests, which could lead to sensitive data being exposed
   
 - Explain how you implemented the checklist above step-by-step (not just following the tutorial).
   already stated in each checkpoints

 - [ x ]Access the four URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md
  - Merequest pada Postman dengan URL XML
    ![image](https://github.com/user-attachments/assets/80efb17c-1e55-4e8f-ae06-a23e941126be)
   
  - Merequest pada Postman dengan URL JSON
    ![image](https://github.com/user-attachments/assets/779f77a9-f65c-4e9e-8c5d-6fe064d11bf4)


- [ x ] Perform add-commit-push to GitHub.

- [ X ] **Implement** the register, login, and logout functions so that the user can access the application freely.
        - Mengimport UserCreationForm dan messages dalam views.py
        - Menambahkan fungsi register
        - Membuat register.html 
        - Mengimport register kedalam views
        - Menambahkan path register ke url patters
        - Import autenthicate, login dan AuthenticationForm
        - Add fungsi login_user
        - Buat login.html
        - Mengimport login_user kedalam views dan menambahkan pathnya
        - Mengimport logout
        - Membuat fungsi logout_user
        - Menglogin login_requred
        - Membuat agar main page hanay dapat diakese dari client yang sudah logged in
        - Import HttpResponseRedirect, reverse, and datetime di paling atas views.py
        - Mengganti if form.isvlaid()
        - Menambahkan     'last_login': request COOKIES['last_login'] di dalam product_detail
        - Mengedit kembali logout_user
        - Menambahkan suatu potongan kode dalan main.html
        - Membuat koneksi dari model ke user model dengan import user dan menambahkan potongan kode yang mengconnect modelnya ke user 
        - Memodifikasi create_product agar prevent Django secara langsung menyimpna objek-objek dari form ke database
        - mengubah value dari products dari views.py
        - Melakukan migrasi
        - Menginput 1 1 1 ke pesan error dan migrasi
        - menambahkan import os dan mengganti variabel debug
      

- [ X ] **Create two user accounts** with three dummy data entries each. Each account should be able to access the data locally.
 - Menbuat akun dengan nama khairul.bintang
 - Membuat produk dalam akun tersebut
 - logout dan membuat akun baru dalam nama biggestofman
 - mengecek apakah produk dari akun lain ada atau tidak
- [ X ] **Connect the models** `Product` and `User`.
 - Dengan import user dan menambahkan potongan kode dalam models.py 
 - Memodifikasi views.py di main
- [ X ] **Display logged-in user details** such as `username`, and apply cookies like `last_login` to the application's main page.
 - Mengubah value dari products dengan mengfilter semua produk dan hanya mengambil product dimana filed user diisi dengan objek user yang sesuai dari user logged-innnya 
- [ X ] **Answer the following questions** below:
  1. What is the difference between HttpResponseRedirect() and redirect()?
  HttpResponseRedirect() is a low-level way to redirect to a URL, while redirect() is a shortcut that handles URL paths or view names directly.

  2. Explain how the MoodEntry model is linked with User.
  The MoodEntry model links with User using a ForeignKey, allowing each mood entry to be associated with a specific user.

  3. What is the difference between authentication and authorization?
     - What happens when a user logs in?
     When a user logs in, Django checks their credentials and creates a session.
     - How does Django implement these two concepts?
     Django handles authentication with the auth system and permissions for authorization.

  4. How does Django remember logged-in users?
  Django remembers logged-in users by storing a session ID in a cookie.
     - Explain other uses of cookies and whether all cookies are safe to use.
     Sessions are also used to track other user-related data across requests.

  5. Explain the implementation process of the checklist step-by-step (apart from following the tutorial). Sudah ada di tiap checkpoint diatas

- [ X ]  Perform add -commit-push to Github
