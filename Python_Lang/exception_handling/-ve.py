class NegativeError(Exception):
    pass

def pos(n):
    if n < 0:
        raise NegativeError("Negative no. are not allowed")
    else:
        print("Number is positive")
