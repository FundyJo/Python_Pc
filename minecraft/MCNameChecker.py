import time
from itertools import product

from mojang import MojangAPI

def allwords(chars, length):
    for letters in product(chars, repeat=length):
        yield ''.join(letters)

words = []

def main():
    letters = "abcdefghijklmnopqrstuvwxyz"
    for wordlen in range(3, 4):
        for word in allwords(letters, wordlen):
            print(word)
            words.append(word)
    print(words)

    not_taken = []

    for name in words:
        time.sleep(2)
        uuid = MojangAPI.get_uuid(name)

        if not uuid:
            print(f"{name} is not taken.")
            not_taken.append(name)

        else:
            print(f"{name}'s UUID is {uuid}")

        for x in not_taken:
            file = open(f"../names.txt", "w")
            file.write(x)

    print(not_taken)

    input("Press Enter to close...")

if __name__=="__main__":
    main()
