from __future__ import unicode_literals
import youtube_dl

filename = 'Audio'
ext = 'wav'
#destination = 'CorpusA/'
destination =''
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': ext,
        'preferredquality': '192',
    }],
    'outtmpl':destination+filename+'.'+ext,
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=XHIg6nki52Q'])