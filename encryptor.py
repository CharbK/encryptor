import random
import pyperclip

ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,!?;:-\'"()/-_=+  '

class bcolors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

def encrypt(string, key=0):
    result = 0
    for i in range(len(string)):
        # print(len(string) - (i + 1))
        temp = (ALPHABET.index(string[i]) + 1) * (len(ALPHABET)**(len(string) - (i + 1)))
        # print(temp)
        result += temp

    pyperclip.copy(str(result + key))
    return str(result + key)

def decrypt(string, key=0):
    string = int(string) - key
    res = ""
    num = string
    while num != 0:
        res += ALPHABET[(num % len(ALPHABET)) - 1]
        num //= len(ALPHABET)

    pyperclip.copy(res[::-1])
    return res[::-1]

def test():
    string = ""
    for i in range(random.randint(3,3)): string += ALPHABET[random.randint(0, len(ALPHABET) - 1)]

    if string != decrypt(encrypt(string)):
        print("New bug found. Please send these characters to Charbel:")
        print("    " + string)
        print("    " + encrypt(string))
        print("    " + decrypt(encrypt(string)))

def find_accuracy():
    amount_done = 0
    amount_correct = 0

    for i in range(20000):
        amount_done += 1

        string = ""
        for i in range(random.randint(200,300)):
            string += ALPHABET[random.randint(0, len(ALPHABET) - 1)]

        if string == decrypt(encrypt(string)):
            amount_correct += 1
        else:
            print(string)

    print(f"Accuracy: {(amount_correct/amount_done) * 100}%")


def main():

    key = input(f"{bcolors.YELLOW}KEY - ")
    try:
        key = int(key)
    except:
        print(f"{bcolors.FAIL}Invalid input")
        quit()
    act = input(f"{bcolors.CYAN}'e'ncrypt/'d'ecrypt - ")

    if act == "e":
        print("Result: " + encrypt(input(f"{bcolors.GREEN}--> "), key))
    elif act == "d":
        print("Result: " + decrypt(input(f"{bcolors.GREEN}--> "), key))
    else:
        print(f"{bcolors.FAIL}Invalid input")
        quit()

if __name__ == "__main__":
    #find_accuracy()
    test()
    main()
