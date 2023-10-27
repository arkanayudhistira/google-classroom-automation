# Google Classroom Automation - How to Use

Sebelum mengakses aplikasi, pastikan anda telah mempersiapkan hal-hal berikut:
- Python dan Visual Studio Code
- Instalasi library yang diperlukan pada `requirements.txt` di virtual environment dengan menjalankan
  
   ```
   pip install -r requirements.txt
   ```
- File `credentials.json` tersedia pada directory untuk melakukan autentikasi akun pengguna
   
## Grade Quiz (Streamlit Dashboard)

1. Buka Visual Studio Code dan pastikan virtual environment yang digunakan telah sesuai (pada bagian pojok kanan bawah) <br>
    ![image](https://github.com/arkanayudhistira/google-classroom-automation/assets/100895120/38e04660-93fa-4d0a-ae8f-7492b7cc526d)
   
2. Pilih menu Terminal di bagian kiri atas dan pilih New Terminal <br>
    ![image](https://github.com/arkanayudhistira/google-classroom-automation/assets/100895120/916f4b60-e2f1-40c9-9206-2449c6b3a1e2)

3. Buka Dashboard Streamlit dengan menjalankan code berikut: <br>
   ```
   streamlit run app.py
   ```
4. Pilih nama classroom, spesialisasi, kelas, sheet Score Academy, dan upload file CSV hasil quiz dari Algoritma Online WP Admin
5. Klik **Grade Quiz** untuk me-return nilai quiz student di Google Classroom dan mencatat di sheet Score Academy

## Post Material dan Assignment Classroom

1. Buka file `classroom-automation.ipynb` pada IDE anda kemudian Run All
4. Browser akan terbuka untuk melakukan autentikasi pada akun Google anda, gunakan email `algorit.ma`, dan kemudian klik `Allow`
5. Jika proses autentikasi berhasil, maka akan muncul `"The authentication flow has completed. You may close this window."`, dan silahkan kembali ke IDE
6. File `token.json` telah terbentuk untuk memberikan akses untuk penggunaan selanjutnya (sehingga tidak perlu melakukan autentikasi kembali)
7. Input nama course yang diinginkan untuk pembuatan post (**case-insensitive**, contoh : `wizard data visualization`)
8. Jika pembuatan suatu post berhasil, maka akan menampilkan `"Material ... created"` atau `"Assignment ... created"`
9. Post telah berhasil dibuat secara otomatis, silahkan periksa pada Google Classroom

## Grade Quiz (Notebook)

1. Buka file `quiz-grader.ipynb` pada IDE anda
4. Pastikan link spreadsheet yang tersimpan pada `SCORE_ACADEMY_LINK` dan range sheet yang tersimpan pada `GRADE_RANGE` sudah sesuai
5. Lakukan Run All
6. Browser akan terbuka untuk melakukan autentikasi pada akun Google anda, gunakan email `algorit.ma`, dan kemudian klik `Allow`
7. Jika proses autentikasi berhasil, maka akan muncul `"The authentication flow has completed. You may close this window."`, dan silahkan kembali ke IDE
8. File `token.json` telah terbentuk untuk memberikan akses untuk penggunaan selanjutnya (sehingga tidak perlu melakukan autentikasi kembali)
9. Pastikan nilai yang diakses sudah tepat dengan memeriksa dataframe pada section `Score Academy`
10. Input nama course yang diinginkan untuk pembuatan post (**case-insensitive**, contoh : `wizard data visualization`)
11. Input code quiz yang diinginkan untuk dilakukan penilaian (**case-insensitive**, contoh : `p4ds`), berikut list code quiz yang tersedia:
    - `P4DS` : 1. Q: Programming for Data Science (P4DS) & Practical Statistic (PS)
    - `DV` : 2. Q: Data Visualization (DV)
    - `IP` : 3. Q: Interactive Plotting (IP)
11. Nama, nilai, dan status hasil penilaian akan ditampilkan pada dataframe di section `Draft Grade`. Jika e-mail/nilai student tidak ditemukan, maka akan muncul warning
12. Konfirmasi hasil grade draft yang telah dilakukan di Google Classroom, pastikan nilai-nilai sudah sesuai. Jika sudah sesuai, ketik `y` kemudian enter
13. Jika penilaian quiz telah berhasil, maka akan menampilkan `"Quiz grades was successfully returned"`
14. Quiz telah berhasil dinilai secara otomatis, silahkan periksa pada Google Classroom

 ## Pembuatan File `credentials.json`

 Jika file `credentials.json` hilang/tidak bisa digunakan untuk melakukan autentikasi, anda dapat membuat file credentials baru. Secara keseluruhan, guide pembuatan file tersebut telah disediakan oleh Google pada [Classroom Quickstart](https://developers.google.com/classroom/quickstart/python). Berikut step-step yang perlu dilaksanakan:
 1. Membuat Google Cloud Project dengan melakanakan step-step dari [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)
 2. Mengaktivasi API Google Classroom sesuai dengan guide pada section [Enable the API](https://developers.google.com/classroom/quickstart/python#enable_the_api)
 3. Konfigurasi OAuth consent screen sesuai dengan guide pada section [Configure the OAuth consent screen](https://developers.google.com/classroom/quickstart/python#configure_the_oauth_consent_screen)
 4. Berikan nama `Algoritma` untuk mengisi App Name OAuth consent screen
 5. Melakukan pembuatan file **credential** sesuai dengan guide pada section [Authorize credentials for a desktop application](https://developers.google.com/classroom/quickstart/python#authorize_credentials_for_a_desktop_application)
 6. Rename file credential yang telah didownload menjadi `credentials.json` dan letakkan pada directory notebook
