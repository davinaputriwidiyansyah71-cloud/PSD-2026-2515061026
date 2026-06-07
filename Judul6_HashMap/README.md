A. Judul Program : Hash Map Menggunakan Metode Separate Chaining pada Sistem Playlist Lagu 

B. Deskripsi Singkat    	: Program ini dibuat untuk menerapkan struktur data Hash Map dengan metode Separate Chaining menggunakan Python. Data yang disimpan berupa playlist lagu yang terdiri dari id lagu dan judul lagu. id lagu digunakan sebagai key, sedangkan judul lagu digunakan sebagai value. Untuk mengatasi collision, program menggunakan linked list pada setiap indeks hash table. Program dapat digunakan untuk menambah data lagu, mencari lagu berdasarkan id, menghapus lagu, dan menampilkan seluruh data yang tersimpan. Dengan penerapan Hash Map, proses pencarian data menjadi lebih cepat dan pengelolaan playlist dapat dilakukan dengan lebih efisien.

C.	Source Code	:
<img width="1366" height="720" alt="Screenshot 2026-06-07 123431" src="https://github.com/user-attachments/assets/be040ea4-461f-423b-ab19-38d12d9f5a0e" />
<img width="1366" height="720" alt="Screenshot 2026-06-07 123445" src="https://github.com/user-attachments/assets/54311ef6-9ea7-4ba4-a08c-ed558603ec5b" />
<img width="1366" height="720" alt="Screenshot 2026-06-07 123455" src="https://github.com/user-attachments/assets/d57abded-6d22-4364-b52c-7326c337da49" />
Penjelasan Kode Program Perbarisnya :
1.	Class Node digunakan sebagai tempat untuk menyimpan data pada linked list.
2.	Method _init_ dijalankan saat objek node dibuat dan menerima data key serta value.
3.	Menyimpan nilai key yang berfungsi sebagai identitas data.
4.	Menyimpan nilai value yang berisi informasi dari data tersebut.
5.	Menginisialisasi pointer next dengan nilai None karena node belum terhubung ke node lain.
6.	-
7.	-
8.	Mendefinisikan class Hash Map yang menggunakan metode Separate Chaining.
9.	Digunakan untuk menentukan ukuran tabel hash, defaultnya adalah 10.
10.	Menyimpan ukuran hash table ke dalam atribut SIZE.
11.	Membuat tabel hash berupa list yang berisi nilai None sebanyak ukuran yang ditentukan.
12.	-
13.	Mendefinisikan fungsi hash yang menerima parameter key.
14.	Menghasilkan indeks penyimpanan dengan menggunakan operasi modulo (%) terhadap ukuran tabel.
15.	-
16.	Method insert digunakan untuk menambahkan data ke dalam Hash Map.
17.	Menghitung indeks penyimpanan menggunakan fungsi hash.
18.	Mengambil node pertama pada slot tersebut.
19.	Menelusuri linked list yang ada pada slot.
20.	Mengecek apakah key sudah ada.
21.	Jika ada, value diperbarui.
22.	Proses selesai dan method dihentikan.
23.	Jika belum ditemukan, lanjut ke node berikutnya.
24.	Membuat node baru jika key belum ada.
25.	Menghubungkan node baru dengan node sebelumnya pada slot.
26.	Menjadikan node baru sebagai node pertama pada slot hash table.
27.	-
28.	Digunakan untuk mencari data berdasarkan key.
29.	Menghitung indeks menggunakan fungsi hash.
30.	Mengambil node pertama pada slot yang sesuai.
31.	Menelusuri linked list selama masih ada node.
32.	Mengecek apakah key yang dicari sama dengan key pada node saat ini.
33.	Jika ditemukan, node tersebut langsung dikembalikan.
34.	Jika belum sesuai, lanjut ke node berikutnya.
35.	Jika seluruh node sudah diperiksa tetapi data tidak ditemukan, method mengembalikan nilai None.
36.	-
37.	Untuk menghapus data berdasarkan key.
38.	Menghitung indeks penyimpanan menggunakan fungsi hash.
39.	Mengambil node pertama pada slot tersebut.
40.	Membuat variabel prev untuk menyimpan node sebelumnya.
41.	Melakukan penelusuran linked list selama masih ada node.
42.	Memeriksa apakah key yang dicari sama dengan key pada node saat ini.
43.	Mengecek apakah node yang akan dihapus berada di posisi pertama.
44.	Jika node pertama, maka head akan dipindahkan ke node berikutnya.
45.	Jika bukan node pertama
46.	Maka hubungan node sebelumnya langsung diarahkan ke node setelah node yang dihapus.
47.	Mengembalikan nilai True sebagai tanda bahwa penghapusan berhasil.
48.	Menyimpan posisi node saat ini ke variabel prev.
49.	Berpindah ke node berikutnya.
50.	Jika data tidak ditemukan sampai akhir linked list, method mengembalikan nilai False.
51.	-
52.	Untuk menampilkan seluruh isi hash table.
53.	Menampilkan judul tampilan data.
54.	Melakukan perulangan untuk setiap slot pada hash table.
55.	Menampilkan nomor indeks slot yang sedang diperiksa.
56.	Mengambil node pertama pada slot tersebut.
57.	Menelusuri linked list pada slot tersebut.
58.	Menampilkan key dan value dari setiap node.
59.	Berpindah ke node berikutnya.
60.	Menampilkan tulisan NONE sebagai penanda akhir linked list pada slot tersebut.
61.	-
62.	Mendefinisikan fungsi utama program.
63.	Membuat objek hash map bernama playlist.
64.	Menambahkan lagu "Hati-Hati di Jalan" dengan id 9.
65.	Menambahkan lagu "Sial" dengan id 21.
66.	Menambahkan lagu "Komang" dengan id 76.
67.	Menambahkan lagu "Monokrom" dengan id 6. slot: 6 % 10 = 6 (collision dengan Komang, disisip di depan).
68.	Menampilkan seluruh isi playlist yang tersimpan.
69.	Mencari lagu dengan ID 21 dan menyimpan hasilnya ke variabel hasil.
70.	Mengecek apakah data lagu berhasil ditemukan.
71.	Jika ditemukan, menampilkan judul lagu yang sesuai.
72.	Jika data tidak ditemukan.
73.	Menampilkan pesan bahwa lagu tidak tersedia.
74.	Menghapus lagu dengan id 21 dari playlist.
75.	Menampilkan informasi bahwa lagu telah dihapus.
76.	Menampilkan kembali isi playlist setelah proses penghapusan.
77.	-
78.	Digunakan untuk memastikan fungsi main() hanya dijalankan ketika file dieksekusi secara langsung.
79.	Menjalankan fungsi main.

