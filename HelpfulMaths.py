n=input()
x=[]
for i in range(len(n)):
    if(i%2==0):
        x.append(n[i])
x=[int(i) for i in x]
x.sort()
y=""
j=0
for i in range((len(x)*2)-1):
    if(i%2==0):
        y+=str(x[j])
        j+=1
    else:
        y+="+"
print(y)
