#The following chunk of code calculates the recaman sequence of a specified length
n = int(input("Please, specify the number of elements in the Recaman Sequence you want to compute: "))
l_elem = []

for num in range(n):
	if num==0:
		l_elem.append(num)
	elif (l_elem[num-1]-num>0) and (l_elem[num-1]-num) not in l_elem:
		l_elem.append(l_elem[num-1]-num)
	else:
		l_elem.append(l_elem[num-1]+num)

print(l_elem)
