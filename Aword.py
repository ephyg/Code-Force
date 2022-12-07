x=input()
cUpper=0
cLower=0
for i in range(len(x)):
    if(x[i]==x[i].upper()):
        cUpper+=1
    else:
        cLower+=1
if(cUpper>cLower):
    print(x.upper())
else:
    print(x.lower())