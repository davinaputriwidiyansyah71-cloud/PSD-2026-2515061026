A. Judul Program: Sistem Riwayat Checkout Barang di Gudang Ekspedisi

B. Deskripsi Singkat: Program ini dibuat untuk mensimulasikan sistem riwayat checkout barang pada gudang ekspedisi menggunakan struktur data Stack Array. Konsep yang digunakan adalah LIFO (Last In First Out), dimana barang yang terakhir masuk ke rak akan menjadi barang pertama yang keluar saat proses checkout.
Program ini memiliki beberapa fitur seperti menambah barang, checkout barang, melihat barang teratas, menampilkan isi rak, menghitung jumlah barang, dan mengosongkan rak. Dengan program ini, saya jadi lebih memahami bagaimana cara kerja stack diterapkan pada situasi yang ada di dunia nyata, khususnya pada sistem penyimpanan barang di gudang ekspedisi.

C. Source Code: 
<img width="1366" height="720" alt="Screenshot 2026-05-14 022510" src="https://github.com/user-attachments/assets/490791b3-7ae0-49db-b6fd-787d281b2da5" />
<img width="1366" height="720" alt="Screenshot 2026-05-14 022548" src="https://github.com/user-attachments/assets/c90ab018-8779-43dc-aa4d-dfac14e16274" />
<img width="1366" height="720" alt="Screenshot 2026-05-14 022558" src="https://github.com/user-attachments/assets/5491794f-bc77-4802-b1c4-a513d99cf54a" />

Penjelasan Kode Program Perbarisnya :
1. Sebagai implementasi stack menggunakan array untuk mengelola barang di gudang  ekspedisi
2. Fungsi inisialisasi, dipanggil otomatis saat objek dibuat. Default kapasitas 100
3. Simpan batas maksimal rak ke variabel max
4. Membuat array kosong untuk menyimpan data barang.
5. Penanda posisi teratas stack. -1 berarti stack masih kosong
6. -
7. Fungsi cek apakah stack kosong
8. Kalau top_idx masih -1, berarti belum ada barang > kembalikan True
9. -
10. Fungsi cek apakah stack sudah penuh
11. Kalau top_idx sudah di posisi terakhir array > kembalikan True
12. -
13. Fungsi untuk menambah barang ke atas stack
14. Mengecek dahulu, apakah rak sudah penuh?
15. Kalau penuh akan mencetak kasih peringatan “Rak gudang penuh!”
16. Hentikan fungsi, tidak bisa tambah barang lagi
17. Menaikan posisi top satu langkah ke atas
18. Untuk menyimpan nama barang pada stack
19. Konfirmasi ke user bahwa barang berhasil masuk dengan mencetak “Barang '{barang}' berhasil ditambahkan”
20. -
21. Fungsi untuk mengambil/checkout barang paling atas
22. Mengecek apakah rak kosong
23. Kalau kosong, kasih peringatan dengan mencetak “Tidak ada barang di rak”
24. Hentikan fungsi karena tidak ada yang bisa diambil
25. Menampilkan nama barang yang diambil
26. Turunkan posisi top satu langkah barang dianggap sudah diambil
27. -
28. Fungsi untuk intip barang paling atas tanpa menghapusnya
29. Mengecek apakah rak kosong
30. Jika kosong, maka akan beritahu user dengan mencetak “Rak kosong”
31. Hentikan fungsi
32. Menampilkan nama barang di posisi paling atas stack
33. -
34. Fungsi untuk menampilkan semua barang yang ada di rak
35. Cek apakah rak kosong
36. Jika kosong maka akan beri peringatan 
37. Hentikan fungsi
38. Menampilkan judul isi stack.
39. Perulangan untuk menampilkan data dari atas ke bawah.
40. Cetak nama barang satu per satu dari yang paling atas
41. -
42. Fungsi untuk hitung total barang di rak
43. Menampilkan jumlah pada stack top_idx + 1 karena index mulai dari 0, jadi totalnya selalu +1
44. Fungsi untuk kosongkan seluruh rak sekaligus
45. Untuk mengosongkan rak dengan mengatur top_idx kembali ke -1
46. Konfirmasi ke user bahwa rak sudah kosong
47. -
48. -
49. Fungsi utama tempat program berjalan
50. Buat objek stack baru dengan kapasitas default 100
51. Set pilihan awal ke 0 agar bisa masuk ke while loop
52. Terus tampilkan menu selama user belum pilih 7 (Keluar)
53. Cetak judul menu utama
54. Menampilkan menu ke 1 pada user
55. Menampilkan menu ke 2 pada user
56. Menampilkan menu ke 3 pada user
57. Menampilkan menu ke 4 pada user
58. Menampilkan menu ke 5 pada user
59. Menampilkan menu ke 6 pada user
60. Menampilkan menu ke 7 pada user
61. -
62. Coba tangkap input dari user
63. Minta user pilih menu, konversi ke integer
64. Kalau user ketik huruf/simbol bukan angka, tangkap errornya
65. Kasih peringatan input salah
66. Langsung ulang loop dari awal tanpa proses pilihan
67. Jika user pilih menu 1
68. Minta user ketik nama barang
69. Panggil fungsi push untuk memasukkan barang ke stack
70. Jika user pilih menu 2
71. Panggil fungsi pop untuk ambil barang teratas
72. Jika user pilih menu 3
73. Panggil fungsi peek untuk intip barang teratas
74. Jika user pilih menu 4
75. Panggil fungsi display untuk tampilkan semua barang
76. Jika user pilih menu 5
77. Panggil fungsi count untuk hitung total barang
78. Jika user pilih menu 6
79. Panggil fungsi clear untuk kosongkan semua barang
80. Jika user pilih menu 7 (keluar)
81. Tampilkan pesan program selesai sebelum program berhenti
82. Jika angka yang diketik tidak ada di menu (misal: 8, 9, 99)
83. Kasih tahu user bahwa pilihannya tidak tersedia
84. -
85. untuk memastikan main() hanya dijalankan saat file ini dieksekusi langsung, bukan saat diimpor sebagai modul
86. Jalankan program dari fungsi main!

