
def makealbertpresident(A,B,C,D):
    a=(A+D)
    b=((A*C)-(3*B))
    c=((A*B)*(A*B))
    d=((C*D)/(A*B))
    print(a, b, c, d)

def count_schedules(n):
    dp = [[0, 0] for _ in range(n + 1)]
 
    
    dp[1][0] = 1  # G
    dp[1][1] = 1  # T
 
    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]   
        dp[i][1] = dp[i-1][0]               
 
    return dp[n][0] + dp[n][1]

def ratioAgain(gurls_ratio,boys_ratio,multiple):
    diff = boys_ratio-gurls_ratio
    total_ratio = gurls_ratio+boys_ratio
    multiplier = multiple/diff
    total = total_ratio*multiplier
    return int(total)

def perimeter(h_length, v_length):
    one = h_length//2
    two = v_length//2
    length = one**2 + two**2
    length = sqrt(length)
    return length*4

def bearing_q(known_bearing):
    known_bearing = list(known_bearing)
    if known_bearing[0] == "0":
        bearing = known_bearing[1:]
    else:
        bearing = known_bearing
    bearing_int = ''.join(bearing)
    bearing_int = int(bearing_int)
    new_bearing = 360-bearing_int
    new_bearing = list(str(new_bearing))
    if new_bearing[0] == "0":
        output = new_bearing[1:]
    else:
        output = new_bearing  
    return ''.join(output)

def cuboidvolume(a,b,c):
    cuboidv=(a*b*c)
    print("The volume of the cuboid is",cuboidv)

def ratiogb(g,b):
    c = ((g+b)*4)
    print(c)

def isPrime(n):
    n = int(n)
    i = 2
    while n > 1:
        while n % i == 0:
            print(i, end=" ")
            n //= i
        i += 1
def add(a,b):
    a = int(a)
    b = int(b)
    print(a+b)

 
def times(a,b):
    a = int(a)
    b = int(b)

    print(a*b)
 

 
def subtract(a,b):
    a = int(a)
    b = int(b)
    print(a-b)

 
def divide(a,b):
    a = int(a)
    b = int(b)
    print(a/b)

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
    print(count)

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
    d = int(d)
    h = int(h)
    area = ((d/2)**2)*3
    volume = area * h
    print('area of cross section', area, 'cm^2')
    print('volume is:', volume, 'cm^3')
    print('capacity is:', volume, 'ml')



def main():
    print('cool')
    
    quit = False
    try:
        while not quit:
            calc = input('>>> ')
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
            
            elif args[0] == 'ratio':
                ratiogb(args[1], args[2])
            
            elif args[0] == 'add':
                add(args[1], args[2])
            elif args[0] == 'subtract':
                subtract(args[1], args[2])
            elif args[0] == 'times':
                times(args[0], args[1])
            elif args[0] == 'divide':
                divide(args[1], args[2])
            elif args[0] == 'bearing':
                bearing_q(args[1])
            elif args[0] == 'perimeter':
                perimeter(args[1], args[2])
            elif args[0] == 'ratioAgain':
                ratioAgain(args[1], args[2], args[3])
            elif args[0] == 'schedules':
                count_schedules(args[1])
            
            
            
            
            
    except:
        print('lol')
            

        
main()

    