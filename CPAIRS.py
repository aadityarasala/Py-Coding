#Chef and Pairs Problem Code: CPAIRS
ta=int(input())
while ta:
    ta=ta-1 #total no of array (ta) 
    s=int(input()) #size of array (s)
    l=list(map(int,input().split())) #elements in array
    c=0 #cond
    c1=0 #cond
    for i in range(s):
        if((l[i]%2==0)):
            c+=1
        else:
            c1+=c
                
    print(c1)
