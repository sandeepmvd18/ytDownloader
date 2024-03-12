from pytube import YouTube
from sys import argv 

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

stream = yt.streams.get_highest_resolution()
stream.download('/mnt/c/Users/sandy/Documents/TechVideos')