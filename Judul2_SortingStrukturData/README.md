A. Judul Program: Pengurutan Data Harga Sayur Menggunakan Insertion Sort

B. Deskripsi Singkat: Program ini dibuat menggunakan Python untuk mengurutkan harga sayur dengan metode Insertion Sort. User diminta memasukkan jumlah data, lalu menginput harga dan nama pada setiap sayur. Data tersebut disimpan dalam bentuk (nama dan harga), kemudian diurutkan berdasarkan harga dari yang paling murah ke yang paling mahal. Setelah itu, program akan menampilkan data sebelum dan sesudah diurutkan supaya bisa terlihat perbedaannya.

C. Source Code:
<img width="1366" height="720" alt="Screenshot 2026-05-02 215052" src="https://github.com/user-attachments/assets/6edbce99-9075-4ee0-b110-ba5b43b3cecc" />
<img width="1366" height="720" alt="Screenshot 2026-05-02 215103" src="https://github.com/user-attachments/assets/16b13f93-5976-4629-8009-86b180916d17" />
Penjelasan Kode Program Perbarisnya : 
1. Membuat fungsi namanya insertion_sort. Fungsi ini butuh dua bahan: arr sebagai list data sayurnya, dan n untuk berapa banyak sayurnya. 
2. Mulai cek dari sayur ke-2 (indeks 1) sampai habis. Kenapa dari ke-2? Karena sayur pertama dianggap sudah "aman" di posisinya, tidak perlu dibandingkan dengan yang lain dulu. 
3. Ambil sayur yang lagi dicek sekarang, taruh dulu di "tangan" (simpan ke temp). Ibarat kita cabut satu kartu dari tumpukan untuk dibandingkan.
4. Sekarang lirik ke kiri j menunjuk ke sayur tepat sebelumnya. Ini yang akan kita bandingkan dengan temp.
5. Selama masih ada elemen di kiri (j >= 0) dan harga elemen kiri lebih mahal dari yang di tangan (temp), berarti dia harus digeser. [1] artinya kita ambil bagian harga dari tuple (nama, harga).
6. Geser elemen yang lebih mahal tadi satu langkah ke kanan. Ibarat ngasih tempat 
7. Setelah geser, mundur lagi satu langkah ke kiri. Cek lagi apakah yang di kiri masih lebih mahal juga.
8. Setelah ketemu posisi yang pas (tidak ada lagi yang lebih mahal di kiri), taruh temp di sana. Sayur sudah masuk ke posisi yang benar.
9. -
10. -
11. Ini fungsi utamanya, tempat program berjalan dari awal sampai akhir.
12. Meminta input dari user, tapi belum tentu user memasukkan angka yang benar.
13. Meminta user berapa banyak sayur yang mau dimasukkan, lalu ubah ke angka bulat (integer).
14. Kalo ternyata user masukin huruf atau karakter aneh yang tidak bisa jadi angka, tangkap errornya.
15. Kasih tau user bahwa inputnya salah.
16. Langsung hentikan program karena tidak bisa lanjut kalau jumlah sayurnya tidak jelas.
17. -
18. Siapkan tempat kosong (list) untuk menampung semua data sayur yang akan dimasukkan.
19. Print instruksi ke user bahwa sekarang giliran input nama dan harga tiap sayur.
20. -
21. Lakukan pengulangan sebanyak n kali  satu putaran untuk satu sayur.
22. Looping terus sampai user berhasil input dengan benar. Kalau salah, akan diminta ulang, bukan langsung error lalu berhenti.
23. Mencoba lagi, antisipasi kalau user salah ketik harga.
24. Meminta user memasukan harga sayur ke sekian. i+1 supaya tampil dari angka 1, bukan 0. Hasilnya disimpan ke nilai.
25. Meminta input nama sayurnya, lalu gabungkan nama dan harga jadi satu pasangan (nama, harga) dan masukkan ke dalam list arr.
26. Kalau input nama dan harga berhasil semua, keluar dari while True. Lanjut ke sayur berikutnya.
27. Kalau harga yang diketik bukan angka (misal user ketik "dua ribu"), tangkap errornya.
28. Kasih peringatan, lalu while True akan mengulang permintaan input dari harga lagi.
29. -
30. Tampilkan semua data sayur sebelum diurutkan, biar user bisa lihat bedanya nanti setelah sorting.
31. Panggil fungsi yang tadi dibuat di atas jalankan proses pengurutan berdasarkan harga dari murah ke mahal.
32. Cetak label hasilnya. end=" " supaya teks berikutnya nyambung di baris yang sama, tidak turun baris.
33. Ulang sebanyak jumlah sayur untuk cetak satu per satu hasil urutan.
34. Cetak data sayur ke-i dalam bentuk (nama, harga), diikuti spasi. Semua tampil dalam satu baris.
35. Cetak baris kosong di akhir agar tampilan tidak "menempel" dengan teks lain di terminal.
36. -
37. -
38. Pengecekan: "Apakah file ini yang sedang dijalankan langsung?" Kalau iya, baru jalankan main(). Supaya kalau file ini dipakai sebagai modul oleh program lain, fungsi main() tidak ikut-ikutan jalan otomatis.
39. Jalankan semua! Di sinilah program benar-benar dimulai.

D. Output Program: 
<img width="1366" height="720" alt="Screenshot 2026-05-02 215551" src="https://github.com/user-attachments/assets/103c7b68-00af-4792-8408-0964c9b66cf2" />
Penjelasan output source code tersebut : 
Pertama user diminta memasukkan jumlah data sayur yang ingin di input. Pada contoh output, jumlah sayur yang dimasukkan adalah 5. Setelah itu, program meminta user memasukkan harga dan nama sayur satu per satu, mulai dari sayur ke-1 sampai sayur ke-5. 
Data yang diinput pada gambar yaitu:
Bayam dengan harga 5000, Brokoli dengan harga 15000, Wortel dengan harga 7000, Kentang dengan harga 9000, Selada dengan harga 12000

Setelah semua data selesai dimasukkan, program menampilkan bagian “Harga sebelum diurutkan”. Pada bagian ini, data masih sesuai urutan awal saat user menginput data. Jadi belum ada proses sorting.

Selanjutnya, program menjalankan algoritma Insertion Sort untuk mengurutkan data berdasarkan harga dari yang paling murah ke paling mahal. Cara kerjanya yaitu program membandingkan setiap harga dan menyisipkannya ke posisi yang sesuai sampai seluruh data tersusun rapi. 

Hasil akhirnya ditampilkan pada bagian “Harga setelah diurutkan (Insertion Sort)”. Dari output terlihat data sudah berubah urutannya menjadi:
Bayam (5000), Wortel (7000), Kentang (9000), Selada (12000), Brokoli (15000)

Program berhasil mengurutkan harga sayur secara ascending atau dari nilai terkecil ke terbesar.

E. Link YouTube: 
https://youtu.be/yzkdFpOijH8?si=fU0f_yzigYVJmCtk
