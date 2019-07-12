import os
import time


class DictionaryCrack:
    def __init__(self):
        self.path = './WordLists/'
        self.passwords = []

        for file in os.listdir(self.path):
            cur_file = [word.strip() for word in open(self.path+file)]
            # We take passwords from all word lists and merge them into a single big list
            self.passwords.extend(cur_file)

        print("Total passwords in dictionary: ", len(self.passwords))

    def start_attack(self, user_pass):
        counter = 0
        notFound = True
        performance_data = dict()
        start = time.time()

        for guess in self.passwords:
            print("Iteration: ", counter, " password generated: ", guess)
            if guess == user_pass:
                notFound = False
                print("Password cracked successfully.")
                performance_data["Outcome"] = "Successful"
                performance_data["Iterations"] = counter
                performance_data["Password"] = guess
                break
            counter += 1

        end = time.time()
        performance_data["Speed"] = end-start
        if notFound:
            performance_data["Outcome"] = "Failed"
            performance_data["Iterations"] = counter
            performance_data["Password"] = "Not found"
            print("Password not found in the dictionary. Attack failed.")

        return performance_data


if __name__ == "__main__":
    da = DictionaryCrack()

    da.start_attack("abcd123")
