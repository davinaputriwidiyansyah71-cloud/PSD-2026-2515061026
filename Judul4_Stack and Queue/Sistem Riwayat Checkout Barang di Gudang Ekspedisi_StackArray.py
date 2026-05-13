class StackArray: # code ini sebagai implementasi stack menggunakan array untuk mengelola barang di gudang ekspedisi
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, barang):
        if self.is_full():
            print("Rak gudang penuh!")
            return
        self.top_idx += 1
        self.st[self.top_idx] = barang
        print(f"Barang '{barang}' berhasil ditambahkan")

    def pop(self):
        if self.is_empty():
            print("Tidak ada barang di rak")
            return
        print(f"Barang '{self.st[self.top_idx]}' berhasil checkout")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Rak kosong")
            return
        print(f"Barang paling atas: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Rak kosong")
            return
        print("\nIsi rak gudang:")
        for i in range(self.top_idx, -1, -1):
            print(f"- {self.st[i]}")

    def count(self):
        print(f"Total barang dalam rak: {self.top_idx + 1}")
    def clear(self):
        self.top_idx = -1
        print("Semua barang berhasil dikosongkan")


def main():
    stack = StackArray()
    pilih = 0
    while pilih != 7:
        print("\n=== GUDANG EKSPEDISI ===")
        print("1. Tambah Barang")
        print("2. Checkout Barang")
        print("3. Lihat Barang Teratas")
        print("4. Tampilkan Semua Barang")
        print("5. Hitung Total Barang")
        print("6. Kosongkan Rak")
        print("7. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue
        if pilih == 1:
            barang = input("Masukkan nama barang: ")
            stack.push(barang)
        elif pilih == 2:
            stack.pop()
        elif pilih == 3:
            stack.peek()
        elif pilih == 4:
            stack.display()
        elif pilih == 5:
            stack.count()
        elif pilih == 6:
            stack.clear()
        elif pilih == 7:
            print("Program selesai")
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()