A. Judul Program: Pencarian Kode Buku yang Dipinjam di Perpustakaan

B. Deskripsi Singkat: Program tersebut menggunakan metode Sequential Search untuk mencari kode buku pada data peminjaman perpustakaan. Program akan memeriksa data satu per satu dari awal hingga akhir untuk mengetahui apakah kode buku yang dicari ada di dalam array. Selain menghitung berapa kali kode buku muncul, program juga menampilkan indeks pertama kali kode buku tersebut ditemukan dan indeks terakhir kali kode buku ditemukan. Jika data tidak ada, maka program akan menampilkan pesan bahwa kode buku tidak ditemukan.

C. Source Code: 
<img width="1366" height="720" alt="Screenshot 2026-05-08 150821" src="https://github.com/user-attachments/assets/1928747c-007a-43f8-aaba-d46790a1ae33" />
<img width="1366" height="720" alt="Screenshot 2026-05-08 150833" src="https://github.com/user-attachments/assets/1369132d-e389-429e-9cbb-dd4d9fcd4c06" />
Penjelasan Kode Program Perbarisnya :
1. Mendefinisikan fungsi bernama sequential_search dengan tiga parameter: data (list yang dicari), n (jumlah elemen list), dan target (nilai yang ingin ditemukan). 
2. Variabel i diinisialisasi dengan nilai 0. Ini adalah indeks awal yang digunakan untuk menelusuri setiap elemen list dari posisi pertama (index ke-0).
3. Menghitung jumlah kemunculan target pada data
4. Variabel first_index diinisialisasi dengan nilai -1. Nilai -1 dipakai sebagai tanda 'belum ditemukan'. Variabel ini akan menyimpan indeks pertama kali target muncul dalam list.
5. Variabel last_index diinisialisasi dengan nilai -1. Sama seperti first_index, nilai -1 berarti belum ada kemunculan. Variabel ini akan selalu diperbarui setiap kali target ditemukan, sehingga pada akhirnya menyimpan kemunculan terakhir.
6. while i < n artinya ulangi selama nilai i masih lebih kecil dari n (jumlah elemen). Loop ini memastikan setiap elemen list diperiksa satu per satu dari indeks 0 hingga n-1. 
7. if data[i] == target merupakan cek apakah elemen pada posisi indeks i sama dengan nilai yang dicari (target). Jika sama, blok di dalam if akan dijalankan. Jika tidak, program langsung lanjut ke i += 1.
8. counter += 1 berarti counter = counter + 1. Setiap kali target ditemukan, counter bertambah 1. Ini memungkinkan program mengetahui berapa kali kode buku yang dicari muncul.
9. if first_index == -1 mengecek apakah first_index masih bernilai -1 (belum pernah diisi). Jika ya, berarti ini adalah kali pertama target ditemukan, sehingga indeks ini perlu disimpan. 
10. first_index = i menyimpan nilai i (posisi saat ini) ke dalam first_index. Ini hanya terjadi sekali saat pertama kali target ditemukan  karena kondisi di baris 9 hanya terpenuhi ketika first_index masih -1.
11. last_index = i memperbarui last_index dengan nilai indeks saat ini. Baris ini selalu dijalankan setiap kali target ditemukan tanpa pengecekan tambahan. Sehingga nilainya terus diperbarui dan pada akhir loop akan berisi indeks kemunculan target yang paling akhir.
12. i += 1 menambah nilai i sebesar 1, sehingga pada iterasi berikutnya program akan memeriksa elemen di posisi berikutnya. Baris ini ada di luar blok if, artinya i selalu bertambah 1 setiap iterasi, baik target ditemukan maupun tidak. 
13. return counter, first_index, last_index mengembalikan tiga nilai sekaligus ke pemanggil fungsi: (1) counter berapa kali target muncul, (2) first_index indeks kemunculan pertama, (3) last_index indeks kemunculan terakhir. Python mengemas ketiganya sebagai tuple.
14. -
15. -
16. def main(): mendefinisikan fungsi utama program. 
17. Data yang berisi list kode-kode buku yang tercatat dipinjam 
18. Jumlah data dalam list 
19. Menampilkan seluruh isi list kepada user sebelum pencarian dimulai 
20. Membuat perulangan tak terbatas, tujuannya supaya program terus meminta input sampai user memasukkan data yang valid (angka).  
21. Meminta input kode buku yang dicari dan memastikan input valid
22. Meminta input kode buku yang ingin dicari
23. Keluar dari loop jika input valid sesuai list 
24. except ValueError: menangkap error yang terjadi saat int() menerima nilai yang bukan angka 
25. Memberi tahu user bahwa inputnya salah. 
26. Memanggil fungsi yang sudah didefinisikan di atas. Tiga nilai yang dikembalikan fungsi (return baris 18) langsung di-unpack ke dalam tiga variabel sekaligus dalam satu baris. 
27. Mengecek apakah counter lebih dari 0. Jika ya, berarti target paling tidak muncul satu kali dalam data. Jika counter == 0, target tidak ditemukan dan program masuk ke blok else. 
28. Menampilkan informasi lengkap: (1) kode buku yang dicari, (2) berapa kali muncul (counter), (3) indeks pertama kali ditemukan (first_index), dan (4) indeks terakhir ditemukan (last_index). Menggunakan f-string untuk menyisipkan nilai variabel ke dalam teks.
29. Menampilkan informasi lengkap: (1) kode buku yang dicari, (2) berapa kali muncul (counter), (3) indeks pertama kali ditemukan (first_index), dan (4) indeks terakhir ditemukan (last_index). Menggunakan f-string untuk menyisipkan nilai variabel ke dalam teks.
30. Blok ini dijalankan hanya jika kondisi if tidak terpenuhi. 
31. Menampilkan pesan bahwa kode buku yang dicari tidak ada dalam data peminjaman. 
32. -
33. Memastikan bahwa fungsi main() hanya dijalankan ketika skrip ini dieksekusi langsung, bukan ketika diimpor sebagai modul.
34. Memanggil fungsi utama dan memulai jalannya seluruh program.  

D. Output Program: 
<img width="1366" height="720" alt="Screenshot 2026-05-08 151053" src="https://github.com/user-attachments/assets/a1f8e1f6-8770-4814-82a4-9d3b6c9c8f83" />
Penjelasan output source code tersebut :  
Program tersebut digunakan untuk mencari kode buku yang dipinjam dengan metode Sequential Search atau pencarian berurutan. Pada output pada gambar Data yang dicek adalah: [210, 315, 210, 400, 210, 512, 315, 210, 200, 400, 512]. Program akan mengecek data satu per satu dari awal hingga akhir, user memasukkan kode buku 210. Setelah proses pencarian selesai, program menampilkan bahwa kode buku 210 dipinjam sebanyak 4 kali. Selain itu, program juga menunjukkan bahwa data pertama kali ditemukan pada indeks ke-0 dan terakhir ditemukan pada indeks ke-7. Hal ini berarti angka 210 muncul di beberapa posisi dalam daftar data, yaitu pada indeks 0, 2, 4, dan 7. Dengan demikian, program berhasil menghitung jumlah kemunculan data sekaligus mengetahui posisi awal dan posisi akhir data yang dicari. 

E. Link YouTube : https://youtu.be/gp9OMJsH0eQ?si=-gFTrhEJ8yl7oc8c




