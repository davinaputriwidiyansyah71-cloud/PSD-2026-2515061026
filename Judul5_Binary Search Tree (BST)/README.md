A. Judul Program: Manajemen Ruang ICU Klinik Menggunakan Binary Search Tree (BST)

B. Deskripsi Singkat: Program dibuat untuk mengelola data ruang ICU di sebuah klinik menggunakan metode Binary Search Tree (BST). Program ini dapat digunakan untuk menambah nomor ruang ICU, mencari ruang cadangan terdekat yang lebih besar maupun lebih kecil, menghapus ruang yang sudah penuh, serta menampilkan seluruh daftar ruang ICU secara terurut. 

C. Source Code:
<img width="1366" height="720" alt="Screenshot 2026-05-21 212620" src="https://github.com/user-attachments/assets/b79ade87-a329-49a6-ad95-05e9d497cb50" />
<img width="1366" height="720" alt="Screenshot 2026-05-21 212647" src="https://github.com/user-attachments/assets/1428ad8a-e8bf-403d-9bae-fa07f7f458df" />
<img width="1366" height="720" alt="Screenshot 2026-05-21 212658" src="https://github.com/user-attachments/assets/33cc13c8-ef53-4da3-acc6-5f40a33763db" />
<img width="1366" height="720" alt="Screenshot 2026-05-21 212721" src="https://github.com/user-attachments/assets/ab2139d9-a077-4de2-8f0f-e9c483e276b3" />
<img width="1366" height="720" alt="Screenshot 2026-05-21 212736" src="https://github.com/user-attachments/assets/748f77df-a844-41f6-be5e-fbdc3817018d" />
<img width="1366" height="720" alt="Screenshot 2026-05-21 212803" src="https://github.com/user-attachments/assets/dff0f5c3-7f98-4d04-b141-c1eec32ebdfc" />
Penjelasan Kode Program Perbarisnya :
1.	Bikin class Node sebagai cetakan tiap simpul pohon
2.	Fungsi __init__ untuk inisialisasi node dengan parameter key 
3.	Simpan nilai key di node ini 
4.	Menyimpan node anak kiri yang mana itu masih kosong
5.	Menyimpan node anak kanan yang mana itu masih kosong 
6.	–
7.	Bikin class BSTKlinik, isinya semua operasi BST
8.	Fungsi _init_ untuk inisialisasi BST 
9.	Root (akar pohon) yang mana kosong pada awalnya
10.	–
11.	Fungsi rekursif untuk menyisipkan node baru
12.	Jika root kosong, buat node baru dengan key yang diberikan
13.	mengembalikan node baru sebagai root
14.	jika key yang akan dimasukkan lebih kecil dari key root, masukkan ke subtree kiri
15.	rekursif memanggil insert_node pada subtree kiri dan mengupdate root.left dengan hasilnya
16.	jika key yang akan dimasukkan lebih besar dari key root, masukkan ke subtree kanan
17.	rekursif memanggil insert_node pada subtree kanan dan mengupdate root.right dengan hasilnya
18.	mengembalikan root yang sudah diperbarui setelah penambahan node baru
19.	–
20.	fungsi untuk menambahkan node baru dengan key yang diberikan ke dalam pohon
21.	memanggil insert_node dengan root saat ini dan key yang akan dimasukkan, lalu mengupdate root dengan hasilnya
22.	–
23.	Fungsi untuk cari node dengan nilai terkecil
24.	Mulai dari root
25.	selama current tidak kosong dan masih memiliki anak kiri, terus bergerak ke kiri
26.	update current ke anak kiri
27.	mengembalikan node dengan key terkecil
28.	–
29.	Fungsi traversal inorder (kiri > tengah > kanan)
30.	jika root kosong, tidak ada yang perlu ditampilkan
31.	Kembali 
32.	memanggil inorder pada subtree kiri
33.	menampilkan key dari node saat ini
34.	memanggil inorder pada subtree kanan
35.	–
36.	Fungsi rekursif untuk hapus node berdasarkan key
37.	Jika node kosong
38.	Kembali 
39.	jika key yang akan dihapus lebih kecil dari key root, 
40.	cari dan hapus di subtree kiri
41.	jika key yang akan dihapus lebih besar dari key root
42.	cari di subtree kanan
43.	jika key ditemukan
44.	Cek, kalau tidak punya anak sama sekali
45.	hapus langsung, return None
46.	Kalau tidak punya anak kiri
47.	gantikan dengan anak kanan
48.	Kalau tidak punya anak kanan
49.	gantikan dengan anak kiri
50.	Kalau punya dua anak
51.	cari successor (nilai terkecil di kanan)
52.	ganti key node ini dengan key successor
53.	hapus successor dari subtree kanan
54.	Kembalikan node yang sudah diperbarui
55.	–
56.	Fungsi publik untuk hapus node
57.	Panggil delete_node mulai dari root
58.	–
59.	Fungsi untuk cari ruang cadangan lebih besar dari key
60.	Mulai pencarian dari root
61.	untuk menyimpan kandidat successor yang ditemukan selama pencarian
62.	selama current tidak kosong, terus mencari node dengan key yang sesuai
63.	Kalau key lebih kecil dari node sekarang
64.	node ini kandidat successor, simpan
65.	update successor dan bergerak ke kiri
66.	Jika key lebih besar
67.	terus cari di subtree kanan tanpa mengupdate successor karena successor harus lebih besar dari key
68.	Kalau sama persis
69.	Berhenti
70.	Kalau node tidak ditemukan di tree
71.	return None, False
72.	jika node memiliki anak kanan 
73.	cari successor di subtree kanan
74.	jika tidak ada successor yang ditemukan, berarti tidak ada ruang cadangan lebih besar
75.	return None, False
76.	mengembalikan key successor dan True
77.	–
78.	Fungsi untuk cari ruang cadangan lebih kecil dari key
79.	Mulai dari root 
80.	variabel untuk menyimpan kandidat predecessor
81.	Selama node masih ada
82.	Kalau key lebih besar dari node sekarang
83.	node ini kandidat predecessor, simpan 
84.	geser ke kanan 
85.	Kalau key lebih kecil
86.	geser ke kiri 
87.	Kalau sama persis
88.	berhenti 
89.	Kalau node tidak ditemukan
90.	return None, False 
91.	Kalau node punya anak kiri
92.	ambil node terkanan dari subtree kiri 
93.	terus geser ke kanan sampai ujung 
94.	pergerakan ke kanan untuk mencari predecessor terbesar di subtree kiri
95.	simpan sebagai predecessor
96.	Kalau tidak ada predecessor
97.	return None, False
98.	Return key predecessor dan True (berhasil)
99.	–
100.	Fungsi utama program 
101.	Buat objek BST baru 
102.	pilih 0 sebagai nilai awal menu
103.	–
104.	Looping terus sampai user pilih 6 (keluar) 
105.	Tampilkan Judul menu 
106.	Menu 1: Tambah ruang ICU 
107.	Menu 2: Cari ruang cadangan lebih besar 
108.	Menu 3: Cari ruang cadangan lebih kecil 
109.	Menu 4: Hapus ruang penuh 
110.	Menu 5: Tampilkan semua ruang 
111.	Menu 6: Keluar
112.	–
113.	Coba ambil input user 
114.	Konversi input jadi integer 
115.	Kalau bukan angka
116.	tampilkan pesan error 
117.	ulangi loop
118.	–
119.	Kalau pilih 1 (tambah ruang)
120.	Coba ambil input nomor ruang 
121.	Konversi jadi integer 
122.	Memanggil Fungsi Insert ke BST 
123.	Konfirmasi berhasil ditambahkan 
124.	Kalau input salah
125.	tampilkan error
126.	–
127.	Kalau pilih 2 (cari ruang lebih besar)
128.	Coba ambil input 
129.	Konversi jadi integer 
130.	Panggil find_successor 
131.	Kalau ketemu
132.	tampilkan hasilnya 
133.	Kalau tidak
134.	Mencetak tidak ada  ruang cadangan lebih besar
135.	Kalau input salah
136.	tampilkan error
137.	–
138.	Kalau pilih 3 (cari ruang lebih kecil)
139.	Coba ambil input 
140.	Konversi jadi integer 
141.	Panggil find_predecessor 
142.	Kalau ketemu
143.	tampilkan hasilnya 
144.	Kalau tidak
145.	Mencetak tidak ada ruang cadangan lebih kecil
146.	Kalau input salah
147.	tampilkan error
148.	–
149.	Kalau pilih 4 (hapus ruang penuh)
150.	Coba ambil input 
151.	Konversi jadi integer 
152.	Memanggil fungsi Hapus dari BST 
153.	Konfirmasi berhasil dihapus 
154.	Kalau input salah
155.	tampilkan error
156.	–
157.	Kalau pilih 5 (tampilkan semua)
158.	Print label "Daftar ruang ICU:" 
159.	Memanggil fungsi Traversal inorder (urut dari kecil ke besar)
160.	Print baris baru setelah selesai
161.	–
162.	Kalau pilih 6
163.	tampilkan "Program selesai."
164.	–
165.	Kalau input diluar 1-6
166.	tampilkan "Pilihan tidak valid!" 
167.	–
168.	Kalau file ini dijalankan langsung (bukan di-import)
169.	panggil fungsi main()

