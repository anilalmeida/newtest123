# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 
# Then, the output should be:40320

# using for
'''
def fact(n):
    factor = 1
    for i in range(1, n +1):
        factor = factor * i
    return factor

i = int(input())
print(fact(i))
'''

# Using while
''''
initial  = 1
fact = 1
num = int(input( "Enter a number "))
while initial <= num:
    fact = fact * initial
    initial+=1
print(fact)
'''

# Using Lambda
init = 1
fact = 1
# num = int(input("Enter a number "))
factor = lambda num : [fact * i for i in range(1, num+1)]
print(num(5))



