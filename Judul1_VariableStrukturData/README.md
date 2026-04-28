A. Judul Program: Program Pengolahan Nilai Siswa Menggunakan List 2D

B. Deskripsi Singkat: Program ini dibuat untuk mengelola data nilai siswa dengan menggunakan struktur data List 2D di Python. Data disusun seperti tabel, yang dimana baris menunjukkan siswa dan kolom menunjukkan mata pelajaran, yaitu Matematika dan Sejarah. Di dalam program ini ada beberapa menu, yaitu menampilkan alamat memori array, menginput nilai siswa, menampilkan semua data nilai, dan juga mengecek nilai tertentu berdasarkan indeks yang dipilih. 

C.Source Code: 
<img width="1366" height="720" alt="Screenshot 2026-04-28 115534" src="https://github.com/user-attachments/assets/c5635381-0002-4f27-a213-a5609e1e61e2" />
<img width="1366" height="720" alt="Screenshot 2026-04-28 115547" src="https://github.com/user-attachments/assets/7c252aa8-b421-47aa-b172-d4a2b00b4d21" />
<img width="1366" height="720" alt="Screenshot 2026-04-28 115556" src="https://github.com/user-attachments/assets/2deaadcd-b9e2-4725-8982-3e09d8924f4b" />
Penjelasan Kode Program Perbarisnya : 
1. Mendefinisikan fungsi bernama menu() yang berisi semua opsi pilihan yang akan ditampilkan ke pengguna
2. Mencetak pilihan 1: menampilkan alamat memori (id) dari seluruh array nilai
3. Mencetak pilihan 2: menampilkan  alamat memori dari setiap elemen individu di dalam array
4. Mencetak pilihan 3: meminta pengguna memasukkan nilai untuk setiap siswa dan mata pelajaran.
5. Mencetak pilihan 4: menampilkan seluruh data nilai yang telah diinput
6. Mencetak pilihan 5: mengecek nilai siswa tertentu berdasarkan baris (siswa) dan kolom (mapel).
7. Mencetak pilihan 6: keluar dari program / menghentikan loop utama.
8. -
9. -
10. Mendefinisikan fungsi utama main() yang menjadi inti jalannya program.
11. Komentar yang menjelaskan ukuran array: 3 baris (siswa) dan 2 kolom (mata pelajaran).
12. Membuat matriks 2D (3x2) menggunakan list, semua diinisialisasi dengan nilai 0. Ini adalah struktur data array 2 dimensi.
13. Selama True, program terus berjalan
14. -
15. Memulai loop utama program. Loop akan terus berulang selama variabel running bernilai True.
16. Memanggil fungsi menu() untuk menampilkan daftar pilihan kepada pengguna di setiap iterasi loop.
17. Mulai menggunakan blok try untuk mengantisipasi kemungkinan error ketika pengguna memasukkan input yang tidak sesuai atau tidak valid.
18. Meminta input dari pengguna dan mengkonversinya ke integer. Jika bukan angka, akan memicu ValueError.
19. Menangkap error jika pengguna memasukkan bukan angka (huruf atau simbol)
20. Menampilkan pesan error ke pengguna agar memasukkan angka yang benar.
21. Langsung kembali ke awal loop (melewatkan sisa kode di bawahnya), menampilkan menu lagi.
22. -
23. Kondisi: jika pengguna memilih angka 1, jalankan blok di bawahnya.
24. Menampilkan alamat memori dari objek list 'nilai' menggunakan fungsi id().
25. -
26. Kondisi alternatif: jika pengguna memilih angka 2, jalankan blok di bawahnya.
27. Loop untuk iterasi 3 baris (mewakili setiap siswa, indeks 0 sampai 2).
28. Loop bersarang untuk iterasi 2 kolom (mewakili setiap mata pelajaran, indeks 0 dan 1).
29. Mencetak alamat memori dari setiap elemen nilai[i][j] menggunakan id(). 
30. -
31. Kondisi alternatif: jika pengguna memilih angka 3 (input nilai siswa).
32. Mencetak petunjuk bahwa pengguna akan memasukkan nilai Matematika dan Sejarah.
33. Loop untuk setiap siswa (3 siswa total, indeks 0–2).
34. Mencetak informasi siswa yang sedang di input (misalnya: Siswa ke-0, Siswa ke-1, dst)
35. Loop bersarang untuk setiap mata pelajaran (2 mapel, indeks 0 dan 1), karena selalu di mulai dengan angka 0.
36. Loop tak terhingga untuk memastikan pengguna memasukkan nilai yang valid sebelum lanjut.
37. Blok try untuk menangkap error konversi integer saat input nilai.
38. Meminta input nilai dari pengguna dan menyimpannya ke elemen array nilai[i][j] setelah dikonversi ke integer.
39. Jika input berhasil dikonversi, keluar dari loop while dan lanjut ke mapel/siswa berikutnya
40. jika input bukan angka (misalnya huruf), tangkap error ini.
41. Tampilkan pesan error dan ulangi permintaan input (loop while kembali dari atas).
42. -
43. Kondisi alternatif: jika pengguna memilih angka 4 (tampilkan semua nilai).
44. Mencetak header/judul sebelum menampilkan data nilai semua siswa.
45. Loop untuk iterasi semua 3 siswa.
46. Mencetak baris nilai untuk siswa ke-i, menampilkan seluruh list nilai[i] (berisi 2 nilai mapel).
47. -
48. Kondisi alternatif: jika pengguna memilih angka 5 (cek nilai tertentu).
49. Blok try untuk menangani error input maupun akses elemen di luar batas array.
50. Meminta input indeks baris (siswa ke berapa) dan mengonversinya ke integer.
51. Meminta input indeks kolom (mata pelajaran ke berapa) dan mengonversinya ke integer.
52. Mengakses dan mencetak nilai pada posisi nilai[baris][kolom] sesuai input pengguna.
53. Menangkap dua jenis error: ValueError (input bukan angka) dan IndexError (indeks melebihi batas array 3x2).
54. Menampilkan pesan error jika terjadi salah satu dari kedua kondisi error di atas.
55. -
56. Kondisi alternatif: jika pengguna memilih angka 6 (keluar).
57. Mengubah nilai variabel running menjadi False, sehingga kondisi while tidak terpenuhi dan loop berhenti.
58. Mencetak pesan konfirmasi bahwa program telah selesai berjalan.
59. -
60. Kondisi fallback: jika pengguna memasukkan angka selain 1–6
61. Mencetak pesan bahwa pilihan yang dimasukkan tidak tersedia, lalu loop kembali ke atas.
62. -
63. -
64. Blok ini hanya dieksekusi jika file dijalankan langsung (bukan diimpor sebagai modul).
65. Memanggil fungsi main() untuk memulai eksekusi program secara keseluruhan.


