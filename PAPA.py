#coding=utf-8
import os, sys, platform

os.system('xdg-open https://chat.whatsapp.com/J7W0XhWjOCM5e78jQc10aX')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf COOL.cpython-311.so')
except:
    pass
os.system('rm -rf COOL.cpython-311.so')
os.system('git pull')
try:os.mkdir('/sdcard/PAPA')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('COOL.cpython-311.so'):
        os.system('curl -L https://raw.githubusercontent.com/PAPA-71/PAPA-PRO/main/COOL.cpython-311.so?raw=true -o COOL.cpython-311.so') 
        import COOL
    else:
        import COOL