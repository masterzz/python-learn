from pytube import YouTube
YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=g9qPe5DWjds')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()\
    .first()\
    .download(output_path="D:\download\yt")