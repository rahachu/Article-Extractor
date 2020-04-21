# Pencarian string dalam suatu teks dengan
# menggunakan algoritma Knuth-Morris-Pratt
# implementasi algoritma dasar

# Fungsi KMP matching
# Input terget text dan pattern
# output posisi pattern pertama yang ditemukan
# -1 bila pattern tidak ditemukan
def KMPmatch(target,pattern):
    if len(pattern)>len(target):
        return -1
    b = computeBorder(pattern)
    i=0
    j=0
    while i<len(target):
        if target[i]==pattern[j]:
            if j==len(pattern)-1:
                return i+1-len(pattern)
            i+=1
            j+=1
        elif j>0:
            j=b[j-1]
        else:
            i+=1
    return -1


# Fungsi pinggiran (Border function)
# funsi pinggiran adalah fungsi yang menghasilkan
# besar karakter yang terdapat pada akhir ketidak cocokan
# dengan awal pola
# Fungsi compute border menghasilkan hasil fungsi border
# untuk setiap posisi ketidakcocokan
# input string dari pattern
# output array of integer
def computeBorder(pattern):
    fail = [0 for i in pattern]
    j = 0
    i = 1
    while i<len(pattern):
        if pattern[j]==pattern[i]:
            fail[i]=1+j
            i+=1
            j+=1
        elif j>0:
            j=fail[j-1]
        else:
            fail[i]=0
            i+=1
    return fail