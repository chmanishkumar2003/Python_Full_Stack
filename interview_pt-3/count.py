n=[1,2,3,3,3,4]
for i in n:
    count=0
    for j in n:
        if i == j:
            count=count+1
    if count==1:
     print("The numbers are",i)    
