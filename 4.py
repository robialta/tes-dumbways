import re

def hitung(str, kata):
    if len(kata) > len(str):
        print('String harus lebih panjang')
    else:
        kata_rv = kata[len(kata)::-1]
        str_rv = str[len(str)::-1]
        val = re.findall(kata, str) + re.findall(kata_rv, str) + re.findall(kata_rv, str_rv)
        print(len(val))
    
hitung('bandanadana', 'dana')
