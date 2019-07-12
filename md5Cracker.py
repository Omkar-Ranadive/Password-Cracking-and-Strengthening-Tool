import os
import hashlib
import time


class Md5Cracker:
    def __init__(self):
        self.path = './WordLists/'
        self.passwords = []
        self.md5 = hashlib.md5

        for file in os.listdir(self.path):
            cur_file = [word.strip() for word in open(self.path + file)]
            # We take passwords from all word lists and merge them into a single big list
            self.passwords.extend(cur_file)

    def make_rainbow_table(self):
        rainbow_t = dict()
        for guess in self.passwords:
            m = hashlib.md5()
            m.update(guess.encode('utf-8'))  # utf-8 encoding is required
            hashed = (m.digest()).hex()  # encode in hex to get rid of '\x'
            # We need setdefault because multiple passwords can map to same hash (collision)
            rainbow_t.setdefault(hashed, [])
            rainbow_t[hashed].append(guess)

        return rainbow_t

    def collision_attack(self, file_path):

        performance_data = dict()
        start = time.time()
        # Create rainbow table
        rainbow_table = self.make_rainbow_table()

        # Load up a file
        loaded_hashes = [h.strip() for h in open(file_path)]

        cracked_hashes = []

        for h in loaded_hashes:
            if h in rainbow_table:
                cracked_hashes.append((h, rainbow_table[h]))

        end = time.time()
        performance_data["Speed"] = end-start
        performance_data["Hashes"] = cracked_hashes
        print("Cracked hashes are: ")
        print(cracked_hashes)

        return performance_data


if __name__ == "__main__":
    md = Md5Cracker()
    md.collision_attack('./WordLists/md5Data.txt')

