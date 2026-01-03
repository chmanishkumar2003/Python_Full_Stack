def count(s):
    count=0
    for i in s:
        if i in "AEIOUaeiou":
            count=count+1
            print("Vowels are ",i)
    return count
s="Akash"
print("And count of Vowels are",count(s))
