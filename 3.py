import math

st = 0
num = 9
col = ''
row = ''
mid = math.floor(num/2)
end = num-1

for r in range(num):
    if r == mid:
        for t in range(num):
            col = col+' @ '
    elif r < mid and r > st:
        inat = list(range( mid-r, mid+r+1))
        for p in range(num):
            if p in inat:
                col = col + ' @ '
            else:
                col = col + ' = '
    elif r == st or r == end:
        for s in range(num):
            if s == mid:
                col = col +' @ '
            else:
                col = col +' = '
    elif r > mid and r < end :
        inat = list(range(mid-(end-r),mid+(end-r)+1))
        for o in range(num):
            if o in inat:
                col = col+' @ '
            else:
                col = col+' = '

    col = col+'\n'
    row = col
print(row)
        
