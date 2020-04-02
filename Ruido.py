from inaSpeechSegmenter import Segmenter
def main():
    audio = 'Audio.wav'
    seg = Segmenter(vad_engine = 'smn' )
    result = seg(audio)
    print(result)
       
main()