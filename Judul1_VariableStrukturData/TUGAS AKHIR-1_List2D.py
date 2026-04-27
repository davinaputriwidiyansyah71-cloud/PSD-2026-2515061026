def menu():
    print("1. Tampilkan address array nilai")
    print("2. Tampilkan address tiap nilai")
    print("3. Input nilai siswa")
    print("4. Tampilkan semua nilai")
    print("5. Cek nilai tertentu")
    print("6. Keluar")


def main():
    # 3 siswa, 2 mata pelajaran
    nilai = [[0 for _ in range(2)] for _ in range(3)]
    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print(f"Address array nilai: {id(nilai)}")

        elif choice == 2:
            for i in range(3):
                for j in range(2):
                    print(f"Address nilai[{i}][{j}]: {id(nilai[i][j])}")

        elif choice == 3:
            print("Input nilai siswa (Matematika & Sejarah)")
            for i in range(3):
                print(f"Siswa ke-{i}")
                for j in range(2):
                    while True:
                        try:
                            nilai[i][j] = int(input(f"Nilai mapel ke-{j}: "))
                            break
                        except ValueError:
                            print("Input tidak valid!")

        elif choice == 4:
            print("Data Nilai Siswa:")
            for i in range(3):
                print(f"Siswa {i}: {nilai[i]}")

        elif choice == 5:
            try:
                baris = int(input("Masukkan siswa ke-: "))
                kolom = int(input("Masukkan mapel ke-: "))
                print(f"Nilai siswa {baris} mapel {kolom} = {nilai[baris][kolom]}")
            except (ValueError, IndexError):
                print("Input tidak valid atau di luar batas!")

        elif choice == 6:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()