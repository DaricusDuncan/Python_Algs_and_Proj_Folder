import os
import subprocess

proc = subprocess.Popen("python test.py" ,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
dataBuff = proc.communicate()[0]

_IDFLAG = "NaN_"

grabIndex = dataBuff.find(_IDFLAG)
snipData = dataBuff[grabIndex:]
cleanSnippet = snipData.replace(_IDFLAG,'')
print(cleanSnippet)
