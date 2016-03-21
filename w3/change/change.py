# Uses python3
import sys

def get_change(n):
    denom = [10, 5, 1]
    coins = 0
    for d in denom:
        coins += n//d
        n = n % d        
    return coins

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
