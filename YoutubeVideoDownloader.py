from pytube import YouTube

link = input("please input the youtube video link to download")

# //getting the details of the video

yt = YouTube(link)

# title of the video
print("title:", yt.title)

#views for the video
print("views:", yt.views)

#length of the video
print("lenght : ", yt.length)

#description of the video
print("description: ", yt.description)

#rating
print("rating :", yt.rating)

# streams
# print("streams:", yt.streams)

# filter only audio streams
# print("audio streams", yt.streams.filter(only_audio=True))

# filter only video streams
# print("video streams", yt.streams.filter(only_video=True))

# progressive streams and dash streams
# progressive streams are limited 720 -and contain video and audio both
# while dash streams are used for highest quality rendering - only video and audio need merge using tool

# filter only progressive streams
print("progressive streams:", yt.streams.filter(progressive=True))

# getting highest resolution stream
ys = yt.streams.get_highest_resolution()

print("highest resolution: ", ys)

#we can get using itag also
# ym = yt.streams.get_by_itag('22')

# download to default location else give location
print("downloading......")
ys.download()
print("download completed")