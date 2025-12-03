

def makealbertpresident(A,B,C,D):
    a=(A+D)
    b=((A*C)-(3*B))
    c=((A*B)*(A*B))
    d=((C*D)/(A*B))
    print(a, b, c, d)

def cuboidvolume(a,b,c):
    cuboidv=(a*b*c)
    print("The volume of the cuboid is",cuboidv)

def isPrime(n):
    n = int(n)
    i = 2
    while n > 1:
        while n % i == 0:
            print(i, end=" ")
            n //= i
        i += 1

def two_digits_and_squares():
    squares = []
    for x in range(100):
        squares.append(x**2)
    count = 0
    for x in range(10,100):
        for i in range(10,100):
            num = x*i
            if num in squares:
                count += 1
    return count

def isSquare(x):
    x = int(x)
    while x < 10 or x > 99:
        print("That is not a 2-digit number")
        x = int(input("Re-enter your 2-digit number"))
    arr = list(str(x))
 
    if arr[0]== arr[1]:
        print(True)
    else:
        print(False)
 
def cylinder(d,h):
    area = ((d/2)**2)*3
    volume = area * h
    print('area of cross section', area, 'cm^2')
    print('volume is:', volume, 'cm^3')
    print('capacity is:', volume, 'ml')



def main():
    print('cool')
    calc = input('>>> ')
    quit = False
    try:
        while not quit:
            args = calc.split(' ')
            
            if args[0] == 'albert':
                makealbertpresident(2, -3, 0.5, -12)

            elif args[0] == 'digitSquare':
                two_digits_and_squares()

            elif args[0] == 'isSquare':
                isSquare(args[1])

            elif args[0] == 'cylinder':
                cylinder(args[1], args[2])
            
            elif args[0] == 'prime':
                isPrime(args[1])
            
            
            

        


    