#Para correc el prgograma python Download.py DIRECTORIO_DESTINO
# python Download.py Pruebas/
from __future__ import unicode_literals
import youtube_dl
import ffmpy
import os
import sys
import pandas as pd

def ConvertWav_Completo(path):
    i=1
    for filename in os.listdir(path):
        if(filename.endswith('.mp3')):
            os.system(f"""ffmpeg -i {path+filename} -ss 00 -to 05 -acodec pcm_s16le -ar 16000 {path+filename[:-4]}.wav""")
            i=i+1
            os.remove(path+filename)
def ConvertWav(path,startA,endA,ext):
    i=1
    for filename in os.listdir(path):
        if(filename.endswith(ext)):
            os.system(f"""ffmpeg -i {path+filename} -ss {startA} -to {endA} -acodec pcm_s16le -ar 16000 {path+filename[:-4]}.wav""")
            i=i+1
            os.remove(path+filename)

def Download(filename,link,destination):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl':destination+filename+'.mp3',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

#destination = 'CorpusA/'
def main():
    destination  =  str(sys.argv[1])
    data = pd.read_csv("Data_Download.csv") 

    for index, row in data.iterrows():
        print(row['Nombre'], row['Link'])
        Download(row['Nombre'],row['Link'],destination)

    ConvertWav(destination,'00','10','.mp3')

main()

