def sequential_search(data, n, target): 
    i = 0 
    counter = 0 
    first_index = -1 
    last_index = -1 
    while i < n: 
        if data[i] == target: 
            counter += 1 
            if first_index == -1: 
                first_index = i 
            last_index = i 
        i += 1 
    return counter, first_index, last_index 


def main(): 
    data = [210, 315, 210, 400, 210, 512, 315, 210, 200, 400, 512]     # Data kode buku yang dipinjam
    n = len(data) 
    print(f"Data peminjaman buku: {data}")
    while True: 
        try: 
            target = int(input("Masukkan kode buku yang dicari: ")) 
            break 
        except ValueError: 
            print("Input tidak valid, silakan masukkan angka!")
    counter, first_index, last_index = sequential_search(data, n, target) 
    if counter > 0: 
        print(
            f"Kode buku {target} dipinjam sebanyak {counter} kali, "
            f"pertama ditemukan pada indeks ke-{first_index} "
            f"dan terakhir ditemukan pada indeks ke-{last_index}."
        )
    else: 
        print(f"Kode buku {target} tidak ditemukan.")

if __name__ == "__main__": 
    main()