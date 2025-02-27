import math
def distance(x1,y1,x2,y2):
    print(math.sqrt((x1-x2)**2+(y1-y2)**2))
def area_circle(r):
    print(math.pi*r**2)
def perimeter_cirle(r):
    print(2*r*math.pi)
def surfacearea_sphere(r):
    print(4*math.pi*r**2)
def volume_sphere(r):
    print(4/3*math.pi*r**3)
def Celius_Fahrenheit(C):
    print(9/5*C+32)
def Fahrenheit_Celius(F):
    print(5/9*F-32)
def perimeter_polygon(r,n):
    print(2*r*n*math.sin(math.pi/n))
def perimeter_triangle(x1,y1,x2,y2,x3,y3):
    a = distance(x1,y1,x2,y2)
    b = distance(x2,y2,x3,y3)
    c = distance(x3,y3,x1,y1)
    print(a+b+c)
def area_triagle(x1,y1,x2,y2,x3,y3):
    a = distance(x1,y1,x2,y2)
    b = distance(x2,y2,x3,y3)
    c = distance(x3,y3,x1,y1)
    p = (a+b+c)/2
    print(p*(p-a)*(p-b)*(p-c))
def find_ones(n):
    print(n%10)
def find_tens(n):
    print((n//10)%10)
def find_hundreds(n):
    print((n//100)%10)
def permutation_temp(a,b):
    temp = a
    a = b
    b = a
    print(a,b)
def permutation_nontemp(a,b):
    a = a + b
    b = a - b
    a = a - b
    print(a,b)
def loop1(n):
    i = 1
    s = 0
    while i <= n:
        s = s + i
def loop2(n):
    s = 0
    for i in range (1,n+1):
        s = s + i**2
def loop3(n):
    i = 1
    s = 0
    while i <= n:
        s = s + 1/i
def loop4(n):
    s = 0
    for i in range (1,n+1):
        s = s + 1/(2*i)
def loop5(n):
    s = 0
    i = 1
    while i <= n:
        s = s + 1/(2*i+1)
def loop6(n):
    t = 1
    for i in range(1,n+1):
        t = t * i
def loop7(n):
    t = 1
    i = 1
    while i <= n:
        t = t * (1 + 1/(i*i))
def loop8(n,x):
    t = x
    for i in range(i,n+1):
        t = t * (x+i)
def sum_digits(n):
    sum = 0
    absn=abs(n)
    while(absn!=0):
        sum = sum + (absn)%10
        absn = absn//10
def count_evendigits(n):
    count = 0
    absn = abs(n)
    while (absn!=0):
        if (absn%2==0):
            count +=1
        absn = absn//10
def product_digits(n):
    product = 0
    absn = abs(n)
    while (absn!=0):
        product *= (absn)%10 
        absn = absn//10
def find_maxdigits(n):
    absn = abs(n)
    max = absn % 10
    while (absn!=0):
        if (absn % 10 > max):
            max = absn % 10
        absn //= 10
def check_odd(n):
    absn = abs(n)
    while (absn!=0):
        if (absn % 2 == 1):
            return True
        absn//=10
    return False
def loop9(n):
    sum = 0
    temp = 1
    for i in range (1,n+1):
        temp *=i
        sum += temp
    return sum
def loop10(n,x):
    sum = 0
    for i in range (1,n+1):
        sum += x**(i*2)
    return sum
def loop11(n):
    sum = 0
    temp = 0
    for i in range (1,n+1):
        temp += i
        sum += 1/temp
    return sum
def loop12(n,x):
    sum = 0
    temp = 1
    for i in range(1,n+1):
        temp *= i
        sum += x**(i)/temp
    return sum
def loop13(n,x):
    sum = 1 + x
    temp = 1 
    for i in range(1,n+1):
        temp = temp * (2*i) * (2*i+1)
        sum += x**(2*i+1)/temp
    return sum
def loop14(n,x):
    sum = 0
    temp = 1
    for i in range (0,n+1):
        temp *= (x+i)
        sum += 1/temp
    return sum
def loop15(n,x):
    sum = 0
    temp = x
    for i in range(1, n+1):
        temp *= math.sin(temp)
        sum += temp
    return sum
def loop16(n,x):
    sum = 0 
    for i in range(1,n+1):
        sum += (-1**(n+1))*(x**i)
    return sum
def loop17(n):
    temp = 0
    for i in range(1,n+1):
        temp = math.sqrt(temp + i)
    return temp

def loop18(n):
    temp = 0
    for i in range(n,0,-1):
        temp = math.sqrt(temp + i)
    return temp
def loop19(n):
    ans = 0
    temp = 1
    for i in range(1,n+1):
        temp *= i
        ans = math.sqrt(temp+ans)
    return ans
def loop20(n):
    ans = 0
    for i in range(1,n+1):
        ans = (i+ans)**(1/(i+1))
    return ans
def accuracy():
    epsilon = 1e-6
    s = 0
    i = 1
    while (True):
        temp= 1/i
        if (abs(temp)<epsilon): break
        else: s += temp 
        i+=1
    return s
def sin(x):
    epsilon = 1e-6
    s = x
    term = x
    sign = -1
    temp = 1
    i = 1
    while (abs(term)>=epsilon):
        temp *= (2 * i) * (2 * i + 1)
        term = (x**(2*i+1))/ temp
        s+=sign*term
        sign*=-1
        i+=1
    return s    
def cos(x):
    epsilon = 1e-6
    s = 1
    term = 1
    sign = -1
    temp = 1
    i = 1
    while (abs(term)>=epsilon):
        temp *= (2 * i) * (2 * i - 1)
        term = (x**(2*i))/ temp
        s+=sign*term
        sign*=-1
        i+=1
    return s    
def e(x):
    epsilon = 1e-6
    s = 1
    term = 1
    temp = 1
    i = 1
    while (abs(term)>=epsilon):
        temp*=i
        term = (x**i)/temp
        s+=term
        i+=1
    return s
def pi():
    epsilon = 1e-6
    s = 4
    term = 4
    i = 1
    sign = -1
    while (abs(term)>=epsilon):
        term = 4/(2*i+1)
        s+=term*sign
        sign*=-1
        i+=1
    return s
def sequence(n):
    at = 2
    i = 2
    while(i<=n):
        at = at + 2 * i+1
        i+=1
    return at
def sequence2(n):
    att=-1
    at = 3
    i=2
    while(i<=n):
        att, at = at, 5 * at + 6 * att
        i+=1
    return at
def fibonacci(n):
    f0 = ftt =  1
    f1 =  ft = 2
    i =22
    while(i<=n):
        ftt, ft = ft, ftt + ft
        i+=1
    return ft
def sequence3(n):
    a=-1
    b = 3
    i=2
    while(i<=n):
        a, b = 3*b + 2*a, a + 3*b
        i+=1
    return a,b
def first_digit(n):
    n = abs(n)
    while(n>=10):
        n //=10
    return n
def reverse(n):
    if (n<0): sign = -1
    else: sign = 1
    n = abs(n)
    temp = 0
    while (n!=0):
        temp = temp * 10 + (n%10)
        n//=10
    return temp*sign
def is_perfect_number(n):
    if (n<0): return False
    s = 0
    for i in range(1,int(math.sqrt(n)+1)):
        if (n%i==0):
            s += i
            if i!=1 and n//i!=i:
                s += (n/i)
    if (s==n):
        return True
    return False
def is_palindrome_number(n):
    if (reverse(n)==n): return True
    return False
def greatest_common_divisor(m,n):
    a, b = abs(m), abs(n)
    while(a*b!=0):
        r = a % b
        a = b
        b = r
    return a+b
def least_common_multiple(m,n):
    a, b = abs(m), abs(n)
    while(a*b!=0):
        r = a % b
        a = b
        b = r
    return int(abs(m*n)/(a+b))
def is_leap_year(n):
    if (n%4==0 and n%100!=0): return True
    return False
def f(x):
    if (x<0): 
        return (-2*x**3+6*x+9)
    elif (0<=x and x<=1):
        return (5*x-7)
    else: return 2*x**3 + 5*x**2 - 8*x + 3  
def simple_equation(a,b):
    return (-b/a)
def quadratic_equation(a,b,c):
    delta = b**2 - 4*a*c
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    return x1,x2
def hailstone_sequences(n):
    a = n
    list = []
    while (a!=1):
        list.append(a)
        if (a%2==0):
            a = a//2
        else:
            a = 3*a +1
    list.append(a)
    return list
def count_min_digits(n):
    a = abs(n)
    count = 0
    min_digit = a % 10
    while (a!=0):
        if (a%10<min_digit): 
            min_digit = a% 10
            count = 1
        elif (a%10==min_digit): 
            count += 1
        a//=10
    return count
def greatest_odd_common_divisor(m,n):
    a, b = abs(m), abs(n)
    while(a*b!=0):
        r = a % b
        a = b
        b = r
    gcd = a+b
    while(gcd%2==0):
        gcd//=2
    return a+b
def is_prime(a):
    if a<=1:
        return False
    for i in range (2, int(math.sqrt(a))+1):
        if (a%i==0): return False
    return True