def garisMiring(num):
    pat =''
    for i in range(num):
        for j in range(num):
            if j == i:
                pat = pat+' * '
            else:
                pat = pat+'  '
        pat = pat+'\n'            
    print(pat)

garisMiring(8)