import re

def cek(p, s):
    val = False
    for o in p:
        if re.search(o, s) is not None:
            val = True
            break
    return val

def is_username_valid(username):
    kecil = 'abcdefghijklmnopqrstuvwxyz'
    besar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    angka = '1234567890'
    special = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    if len(username) > 5 or len(username) < 9:
        if(special.search(username[0]) is None): 
            if cek(username, kecil) and cek(username, besar) and cek(username, angka):
                return True
            else:
                return False    
        else: 
            return False           
    else:
        return False

def is_password_valid(password):
    symbol_wajib = re.compile('@')
    special = re.compile('[_!#$%^&*()<>?/\|}{~:]')
    kecil = 'abcdefghijklmnopqrstuvwxyz'
    besar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    angka = '1234567890'
    if len(password) >= 8:
        if symbol_wajib.search(password)  is not None:
            if cek(password, kecil) and cek(password, besar) and cek(password, angka):
                specialTrue = False
                for pp in password:
                    if special.search(pp) is not None:
                        return True
                        break
                return specialTrue
            else:
                return False
        else:
                return False
    else:
            return False
        
print(is_username_valid('@Najibb'))
print(is_username_valid('Ayug9v'))
print(is_password_valid('p@ssW0rd#'))
print(is_password_valid('DumbW4ysDev99!#'))





    