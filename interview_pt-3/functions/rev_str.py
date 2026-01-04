def revs(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
s="Manish"
print(revs(s))