D. Output Program: 
<img width="1366" height="720" alt="Screenshot 2026-05-21 233223" src="https://github.com/user-attachments/assets/35d9c6c4-3c06-4be4-859c-60271638675b" />
<img width="1366" height="720" alt="Screenshot 2026-05-21 233248" src="https://github.com/user-attachments/assets/105f9dc5-7db3-4942-bd2e-ba4d757a3d59" />
<img width="1366" height="720" alt="Screenshot 2026-05-21 233259" src="https://github.com/user-attachments/assets/d54b2d03-c938-4435-b998-018c9ceb8211" />
<img width="1366" height="720" alt="Screenshot 2026-05-21 233316" src="https://github.com/user-attachments/assets/b50bbe79-431d-411f-b78f-fb1e6e1ebe20" />
Penjelasan output source code tersebut :  
Berdasarkan hasil percobaan, saya melakukan pengelolaan data ruang ICU menggunakan struktur Binary Search Tree (BST) dengan memasukkan delapan nomor ruang melalui Menu 1, yaitu 15, 42, 8, 27, 63, 11, 35, dan 50, yang berhasil tersimpan ke dalam sistem. Selanjutnya, pada Menu 2, program berhasil menemukan ruang cadangan yang lebih besar dari 42, yaitu 50 (successor), sedangkan pada Menu 3 ditemukan ruang cadangan yang lebih kecil dari 27, yaitu 15 (predecessor). Setelah itu, melalui Menu 4, saya menghapus ruang 15 sehingga sistem otomatis menyesuaikan susunan data agar tetap teratur. Pada Menu 5, seluruh data ruang yang tersisa ditampilkan secara urut, yaitu 8, 11, 27, 35, 42, 50, dan 63. Terakhir, Menu 6 digunakan untuk mengakhiri program. Dari hasil tersebut, BST membantu pengelolaan data menjadi lebih terstruktur karena proses pencarian, penghapusan, dan penyusunan data dapat dilakukan secara otomatis.

E. Link YouTube : https://youtu.be/8vry7x0kRp4?si=McQDXzv0qan7bGio


