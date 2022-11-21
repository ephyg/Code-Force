n=int(input())
for i in range(n):
    s=input()
    if(len(s)>10):
        mid=len(s)-2
        print("{a}{b}{c}".format(a=s[0],b=mid,c=s[-1]))
    else:
        print (s)