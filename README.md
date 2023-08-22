# Google Classroom Automation

### Post Material dan Assignment Classroom

1. Install library yang diperlukan pada `requirements.txt` dengan menjalankan `pip install -r requirements.txt` pada anaconda prompt/terminal
2. Buka file `classroom-automation.ipynb` kemudian Run All
3. Input nama course yang diinginkan untuk pembuatan post (**case-insensitive**, contoh : `wizard data visualization`)
4. Jika pembuatan suatu post berhasil, maka akan menampilkan `"Material ... created"` atau `"Assignment ... created"`
5. Post telah berhasil dibuat secara otomatis, silahkan periksa pada Google Classroom

### Grade Quiz

1. Install library yang diperlukan pada `requirements.txt` dengan menjalankan `pip install -r requirements.txt` pada anaconda prompt/terminal
2. Buka file `quiz-grader.ipynb`
3. Pastikan link spreadsheet yang tersimpan pada `SCORE_ACADEMY_LINK` dan range sheet yang tersimpan pada `GRADE_RANGE` sudah sesuai
4. Laksanakan Run All
5. Pastikan nilai yang diakses sudah tepat dengan memeriksa dataframe pada section `Score Academy`
6. Input nama course yang diinginkan untuk pembuatan post (**case-insensitive**, contoh : `wizard data visualization`)
7. Input code quiz yang diinginkan untuk dilakukan penilaian (**case-insensitive**, contoh : `p4ds`), berikut list code quiz yang tersedia:
   - `'P4DS'` : 1. Q: Programming for Data Science (P4DS) & Practical Statistic (PS)
   - `'DV'` : 2. Q: Data Visualization (DV)
   - `'IP'` : 3. Q: Interactive Plotting (IP)
8. Jika e-mail dan nilai student ditemukan, maka akan ditampilkan pada dataframe di section `Draft Grade`. Jika e-mail/nilai student tidak ditemukan, maka akan muncul warning
9. Konfirmasi hasil grade draft yang telah dilakukan, jika sudah sesuai, ketik `y` kemudian enter
10. Jika penilaian quiz telah berhasil, maka akan menampilkan `"Quiz grades was successfully returned"`
11. Quiz telah berhasil dinilai secara otomatis, silahkan periksa pada Google Classroom

 
