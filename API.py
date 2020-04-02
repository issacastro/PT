import csv
import os
import sys
import datetime
import pandas as pd
from glob import glob
from os import system
from pydub import AudioSegment
from pydub.playback import play
from inaSpeechSegmenter import Segmenter

def getFolders(name):
    folders = []
    for x in glob(name):
        folders.append(x)
    return folders

def WriteResult(data,user):
    df = pd.DataFrame(data, columns = ['Audio','Genero','Edad','Region']) 
    dt = datetime.datetime.now()
    filename = user+'_Reporte_'+str(dt)
    df.to_csv(filename+'.csv', index = None, header=True)
    df.to_json(filename +'.json',orient='records')
    system("clear")
    print(df)

def Gender(folders,ext,seg):
    list_result = []
    for folder in folders:
        name = folder.split("/")[-1]
        audio = folder + "/individuales/" + name + "01"+ext
        result = seg(audio)
        list_result.append(result[0][0])
    return list_result

def Range_old(folders,ext):
    list_result = []
    for folder in folders:
        name = folder.split("/")[-1]
        audio = folder + "/comunes/" + name + "01"+ext
        sound = AudioSegment.from_wav(audio)
        system("clear")
        play(sound)
        print("Rango de edades")
        print("a) 19-21")
        print("b) 22-24")
        print("c) 25-28")
        print("d) 29-32")
        print("e) 33-36")
        print("f) 37-40")
        print("g) 41-44")
        print("h) 45-48")
        print("i) 49-51")
        edad = input("Ingrese rango:")
        list_result.append(edad)
    return list_result

def Reporte(folders,G,E,R):
    Rango = {"a": "19-21","b":"22-24","c":"25-28","d": "29-32",
        "e":"33-36","f":"37-40","g":"41-44","h":"45-48","i":"49-51","":"-"}
    Generos = {"male":"Hombre","female":"Mujer"}
    list_result = []
    i = 0 
    for folder in folders:
        name = folder.split("/")[-1]
        try:
            Genero = Generos[G[i]]
        except:
            Genero = '-'
        try:
            Edad = Rango[E[i]]
        except:
            Edad = '-'
        list_result.append([name,Genero,Edad,R])
        i = i + 1

    return list_result
def main():
    list_result = []
    seg = Segmenter(detect_gender= True)
    ext = "."+str(sys.argv[1])
    user =  str(sys.argv[2])
    Path = os.getcwd()+"/CorpusM/*"
    folders = getFolders(Path)
    folders = sorted(folders)
    Edades = Range_old(folders, ext)
    Generos = Gender(folders, ext,seg)
    data = Reporte(folders,Generos,Edades,'Mexico')
    WriteResult(data,user) 
       
main()