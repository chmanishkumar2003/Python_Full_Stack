try:
	n=int (input (“Enter no.”))
	res=10/n
except ZeroDivisionError:
	print (“U can’t divide with 0”)
except ValueError:
	print (“U can’t divide with -ve no.”)
else:
	print (“The result =”, res)
finally:
	print (“Code Executed”)
