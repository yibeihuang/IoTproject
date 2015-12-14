import subprocess
import os
def address():
    api = subprocess.Popen('python flux_led.py -s', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    api.wait()
    temp = api.stdout.readlines()[1]
    addr = temp.strip()
    return addr

def on(addr):
    api = subprocess.Popen('python flux_led.py '+addr+' --on', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def Light(addr,color):
    api = subprocess.Popen('python flux_led.py '+addr+' -c '+ color, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

  #if sign == 0:
    #api = subprocess.Popen('python flux_led.py '+addr+' -c green', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def warning(addr):
    api = subprocess.Popen('python flux_led.py '+addr+' -p 0x31 70', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def off(addr):
  api = subprocess.Popen('python flux_led.py '+addr+' -c black', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  #api.wait()
