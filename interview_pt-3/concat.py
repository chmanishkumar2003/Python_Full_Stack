s={'Name':'Manish'}
a={'Age':24}
def add(s,a):
    return {**s,**a}
print(add(s,a))
