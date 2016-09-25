L1 = raw_input()
L2 = raw_input()
row = []
prev = 0
for i in range(len(L1)+1):
        row.append(0)
for j in range(0,len(L2)):
        for i in range(0,len(L1)):
                if L1[i]==L2[j]:
                        temp = row[i+1]
                        row[i+1] = prev+1
                        prev = temp
                else:
                        temp = row[i+1]
                        row[i+1] = max(row[i],temp)
                        prev = temp
        prev = 0
print row[-1]
