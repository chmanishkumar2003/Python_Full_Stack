m="ManishKumar"
n=m.lower()
for i in n:
    if n.count(i) == 0:
        continue
    print(f"{i}:{n.count(i)}")
