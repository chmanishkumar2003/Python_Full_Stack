def my_decorator(fun):
    def wrapper():
        print("before the function runs")
        fun()
        print("After the function run")
    return wrapper
@my_decorator   #this is the decorator to hello()
def hello():
    print("Helo world!")
hello() 
