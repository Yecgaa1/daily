from pytube import YouTube
yt=YouTube('https://www.youtube.com/watch?v=N5nKlyxnGGc')
print(yt.streams.all())