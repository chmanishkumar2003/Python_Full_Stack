def anagram(st_1,st_2):
    
    if len(st_1)!=len(st_2):
        print("Not Ana")
    else :
        for i in st_1:
            if st_1.count(i)!=st_2.count(i):
                print("Not Ana")
        print("Anagram")

print(anagram("race","cared"))
