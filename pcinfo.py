# Programa criado em Python3
# Usado para capturar informacoes como modelo do cpu, VGA, placa mae e memoria.

import subprocess
import webbrowser
import os

os.system("lscpu")
os.system("lspci | grep VGA")
os.system("sudo dmidecode -t baseboard")
os.system("sudo dmidecode -t memory")

r = os.popen('sudo dmidecode -t baseboard').read() 
saida = r[r.index("Manufacturer: "):r.index("Version:")]

webbrowser.open_new_tab("http://www.google.com/search?q={}".format(saida))
