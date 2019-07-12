import itertools
import time

class BruteForce:
    def __init__(self, limit=1000000, length=4):
        # Set a hard limit to number of tests
        self.limit = limit
        # Nowadays, passwords are at least 4 letters long, so start directly with 4 letter passwords
        self.length = length

    def create_combinations(self):
        self.alphabets = "abcdefghijklmnopqrstuvwxyz"
        self.numbers = "1234567890"
        self.special = "!@#$%^&*()"

        # I have used generators to make it memory efficient and to avoid unnecessary computation
        # Loop through all possibilities of letters of length = self.length (default 4)
        # Note: It won't generate a case of double letters. Example - Luffy won't be generated (double fs)
        possibilities_alpha = itertools.permutations(self.alphabets, self.length)
        for password in possibilities_alpha:
            yield password

        # Loop through all possibilities of numbers of length = self.length
        possibilities_num = itertools.permutations(self.numbers, self.length)
        for password in possibilities_num:
            yield password

    def crack(self, user_pass):

        counter = 0
        performance_data = dict()
        found = False

        start = time.time()
        guessed_pass = self.create_combinations()
        for guess in guessed_pass:
            guess_str = "".join(guess)
            print("Iteration: ", counter, " password generated:", guess_str)

            # Stopping condition (other than matched password)
            if counter > self.limit:
                print("Limit exhausted, password not found")
                break
            elif guess_str == user_pass:
                print("Password successfully cracked.")
                performance_data["Outcome"] = "Successful"
                performance_data["Iterations"] = counter
                performance_data["Password"] = guess_str
                found = True
                break

            counter += 1

        end = time.time()

        if not found:
            performance_data["Outcome"] = "Failed"
            performance_data["Iterations"] = counter
            performance_data["Password"] = "Not found"

        performance_data["Speed"] = end-start

        return performance_data


if __name__ == "__main__":
    bf =  BruteForce()
    bf.crack("lufy")