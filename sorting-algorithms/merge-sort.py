# Sorts the given array and counts inversions in nlogn time.
inversions = 0
def read():
    F = open("IntegerArray2.txt","r")
    K = []
    L = F.read().splitlines()
    for i in L:
        K.append(int(i))
    return K
	
def sort(L):
    if len(L) > 1:
        return merge(sort(L[:(len(L)/2)]),sort(L[(len(L)/2):]))
    else:
        return L

def merge(L1, L2):
    global inversions
    L = []
    i1, i2 = 0,0
    l1, l2 = len(L1),len(L2)
    while(True):
        if i1 == l1:
            for i2 in range(i2,l2):
                L.append(L2[i2])
            break
        elif i2 == l2:
            for i1 in range(i1,l1):
                L.append(L1[i1])
            break
        else:
            if L2[i2] >= L1[i1]:
                L.append(L1[i1])
                i1 = i1 + 1
            else:
                L.append(L2[i2])
                i2 = i2 + 1
                inversions = inversions + (l1-i1)
    return L

L = sort(read())
print inversions        
