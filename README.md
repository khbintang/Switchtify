### TUGAS 2
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

### TUGAS 3
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

### TUGAS 4
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

### TUGAS 5
- [ X ] Implement functions to delete and edit products.
  - Integrate Tailwind into css first
  - Add the edit_product function in views.py
  - Change the data structure from int to id
  - Perform migrations again after the data changes
  - Create edit_product.html in main/templates 
  - Importing the edit_product function to urls.py and adding the URL path
  - Doing the same thing again for delete_mood feature
  - Adding the delete and edit button for each product in main.html

- [ X ] Customize the design of the HTML templates created in previous assignments using CSS or a CSS framework (such as Bootstrap, Tailwind, Bulma) with the following conditions:
  - [ X ] Customize the login, register, and add product pages to be as attractive as possible.
    - Create a new login page by changing the login.html and changing the login button to the colour black
    - Styling the register page by changing the register.html and changing the register button to the colour black
    - Styling the add product page with the same style
    - Configuring the static files in settings.py by changing the STATIC_ROOT, STATICFILESS_DIRS, and STATIC_URLS
  - [ X ] Customize the product list page to be more attractive and responsive:
    - [ x ] If there are no products saved in the application, the product list page will display an image and a message that no products are registered.
    - Create a very-sad.png in static/image and adding it to the html
    - [ X ] If there are products saved, the product list page will display details of each product using cards (Note: Must not be exactly the same as the design in the Tutorial!).
    - Did not change much from the previous assingment for the design
  - [ X ] For each product card, create two buttons to edit and delete the product on that card!
    - Adding the edit and delete button for each product card by connecting the function from views.py and adding the url path to urls.py and creating the button in html
  - [ X ]  Create a navigation bar (navbar) for the features in the application that is responsive to different device sizes, especially mobile and desktop.
  - Adding navigation bar with the the feature search product

- [ X ] Answer the following questions in README.md in the root folder (please modify the README.md you have created before; add subheadings for each assignment).
  1. If there are multiple CSS selectors for an HTML element, the priority order follows these rules:
    1. Inline Styles (`style` attribute in the HTML tag) have the highest priority.
    2. ID Selectors (`#elementID`) come next.
    3. Class Selectors, Attribute Selectors, and Pseudo-Class Selectors (`.className`, `[attribute=value]`, `:hover`) follow.
    4. Element Selectors (`elementTag`) and Pseudo-Element Selectors (`::before`, `::after`) have the lowest priority.
    5. Important rule (`!important`) overrides all other selector types.

  2. Responsive design is crucial in web application development because it ensures that web applications provide an optimal viewing experience across a wide range of devices (desktops, tablets, smartphones). Without responsive design, users may have difficulty navigating or interacting with an application, especially on smaller screens like on our phones.
    Examples of applications:
    - Implemented responsive design: Google , Twitter, Instagram .
    - Not implemented responsive design: Aren.cs.ui.ac.id.

  3. 
    - Margin: The space outside the element's border. It defines the distance between elements. We can implement it by setting margin values using margin-top, margin-right, margin-bottom, margin-left, or the shorthand margin.
    - Border: The line surrounding the padding and content, giving the element a defined boundary.We can set borders using border-width, border-style, border-color, or the shorthand border.
    - Padding: The space between the content of the element and its border.We can set padding values using padding-top, padding-right, padding-bottom, padding-left, or the shorthand padding .  . 

  4. 
    - Flexbox:
      Flexbox is a one-dimensional layout model used for laying out items in a row or a column. It excels at distributing space within an item, aligning items, and handling dynamic sizes. We can use flexbox to create navigation bars, centerig items horiozontally or vertically, and aling buttons.

    - Grid Layout:
      Grid is a two-dimensional layout system, meaning it works in both rows and columns. It allows for precise control over the positioning and sizing of items, making it ideal for more complex layouts where items need to span multiple rows or columns. We can use Grid layout to create a page layout for web pages, create a responsive design for different screen sizes or others.

  5.  Explain how you implemented the checklist above step-by-step (not just following the tutorial)!
    Already at each checkpoint
-[ X ] Perform add-commit-push to GitHub.

# TUGAS 6

