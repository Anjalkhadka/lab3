'''Write a function calledfizz_buzzthat takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number.'''
def calledfizz(num):
    if num%3==0:
     print('fizz')
    elif num%5==0:
     print(' buzz')
    elif num%3==0 and num%5==0:
     print('fizzbuzz')
    else:
     print("not divisible by the 5&3")
num=int(input('enter  a number : '))
calledfizz(num)



