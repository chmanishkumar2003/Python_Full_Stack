class NegativeError(Exception):
    pass

def pos(n):
    if n < 0:
        raise NegativeError("Negative no. are not allowed")
    else:
        print("Number is positive")
try:
    pos(-5)
except NegativeError as e:
    print("Error :",e)

with open("ans_of-1.txt","w") as file:
    file.write("Hello,Python!")
print(file.closed)
