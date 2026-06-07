class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return key % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\n- Daftar Playlist Lagu -")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"[{current.key} - {current.value}] -> ", end="")
                current = current.next
            print("NONE")

def main():
    playlist = HashMapSeparateChaining()
    playlist.insert(9, "Hati-Hati di Jalan")
    playlist.insert(21, "Sial")
    playlist.insert(76, "Komang")
    playlist.insert(6, "Monokrom")
    playlist.display()
    hasil = playlist.search(21)
    if hasil:
        print(f"\nLagu ditemukan : {hasil.value}")
    else:
        print("\nLagu tidak ditemukan")
    playlist.remove_key(21)
    print("\nSetelah lagu Sial dihapus:")
    playlist.display()

if __name__ == "__main__":
    main()