- [x] Modify the previously created assignment 5 to use AJAX. . 

Step-by-step:
1. Reviewed the existing code from assignment 5.
2. Identified areas where synchronous operations could be replaced with asynchronous ones, particularly in product loading and creation.
3. Planned the necessary changes to implement AJAX for GET and POST requests for product management.

- [x] AJAX GET
   - [x] Modify the item data cards code to support AJAX GET.
   - [x] Implement task retrieval using AJAX GET.

Step-by-step:
1. Created a new JavaScript function `refreshProducts()` to fetch product data using AJAX GET.
2. Modified the `main.html` template to remove the server-side rendering of product cards.
3. Implemented a function to dynamically create and populate product cards with the data received from the AJAX GET request.
4. Called this function when the page loads and after any changes to the product list.
5. Updated the `get_product_json` view in `views.py` to return only the products belonging to the logged-in user.

- [x] AJAX POST
   - [x] Create a button that opens a modal with a form to add an item.
   - [x] Create a new view function to add a new item to the database.
   - [x] Create a `/create-ajax/` path that points to the new view function you created.
   - [x] Connect the form you created in the modal to the `/create-ajax/` path.
   - [x] Implement asynchronous refresh on the main page to display the latest item list without reloading the entire main page.

Step-by-step:
1. Added a "Add New Product" button to the `main.html` template.
2. Created a modal dialog with a form for adding new products using Tailwind CSS classes for styling.
3. Implemented a new view function `create_product_ajax` in `views.py` to handle the AJAX POST request.
4. Added a new URL pattern in `urls.py` for the `/create-product-ajax/` path.
5. Wrote JavaScript to handle form submission via AJAX POST using jQuery.
6. Updated the product list dynamically after successful form submission by calling `refreshProducts()`.

- [x] Execute the `collectstatic` command.

Step-by-step:
1. Opened a terminal.
2. Navigated to the Switchtify project directory.
3. Ran the command: `python manage.py collectstatic`
4. Confirmed that static files were collected successfully.

- [x] Answer the following questions in the README.md file in the root folder (please modify the README.md you have created; add subheadings for each assignment).
  Explain the benefits of using JavaScript in developing web applications!
  Explain why we need to use await when we call fetch()! What would happen if we don't use await?
  Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?
  On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?
  Explain how you implemented the checklist above step-by-step (not just following the tutorial)!

- [x] Perform add-commit-push to GitHub.


## Answers to Questions

1. Explain the benefits of using JavaScript in developing web applications!

JavaScript enhances web applications by enabling client-side interactivity, cross-platform compatibility, and access to a rich ecosystem of frameworks. It allows for full-stack development with Node.js, supports event-driven programming, and has wide browser support. JavaScript improves performance by offloading processing to the client-side, resulting in faster, more responsive, and scalable web applications.

2. Explain why we need to use await when we call fetch()! What would happen if we don't use await?

Using await with fetch() is crucial for handling asynchronous operations in JavaScript. It allows the code to pause execution until the Promise returned by fetch() is resolved, making the code more readable and easier to follow. Without await, fetch() immediately returns a Promise object instead of the actual data, potentially leading to errors if you try to use the result immediately. It also complicates error handling, as errors may go unnoticed if the code continues executing without waiting for the Promise to resolve.

3. Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?

The csrf_exempt decorator is used on views for AJAX POST requests to bypass Django's built-in Cross-Site Request Forgery (CSRF) protection. AJAX requests often don't include the CSRF token by default, causing Django to reject them as unsafe. While csrf_exempt provides a quick solution, it should be used cautiously as it can introduce security vulnerabilities. A safer alternative is to manually include the CSRF token in the AJAX request header.

4. On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?

Back-end sanitization is essential because front-end security can be easily bypassed by malicious users. The server is the last line of defense against attacks like SQL injection, XSS, and command injection. Back-end sanitization ensures data integrity and consistency across different clients, protects sensitive server resources, and handles untrusted external data sources. While front-end sanitization improves user experience, it cannot replace the crucial security role of back-end sanitization in safeguarding the entire system.

5. Explain how you implemented the checklist above step-by-step (not just following the tutorial)!
Step-by-step implementation details are already included in the "Implementation Steps" section above.
