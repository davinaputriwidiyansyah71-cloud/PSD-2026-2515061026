# Pengurutan Data Harga Sayur Menggunakan Insertion Sort

def insertion_sort(arr, n): 
    for i in range(1, n): 
        temp = arr[i] 
        j = i - 1 
        while j >= 0 and arr[j][1] > temp[1]: 
            arr[j + 1] = arr[j] 
            j -= 1 
        arr[j + 1] = temp


def main(): 
    try: 
        n = int(input("Masukkan jumlah sayur: ")) 
    except ValueError: 
        print("Input tidak valid!") 
        return

    arr = [] 
    print("Masukkan nama dan harga sayur:") 

    for i in range(n): 
        while True: 
            try: 
                nilai = int(input(f"Harga sayur ke-{i+1}: ")) 
                arr.append((input(f"Nama sayur ke-{i+1}: "), nilai)) 
                break 
            except ValueError: 
                print("Input tidak valid, silakan masukkan angka!") 
                
    print(f"Harga sebelum diurutkan: {arr}") 
    insertion_sort(arr, n) 
    print("Harga setelah diurutkan (Insertion Sort):", end=" ") 
    for i in range(n): 
        print(arr[i], end=" ") 
    print() 


if __name__ == "__main__": 
    main()