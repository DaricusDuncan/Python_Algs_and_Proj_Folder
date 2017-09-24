import os
import subprocess

proc = subprocess.Popen("python test.py" ,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
x = proc.communicate()[0]

print(x)