D. Output Program: 
<img width="1366" height="720" alt="Screenshot 2026-05-14 031147" src="https://github.com/user-attachments/assets/d4c5b83a-380f-48ee-aaee-50dbc025c534" />
<img width="1366" height="720" alt="Screenshot 2026-05-14 031159" src="https://github.com/user-attachments/assets/a36bf8c5-1242-433f-9976-6aa1aad7ffdb" />
<img width="1366" height="720" alt="Screenshot 2026-05-14 031214" src="https://github.com/user-attachments/assets/839ae326-1985-4184-b8bb-e25897579475" />
<img width="314" height="220" alt="Screenshot 2026-05-14 031227" src="https://github.com/user-attachments/assets/ed646194-3589-43be-beb0-499296d4fc4d" />

Penjelasan output source code tersebut :  
Jadi pertama kali program dijalankan, muncul deh tuh menu GUDANG EKSPEDISI lengkap dari pilihan 1 sampai 7. Nah di sini saya coba iseng ketik "HandPhone" di bagian "Pilih menu". Yang mana keluar pesan “Input harus angka!”

Menu muncul lagi, saya pilih angka 1 (Tambah Barang). Program langsung minta: Masukkan nama barang saya meng inputkan menu 1 tiga kali yang mana Tv > Kulkas > Laptop (paling atas).

Pilih 2 (Checkout Barang). Program langsung ambil barang yang paling atas: Barang ‘Laptop’ berhasil checkout. Laptop diambil duluan karena dia yang paling atas.

Pilih 3 (Lihat Barang Teratas). Program intip barang paling atas tanpa mengambilnya: Barang paling atas: Kulkas. Setelah Laptop di-checkout, yang jadi di paling atas sekarang adalah Kulkas. Fungsi peek ini sifatnya cuma ngintip saja, tidak mengambil.

Pilih 4 (Tampilkan Semua Barang). Program tampilkan seluruh isi rak dari atas ke bawah:Isi rak gudang: - Kulkas - Tv, Kulkas tampil duluan karena posisinya di atas, baru Tv di bawahnya. Ini bukan urutan input, tapi urutan posisi di stack

Pilih 5 (Hitung Total Barang): Total barang dalam rak: 2, Kulkas sama Tv.

Pilih 6 (Kosongkan Rak): Semua barang berhasil dikosongkan, Program reset top_idx balik ke -1, artinya stack dianggap kosong total.

Pilih 7 (Keluar): Program selesai, Program langsung berhenti while loop berhenti karena kondisi pilih != 7 sudah tidak terpenuhi.


E. Link YouTube : https://youtu.be/WAErs5cR6Rg?si=TdHipEiEmlBrI0Ew


