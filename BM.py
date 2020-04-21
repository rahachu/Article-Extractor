# Pencarian string dalam text
# menggunakan algoritmaBoyer-Moore

# Fungsi BMmatch
# input taget text dan pattern
# output posisi pattern pertama yang ditemukan
# -1 bila tidak ditemukan
def BMmatch(target,pattern):
    if len(pattern)>len(target):
        return -1
    i=len(pattern)-1
    j=len(pattern)-1
    last = buildLast(pattern)
    while i<len(target):
        if(target[i]==pattern[j]):
            if j==0:
                return i
            i-=1
            j-=1
        else:
            if target[i] in last:
                lo = last[target[i]]
            else:
                lo = -1
            i+=len(pattern)-min(j,lo+1)
            j=len(pattern)-1
    return -1


# Fungsi buildLast
# fungsi untuk membuat funsi last
# yaitu indeks char terakhir
# input patter
# output map dari last pattern
def buildLast(pattern):
    last = {}
    j=0
    for i in pattern:
        last[i]=j
        j+=1
    return last