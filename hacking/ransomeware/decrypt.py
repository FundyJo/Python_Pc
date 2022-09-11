import base64
import os

from cryptography.fernet import Fernet

files = []
input_key = input("Key: ")

input_key = bytes(input_key, "utf-8")
key = base64.b64encode(input_key)

##with open("key.key", "rb") as thefile:
    ##key = thefile.read()


print(type(key))


def fill_list(directory):
    for file in os.listdir(directory):
        if os.path.isfile(directory + "/" + file):
            print(f'Detected file: "{directory}/{file}"')
            files.append(directory + "/" + file)
            continue
        fill_list(directory + "/" + file)


for file in os.listdir():
    if file == "ransomeware.py" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        print(f'Detected file: "{file}"')
        files.append(file)
        continue
    fill_list(file)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
