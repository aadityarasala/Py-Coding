#Maximum Production Problem Code: EITA
T = int(input()) #total no of testcase 
for i in range(T):
    d, x, y, z = map(int, input().split()) 
    tr1 = x * 7 #trick1 
    tr2 = (y*d)+((7-d)*z) #trick2 
    result = [tr1, tr2]
    best = max(result)
    print(best)
