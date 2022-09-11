from mojang import MojangAPI

username = str(input("Username: "))
uuid = MojangAPI.get_uuid(username)

if not uuid:
    print(f"{username} is not taken.")
else:
    print(f"{username}'s UUID is {uuid}")

    profile = MojangAPI.get_profile(uuid)
    print(f"{username}'s skin URL is {profile.skin_url}")
    print(f"{username}'s skin model is {profile.skin_model}")
    print(f"{username}'s cape URL is {profile.cape_url}")