D. Output Program: 
<img width="1366" height="720" alt="Screenshot 2026-04-28 121347" src="https://github.com/user-attachments/assets/6a961602-fd07-40ff-901d-a9538c18c657" />
<img width="1366" height="720" alt="Screenshot 2026-04-28 121400" src="https://github.com/user-attachments/assets/553ff3d2-7462-44be-b7e4-87b6d6ab398f" />

Penjelasan output source code tersebut : 

Menu 1 (Tampilkan address array nilai)
Saat memilih menu 1, program menampilkan alamat memori dari array nilai pertama kali jika di pilih

Menu 2 (Tampilkan address tiap nilai)
Program menampilkan alamat memori untuk setiap elemen dalam array (misalnya nilai[0][0], nilai[0][1], dst).

Menu 3 (Input nilai siswa)
User diminta memasukkan nilai untuk beberapa siswa dan mata pelajaran (Matematika & Sejarah).
Siswa 0 >  [67, 56],Siswa 1 > [89, 90], Siswa 2 > [88, 70]. Program berhasil menerima input user dan menyimpannya ke dalam array 2 dimensi sesuai indeks siswa dan mata pelajaran.

Menu 4 (Tampilkan semua nilai)
Program menampilkan seluruh data yang sudah diinput dalam bentuk list per siswa, data yang sebelumnya diinput tersimpan dengan benar dan bisa ditampilkan kembali secara terstruktur.

Menu 5 (Cek nilai tertentu)
User memilih indeks siswa dan mata pelajaran, lalu program menampilkan nilai spesifik.
Siswa ke-1, mapel ke-1 > nilai = 90, program dapat mengakses elemen tertentu dalam array menggunakan indeks dengan benar.

Menu 6 (Keluar)
Program menampilkan pesan “Program selesai.” lalu berhenti.


E. Link YouTube: 












