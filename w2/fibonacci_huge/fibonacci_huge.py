# Uses python3
import sys

def get_fibonaccihuge(n, m):
#    d1 = 1
#    d2 = 1
#    for i in range(2,n):
#        d3 = (d1+d2)%m
#        d1 = d2%m
#        d2 = d3%m
    return 0

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
