# Import Tkinter for GUI
import tkinter
from tkinter import filedialog
# Import the custom-built libraries
import bruteForce
import dictionaryAttack
import md5Cracker
import passGen


def run_brute():
    test_pass = password_field.get()
    length = length_field.get()
    iterations = total_iterations.get()
    assert test_pass, "Empty test password field"    # To ensure that user has entered the password
    # Length is optional, so if provided pass it to the function, else call directly
    print(length)
    if length:
        if iterations:
            bf = bruteForce.BruteForce(length=int(length), limit=int(iterations))
        else:
            bf = bruteForce.BruteForce(length=int(length))
    else:
        if iterations:
            bf = bruteForce.BruteForce(limit=int(iterations))
        else:
            bf = bruteForce.BruteForce()
    performance_data = bf.crack(test_pass)

    # Insert the performance data onto the text window
    text_field.insert(tkinter.END, "\nPerformance Data for Brute Forcing:\n")
    for k, v in performance_data.items():
        output = str(k) + ":\t" + str(v) + "\n"
        text_field.insert(tkinter.END, output)


def run_dictionary():
    test_pass = password_field.get()

    assert test_pass, "Empty test password field"    # To ensure that user has entered the password
    da = dictionaryAttack.DictionaryCrack()
    performance_data = da.start_attack(test_pass)

    # Insert the performance data onto the text window
    text_field.insert(tkinter.END, "\nPerformance Data for Dictionary Attack:\n")
    for k, v in performance_data.items():
        output = str(k) + ":\t" + str(v) + "\n"
        text_field.insert(tkinter.END, output)


def run_md5():
    # Ask user to select the md5 file
    file = filedialog.askopenfile(parent=window, mode='rb', title='Choose file containing MD5 hashes')
    md = md5Cracker.Md5Cracker()
    performance_data = md.collision_attack(file.name)

    text_field.insert(tkinter.END, "\nPerformance Data for MD5 Attack:\n")

    for k, v in performance_data.items():
        if isinstance(v, dict):
            text_field.insert("Cracked hashes: \n")
            for k2, v2 in v.items():
                output = str(k2) + ":  " + str(v2) + "\n"
                text_field.insert(output)
        else:
            output = str(k) + ":\t" + str(v) + "\n"
            text_field.insert(tkinter.END, output)


def run_ran_pass():
    length = length_field.get()

    assert length, "Enter length of password"
    rp = passGen.passGen()
    generated = rp.random_pass(pass_len=int(length))
    output = "\n Generated password: " + generated + "\n"
    text_field.insert(tkinter.END, output)

def run_improve_pass():
    cur_pass = password_field.get()

    assert cur_pass, "No password entered"
    ip = passGen.passGen()
    improved = ip.pass_improve(cur_pass)
    output = "\nEntered password: " + cur_pass + "\n" + "Improved password: " + improved + "\n"
    text_field.insert(tkinter.END, output)

def run_human_pass():
    hp = passGen.passGen()
    phrase, gen_pass = hp.human_pass()
    output = "\nPhrase to remember: " + phrase + "\nPassword generated: " + gen_pass + "\n"
    text_field.insert(tkinter.END, output)


# Initialize the window
window = tkinter.Tk()
window.title("Password Cracking Suite")

# Create the layout
leftFrame = tkinter.Frame(window)
bottomFrame = tkinter.Frame(window)
rightFrame = tkinter.Frame(window)

leftFrame.pack(side=tkinter.LEFT)
bottomFrame.pack(side=tkinter.BOTTOM)
rightFrame.pack(side=tkinter.RIGHT)

# Create a scroll bar
scrollbar = tkinter.Scrollbar(rightFrame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# Create labels and test password entry
instruction = tkinter.Label(leftFrame, text="Enter test password:")
password_field = tkinter.Entry(leftFrame)
instruction.grid(row=0, column=0)
password_field.grid(row=0, column=1)

pass_length = tkinter.Label(leftFrame, text="Enter password length (default=4)")
length_field = tkinter.Entry(leftFrame)
pass_length.grid(row=1, column=0)
length_field.grid(row=1, column=1)

iterate_label = tkinter.Label(leftFrame, text="Total iterations: (default 1 million)")
total_iterations = tkinter.Entry(leftFrame)
iterate_label.grid(row=2, column=0)
total_iterations.grid(row=2, column=1)

# Create the dynamic field
text_field = tkinter.Text(rightFrame, height=20, width=70, yscrollcommand=scrollbar.set)
text_field.pack(side=tkinter.RIGHT)

# Create brute buttons
bruteButton = tkinter.Button(bottomFrame, text="Brute Force", command=run_brute)
dictButton = tkinter.Button(bottomFrame, text="Dictionary Attack", command=run_dictionary)
mdButton = tkinter.Button(bottomFrame, text="MD5 Cracker", command=run_md5)
exitButton = tkinter.Button(bottomFrame, text="Exit", command=window.destroy)
ranButton = tkinter.Button(bottomFrame, text="Gen. Random Password", command=run_ran_pass)
improveButton = tkinter.Button(bottomFrame, text="Improve Password", command=run_improve_pass)
humanButton = tkinter.Button(bottomFrame, text="Gen. human Password", command=run_human_pass)

bruteButton.pack(side=tkinter.LEFT)
dictButton.pack(side=tkinter.LEFT)
mdButton.pack(side=tkinter.LEFT)
ranButton.pack(side=tkinter.LEFT)
improveButton.pack(side=tkinter.LEFT)
humanButton.pack(side=tkinter.LEFT)
exitButton.pack(side=tkinter.RIGHT)


window.mainloop()
