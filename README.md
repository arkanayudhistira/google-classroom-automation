# Google Classroom Automation - How to Use

### Post Material dan Assignment Classroom

1. Install library yang diperlukan pada `requirements.txt` dengan menjalankan `pip install -r requirements.txt` pada anaconda prompt/terminal
2. Pastikan file `credentials.json` tersedia pada directory untuk melakukan autentikasi akun pengguna
3. Buka file `classroom-automation.ipynb` pada IDE anda kemudian Run All
4. Browser akan terbuka untuk melakukan autentikasi pada akun Google anda, gunakan email `algorit.ma`, dan kemudian klik `Allow`
5. Jika proses autentikasi berhasil, maka akan muncul `"The authentication flow has completed. You may close this window."`, dan silahkan kembali ke IDE
6. File `token.json` telah terbentuk untuk memberikan akses untuk penggunaan selanjutnya (sehingga tidak perlu melakukan autentikasi kembali)
7. Input nama course yang diinginkan untuk pembuatan post (**case-insensitive**, contoh : `wizard data visualization`)
8. Jika pembuatan suatu post berhasil, maka akan menampilkan `"Material ... created"` atau `"Assignment ... created"`
9. Post telah berhasil dibuat secara otomatis, silahkan periksa pada Google Classroom

### Grade Quiz

1. Install library yang diperlukan pada `requirements.txt` dengan menjalankan `pip install -r requirements.txt` pada anaconda prompt/terminal
2. Pastikan file `credentials.json` tersedia pada directory untuk melakukan autentikasi akun pengguna
3. Buka file `quiz-grader.ipynb` pada IDE anda
4. Pastikan link spreadsheet yang tersimpan pada `SCORE_ACADEMY_LINK` dan range sheet yang tersimpan pada `GRADE_RANGE` sudah sesuai
5. Laksanakan Run All
6. Browser akan terbuka untuk melakukan autentikasi pada akun Google anda, gunakan email `algorit.ma`, dan kemudian klik `Allow`
7. Jika proses autentikasi berhasil, maka akan muncul `"The authentication flow has completed. You may close this window."`, dan silahkan kembali ke IDE
8. File `token.json` telah terbentuk untuk memberikan akses untuk penggunaan selanjutnya (sehingga tidak perlu melakukan autentikasi kembali)
9. Pastikan nilai yang diakses sudah tepat dengan memeriksa dataframe pada section `Score Academy`
10. Input nama course yang diinginkan untuk pembuatan post (**case-insensitive**, contoh : `wizard data visualization`)
11. Input code quiz yang diinginkan untuk dilakukan penilaian (**case-insensitive**, contoh : `p4ds`), berikut list code quiz yang tersedia:
    - `P4DS` : 1. Q: Programming for Data Science (P4DS) & Practical Statistic (PS)
    - `DV` : 2. Q: Data Visualization (DV)
    - `IP` : 3. Q: Interactive Plotting (IP)
11. Jika e-mail dan nilai student ditemukan, maka akan ditampilkan pada dataframe di section `Draft Grade`. Jika e-mail/nilai student tidak ditemukan, maka akan muncul warning
12. Konfirmasi hasil grade draft yang telah dilakukan, jika sudah sesuai, ketik `y` kemudian enter
13. Jika penilaian quiz telah berhasil, maka akan menampilkan `"Quiz grades was successfully returned"`
14. Quiz telah berhasil dinilai secara otomatis, silahkan periksa pada Google Classroom

 
