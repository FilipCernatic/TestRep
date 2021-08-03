#This chunk of code computes the sine function up to an arbitrary accuracy

def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

def sin(x,n):
	result = 0
	for k in range(1,n+1):
		result += ((-1)**(k-1))*(x**(2*k-1))/(factorial(2*k-1))
	return result

print("sin(x), Taylor series expansion.")
x = float(input("Angle: "))
n = int(input("Number of terms: "))
print("Result: ",sin(x,n))
