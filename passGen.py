from random import randint
import numpy as np

class passGen:
    def __init__(self):
        self.path =  './WordLists/'
        self.dictFile = 'allDictWords.txt'
        self.phraseFile = 'phrases.txt'
        self.fullDict = [word.strip() for word in open(self.path+self.dictFile)]
        self.fullPhrase = [phrase.strip() for phrase in open(self.path+self.phraseFile)]

    def human_pass(self):
        selected = self.fullPhrase[randint(0, len(self.fullPhrase))]
        final_pass = self.pass_improve(selected)
        return selected, final_pass

    def pass_improve(self, cur_pass):
        new_pass = []
        cur_len = len(cur_pass)
        counter = 0
        skip = False
        for character in cur_pass:

            if skip:
                skip = False
                continue

            elif counter < cur_len-2 and cur_pass[counter] == cur_pass[counter+1]:
                convert = np.random.choice([0, 1])  # Convert consecutive words to *
                if convert == 0:
                    new_pass.append("*")
                    new_pass.append("*")
                    skip = True
                else:
                    new_pass.append(character)

            elif character in ("l", "L", "i", "I"):
                convert = np.random.choice([0, 1], p=[0.7, 0.3])  # Convert to ! with a 70% chance
                if convert == 0:
                    new_pass.append("!")
                else:
                    new_pass.append(character)

            elif character in ("a", "A", "o", "O"):
                convert = np.random.choice([0, 1], p=[0.7, 0.3])  # Convert to @
                if convert == 0:
                    new_pass.append("@")
                else:
                    new_pass.append(character)

            elif character in ("s", "S"):
                convert = np.random.choice([0, 1], p=[0.7, 0.3])  # Convert to $
                if convert == 0:
                    new_pass.append("$")
                else:
                    new_pass.append(character)

            elif character in ("c", "C"):
                convert = np.random.choice([0, 1], p=[0.7, 0.3])  # Convert to $
                if convert == 0:
                    new_pass.append("(")
                else:
                    new_pass.append(character)
            elif character.isalpha():
                convert = np.random.choice([0, 1], p=[0.4, 0.6])  # Convert to upper case
                if convert == 0:
                    new_pass.append(character.upper())
                else:
                    new_pass.append(character)
            else:
                new_pass.append(str(character))

        appended_len = randint(2, 4)  # Append 2 to 4 numbers at end
        for _ in range(appended_len):
            new_pass.append(str(randint(0, 9)))

        if len(new_pass) < 8:
            rand_word = randint(0, len(self.fullDict))
            temp = "".join(new_pass)
            return temp + self.fullDict[rand_word]
        else:
            return "".join(new_pass)

    def random_pass(self, pass_len=8):
        # Different possibilities of characters for the random string
        print("Length", pass_len)
        letters = "abcdefghijklmnopqrstuvwxyz"
        letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "1234567890"
        special = "!@#$%^&*()"
        combined = [0, 1, 2, 3]  # Used numbers instead of actual data because it is faster
        combined_types = [letters, letters_upper, numbers, special]
        '''
        0 = letters
        1 = lettters_upper 
        2 = numbers 
        3 = special 
        '''

        # Probability of choosing either of those types
        probabilities = [0.4, 0.2, 0.2, 0.2]
        choices = np.random.choice(combined, pass_len, p=probabilities)

        final_pass = []

        # Now use choice to select the letter inside the chosen type
        for choice in choices:
            cur_length = len(combined_types[choice])-1
            index = randint(0, cur_length)
            final_pass.append(combined_types[choice][index])

        return "".join(final_pass)


if __name__ == "__main__":
    pg = passGen()
    final_pass = pg.pass_improve("weakpassword")
    print(final_pass)
    phrase, generated = pg.human_pass()
    print(generated)
