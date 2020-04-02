import shutil 
for i in range(10,100):
    dst="/home/issa/Documentos/Python/CorpusM/s0"+str(i)
    src="/home/issa/Documentos/CorpusDimex100/s0"+str(i)+"/audio_editado"
    shutil.copytree(src, dst)