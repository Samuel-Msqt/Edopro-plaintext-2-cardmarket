IN = open('D:/lll_UTILE_lll/Bureau/Python/CardMarket/decklist_in.txt', 'r')
OUT = open('D:/lll_UTILE_lll/Bureau/Python/CardMarket/decklist_out.txt', 'w')

L=[]
L2=[]

for l in IN:
    L.append(l.strip())

for i in range (len(L)):
    if not(L[i]==''):
        L2.append(L[i])
L=[]
for i in range(len(L2)):
    if L2[i][-1] in str([1,2,3]):
        L.append(L2[i])
L2=[]

for i in range(len(L)):
    L2.append(L[i][-1]+' '+L[i][:-3]+'\n')

OUT.writelines(L2)

IN.close()
OUT.close()