n=4
class Check:
    @staticmethod
    def even(n):
        if n % 2 == 0:
            return True
        else:
            return False
print(f"Is {n} is Even ? {Check.even(n)}")