D.    Output Program:
<img width="1366" height="720" alt="Screenshot 2026-06-07 122219" src="https://github.com/user-attachments/assets/d2c08f4b-32a1-4388-a3c2-6a57e8ceb5e1" />
Saat program dijalankan, sistem memasukkan empat data lagu ke dalam Hash Map. Lagu "Hati-Hati di Jalan" disimpan slot 9, lagu "Sial" slot 1, dan lagu "Komang" slot 6. Ketika lagu "Monokrom" dimasukkan, terjadi collision karena memiliki indeks yang sama dengan "Komang", yaitu slot 6. Untuk mengatasi collision tersebut, program menggunakan metode Separate Chaining. Data "Monokrom" disimpan di depan linked list pada slot 6, sedangkan "Komang" berada setelahnya. Karena itu, pada slot 6 terlihat dua data yang saling terhubung dalam satu rantai.
 
Setelah semua lagu dimasukkan, hash table menampilkan data yang tersimpan. Slot 1 berisi lagu "Sial", slot 6 berisi "Monokrom" dan "Komang", serta slot 9 berisi "Hati-Hati di Jalan". Slot lainnya masih kosong dan ditampilkan sebagai NONE.
 
Selanjutnya lagu "Sial" dengan key 21 dihapus dari Hash Map. Karena data berada di slot 1 dan merupakan satu-satunya node pada slot tersebut, setelah dihapus slot 1 menjadi kosong.
 
Setelah proses penghapusan selesai, hash table ditampilkan kembali. Slot 1 sudah berubah menjadi NONE karena lagu "Sial" berhasil dihapus. Sementara itu, data pada slot 6 dan slot 9 tetap sama karena tidak terpengaruh oleh proses penghapusan.

E. Link Youtube : https://youtu.be/uVywuWaCdio?si=H4oHOqMnygUzSEdk

