'''Write a Python program to reverse a string.'''
def reverese(string):
    string=string[::-1]#slice operator [start :stop: step]
    print(string)
a=str(input("enetr a word  : "))
reverese(a)
