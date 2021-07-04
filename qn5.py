'''Write a function called show_stars(rows).If rows is 5, it should print the following:'''

row=5
def show_star():
    for i in range(0,row):
        for j in range (0,i+1):
             print("*",end='')
        print("\r")
show_star()
