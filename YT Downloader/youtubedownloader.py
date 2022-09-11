from pytube import YouTube

link = input("Enter Youtube link: ")
yt = YouTube(link)

print("---------------------------------------------")
print(yt.title)
print("---------------------------------------------")
print(yt.author)
print("---------------------------------------------")
print(f"Views: {yt.views}")
print("---------------------------------------------")
print(yt.thumbnail_url)
print("---------------------------------------------")

ys = yt.streams.get_highest_resolution()
ys.download()
print("Download Completed!")
