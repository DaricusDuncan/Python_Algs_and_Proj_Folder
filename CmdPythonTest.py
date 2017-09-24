import os
import subprocess

proc = subprocess.Popen("python test.py" ,stdout=subprocess.PIPE)
x = proc.communicate()[0]

print(x)
