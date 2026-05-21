class Node:
    def __init__(self,key):
        self.key=key
        self.left=None # untuk me
        self.right=None

class BSTKlinik:
    def __init__(self):
        self.root=None # root dari pohon yang mana kosong pada awalnya

    def insert_node(self,root,key):
        if root is None: # jika root kosong, buat node baru dengan key yang diberikan
            return Node(key) # mengembalikan node baru sebagai root
        if key<root.key: # jika key yang akan dimasukkan lebih kecil dari key root, masukkan ke subtree kiri
            root.left=self.insert_node(root.left,key) # rekursif memanggil insert_node pada subtree kiri dan mengupdate root.left dengan hasilnya
        elif key>root.key: # jika key yang akan dimasukkan lebih besar dari key root, masukkan ke subtree kanan
            root.right=self.insert_node(root.right,key) # rekursif memanggil insert_node pada subtree kanan dan mengupdate root.right dengan hasilnya
        return root # mengembalikan root yang sudah diperbarui setelah penambahan node baru

    def insert(self,key): # fungsi untuk menambahkan node baru dengan key yang diberikan ke dalam pohon
        self.root=self.insert_node(self.root,key) # memanggil insert_node dengan root saat ini dan key yang akan dimasukkan, lalu mengupdate root dengan hasilnya

    def find_min_node(self,root):
        current=root 
        while current is not None and current.left is not None: # selama current tidak kosong dan masih memiliki anak kiri, terus bergerak ke kiri
            current=current.left # update current ke anak kiri
        return current 

    def inorder(self,root): 
        if root is None: # jika root kosong, tidak ada yang perlu ditampilkan
            return 
        self.inorder(root.left) # memanggil inorder pada subtree kiri
        print(root.key,end=" ") # menampilkan key dari node saat ini
        self.inorder(root.right) # memanggil inorder pada subtree kanan

    def delete_node(self,root,key): 
        if root is None:
            return None
        if key<root.key: # jika key yang akan dihapus lebih kecil dari key root, cari di subtree kiri
            root.left=self.delete_node(root.left,key) 
        elif key>root.key: # jika key yang akan dihapus lebih besar dari key root, cari di subtree kanan
            root.right=self.delete_node(root.right,key)
        else: # jika key ditemukan
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor=self.find_min_node(root.right)
                root.key=successor.key
                root.right=self.delete_node(root.right,successor.key)
        return root #

    def delete(self,key):
        self.root=self.delete_node(self.root,key)

    def find_successor(self,root,key):
        current=root 
        successor=None 
        while current is not None: 
            if key<current.key:
                successor=current
                current=current.left 
            elif key>current.key: 
                current=current.right 
                break
        if current is None:
            return None,False
        if current.right is not None: 
            successor=self.find_min_node(current.right) 
        if successor is None: 
            return None,False
        return successor.key,True 

    def find_predecessor(self,root,key):
        current=root
        predecessor=None 
        while current is not None:
            if key>current.key:
                predecessor=current
                current=current.right
            elif key<current.key:
                current=current.left
            else:
                break
        if current is None:
            return None,False
        if current.left is not None:
            temp=current.left 
            while temp.right is not None:
                temp=temp.right 
            predecessor=temp
        if predecessor is None:
            return None,False
        return predecessor.key,True

def main():
    bst=BSTKlinik()
    pilih=0
    while pilih!=6:
        print("--- SISTEM RUANG ICU KLINIK ---")
        print("1.Tambah ruang ICU")
        print("2.Cari ruang cadangan lebih besar")
        print("3.Cari ruang cadangan lebih kecil")
        print("4.Hapus ruang penuh")
        print("5.Tampilkan semua ruang")
        print("6.Keluar")
        try:
            pilih=int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih==1:
            try:
                x=int(input("Masukkan nomor ruang ICU: "))
                bst.insert(x)
                print(f"Ruang ICU {x} berhasil ditambahkan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih==2:
            try:
                x=int(input("Cari ruang lebih besar dari: "))
                ans,found=bst.find_successor(bst.root,x)
                if found:
                    print(f"Ruang cadangan terdekat: {ans}")
                else:
                    print("Tidak ada ruang cadangan lebih besar")
            except ValueError:
                print("Input tidak valid!")

        elif pilih==3:
            try:
                x=int(input("Cari ruang lebih kecil dari: "))
                ans,found=bst.find_predecessor(bst.root,x)
                if found:
                    print(f"Ruang cadangan terdekat: {ans}")
                else:
                    print("Tidak ada ruang cadangan lebih kecil")
            except ValueError:
                print("Input tidak valid!")

        elif pilih==4:
            try:
                x=int(input("Masukkan ruang penuh: "))
                bst.delete(x)
                print(f"Ruang ICU {x} berhasil dihapus")
            except ValueError:
                print("Input tidak valid!")

        elif pilih==5:
            print("Daftar ruang ICU: ",end="")
            bst.inorder(bst.root)
            print()

        elif pilih==6:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__=="__main__":
    main()