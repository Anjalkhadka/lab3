'''Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.'''
def prime(num):
    if num%2==0 or num%3==0:
        return "not a prime"
    else:
        return "prime number"
number=int(input("enter a anumber: "))
i=prime(number)
print(i)
