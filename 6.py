# fungsi menentukan bilangan prima 
def prima(n):
    a = 5
    b = 7
    bil_prima = [2, 3, a, b]
    while len(bil_prima) < n*n-n*2:
        x = a + 6
        y = b + 6
        if x % 5 > 0:
            bil_prima.append(x)
        if y%5 > 0:
            bil_prima.append(y)
        a = x
        b = y
    return(bil_prima)

# fungsi membuat
def segitiga(num):
    if num %2 == 0 or num < 0 or num >10:
        print('Input parameter salah')
    else:
        pr = prima(num)
        sg =''
        np = 0
        for i in range(num):
            for j in range(i+1):
                sg = sg+str(pr[np])+' '
                np+=1
            sg = sg+'\n'
        print(sg)
segitiga(9)
