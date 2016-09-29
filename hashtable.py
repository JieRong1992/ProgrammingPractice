class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _get_hash(self, key):
        hash = 0
        for letter in str(key):
            hash += ord(letter)
        return hash % self.size

    def insert(self, key):
        key_hash = self._get_hash(key)
        if key not in self.table[key_hash]:
            self.table[key_hash].append(key)
            print('insert', key, 'at',key_hash)
            return True
        else:
            print('already exist')
            return False

    def delete(self,key):
        key_hash = self._get_hash(key)
        if key not in self.table[key_hash]:
            print('not exist')
            return False
        else:
            self.table[key_hash].remove(key)
            print('delete', key, 'at', key_hash)
            return True
    def get_key(self,key):
        key_hash = self._get_hash(key)
        if key in self.table[key_hash]:
            print('find', key, 'at', key_hash)
            return True
        print('didn\'t find',key)
        return False
