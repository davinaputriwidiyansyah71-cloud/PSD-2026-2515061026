class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class BSTKlinik:
    def __init__(self):
        self.root=None 

    def insert_node(self,root,key):
        if root is None: 
            return Node(key) 
        if key<root.key: 
            root.left=self.insert_node(root.left,key) 
        elif key>root.key: 
            root.right=self.insert_node(root.right,key) 
        return root 

    def insert(self,key): 
        self.root=self.insert_node(self.root,key) 
        
    def find_min_node(self,root):
        current=root 
        while current is not None and current.left is not None: 
            current=current.left 
        return current 

    def inorder(self,root): 
        if root is None: 
            return 
        self.inorder(root.left) 
        print(root.key,end=" ") 
        self.inorder(root.right) 

    def delete_node(self,root,key): 
        if root is None:
            return None
        if key<root.key:
            root.left=self.delete_node(root.left,key) 
        elif key>root.key: 
            root.right=self.delete_node(root.right,key)
        else: 
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
