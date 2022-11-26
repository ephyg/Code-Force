x=list(map(int,input().split()))
n=x[0]
k=x[1]
a=list(map(int,input().split()))
a.sort()
a=a[::-1]
y=0
for i in range(n):
    if((a[i]>0) and (a[i]>=a[k-1])):
        y+=1
    else:
        break
print(y)