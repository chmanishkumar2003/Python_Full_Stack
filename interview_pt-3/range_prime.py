n=50
for i in range(2,n):
    count=0
# a is used for take number and compare with all i's.
    for a in range(2,i):
        if i % a == 0:
            count=count+1
            break
    if count == 0:
        print(i,"It is prime no.") 
