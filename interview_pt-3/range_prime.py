n=50
for i in range(2,n):
    count=0
    for a in range(2,i):
        if i % a == 0:
            count=count+1
            break
    if count == 0:
        print(i,"It is prime no.") 
