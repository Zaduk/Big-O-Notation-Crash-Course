

# What is "Big O notation"?


# --> the function O plots the runtime (in microseconds) as a function of the input size (n)
# --> how time scales with respect to a some input variable (n, n**2, log(n))
# --> evaluates the time it takes for a function to run (runtime) as the input size increases
# --> in O(n), n is a mute variable. It can be represented by any letter, like for integrals.



# When calculating the time complexity or the runtime of a function, there are 4 general rules:



# 1. All the different runtimes get added

def rule1(x):
	c = x + 1 # O(a)
	d = x + 2 # O(b)
	return c,d

# Here, the runtime is O(a+b), whatever they are (n, n**2, log(n))




# 2. Drop constants

# O(kn) --> O(n)
#We only look at how each runtime varies. Linearly, in this case (in calc, f(x) = ax is a linear function)



# 3. Different function inputs ==> different variables

def rule3(array1,array2):
	#whatever operation on array1 --> O(a)
	#whatever operation on array2 --> O(b)
	pass

# Here, since there are two inputs, the runtime is O(a*b)

# 4. Only consider the fastest-growing terms (ignore lower-order)

# O(n+n**2) --> O(n**2)



#Important: the basic order of dominance for time complexities is:
# O(1) < O(log(n)) < O(n) < O(nlog(n)) < O(n**2) < O(n**k) < O(2**n) < O(n!)




# Examples


def test(array1):
	for i in array1: #--> O(n)
		for j in array1: # --> O(n)
			for k in array1: # --> O(n)
				print(i,j,k)
				

	# total runtime = O(n*n*n) = O(n**3)

def testq(array1):
	for i in array1:
		b = i + 1 #O(n) because the operation depends on the input
	for j in array1:
		a = i + 1 # O(n) because the operation depends on the input
	return a,b
	# total runtime = O(n+n) = O(2n) = O(n)






# --> the runtime is expressed as T = an + b for a linear n increase (but then with the rules above we obtain O(n))