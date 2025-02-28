import Fuction as f
def input_array():
    n = int(input())
    return [int(input()) for _ in range(n)]
def list_odd(a):
    l_odd = []
    for i in a:
        if i % 2 == 1:
            l_odd.append(i)
    return l_odd
def sum_negative(a):
    sum = 0
    for i in a:
        if i <0:
            sum+=i
    return sum

def count_prime(a):
    count = 0
    for i in a:
        if f.is_prime(i):
            count+=1
    return count
def sub_array(a):
    for l in range (1,len(a)+1):
        for i in range(0,len(a)-l+1):
            print(a[i:i+l])

print("Hello Word")



