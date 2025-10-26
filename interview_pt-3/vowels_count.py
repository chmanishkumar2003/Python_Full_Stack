a="ManishKumar"
n=len(a)
count=0
vowels="aeiouAEIOU"
for i in a:
    if i in vowels:
        count=count+1
print("The string contains vowels",count)
const=n-count
print("The string contains consonants",const)
