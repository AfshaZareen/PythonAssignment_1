'''Write a python program that generates the first n numbers in the Fibonacci sequence.'''

n = int(input("Enter the number: "))
fnm1 = 1
fnm2 = 0
if (n == 0):
    print(fnm2, end = " ")
else :
    print(fnm2, fnm1, end = " ")
for i in range(2,n) :
    fib = fnm1 + fnm2
    print(fib, end = " ")
    fnm2 = fnm1
    fnm1 = fib