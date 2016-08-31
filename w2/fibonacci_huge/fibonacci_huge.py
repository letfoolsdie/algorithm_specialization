# Uses python3
import sys

#def get_fibonaccihuge(n, m):
#    d1 = 1
#    d2 = 1
#    for i in range(2,n):
#        d3 = (d1+d2)%m
#        d1 = d2%m
#        d2 = d3%m
#    return 0

#if __name__ == '__main__':
#    input = sys.stdin.read();
#    n, m = map(int, input.split())
#    print(get_fibonaccihuge(n, m))

#m = 1000
#n = 239

input = sys.stdin.read()
n, m = map(int, input.split())

def F():
    a, b = 1, 2
    while True:
        a, b = b, a + b
        yield a


def pisano(m):        
    period = [0, 1]
    fib = F()
    while True:
        period.append(next(fib) % m)
        if (period[-1] == 1) and (period[-2] == 0):
            break
    return period[:-1]
    
pis = pisano(m)
#print(pis[n % m])
ind = n % len(pis)
if ind <= 1:
    print(pis[ind])
else:
    print(pis[ind - 1])
#print(pis)
