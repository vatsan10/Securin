dieA = [1,2,3,4,0,0]
dieB = [1,0,0,0,0,0]
sumCount={}
distribution = [[0] * 6 for _ in range(6)] 
for i in range(1,7):
        for j in range(1,7):
            distribution[i-1][j-1] = i + j
print(distribution)
print()
print()
for s in range(2, 13):
   count = sum(1 for row in distribution for value in row if value==s)
   sumCount[s]=count
print(sumCount)
print()
print()

for i in range(0,4):
    sumCount[1+dieA[i]]-=1
print(sumCount)
print()
print()


for i in range(0,2):
    k=1
    while(k<=4):
        if(sumCount[dieB[0]+k]>0):
            sumCount[dieB[0]+k]-=1
            break
        else:
            k+=1
    dieA[4+i]=k

print(dieA)      
print()
print()     
        

l=2
newsumCount=sumCount
i=0
print(sumCount)
print()
for j in range(1,len(dieB)):
    while(i<len(dieA)):
        if(sumCount[dieA[i]+l]>0):
            newsumCount[dieA[i]+l]-=1
            i+=1
            print(sumCount,i)
        else:
            newsumCount=sumCount
            i=0
            l+=1
    print(l)      
    dieB[j]=l
    sumCount=newsumCount
    i=0
    l+=1

print(dieA)
print(dieB)