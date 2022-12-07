n=int(input())
cnt=0
for i in range(n):
    x=input()
    if(x=="++X" or x=="X++"):
        cnt+=1
    if(x=="--X" or x=="X--"):
        cnt-=1
print(cnt)
