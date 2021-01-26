#PROGRAM KODE POS BY MANDO

import requests
import json
import os
os.system('clear')
print("""
\t                 PROGRAM KODE POS
\t               DI BERBAGAI KECAMATAN
\t                CREATOR SC : MANDO
""")
print(70*'=')
url='https://kodepos-2d475.firebaseio.com/kota_kab/k69.json?print=pretty'
req=requests.get(url)
jeson=json.loads(req.text)
j=0


for data in jeson:
    j += 1
    print('\tnomor', str(j))
    print('\tNAMA KECAMATAN :', data[ 'kecamatan'])
    print('\tNAMA KELURAHAN :', data[ 'kelurahan'])
    print('\tKODE POS NYA   :', data[ 'kodepos'])
    print('\t'+37*'=')

