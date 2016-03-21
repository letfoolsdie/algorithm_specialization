# Uses python3
import sys

def optimal_summands(n):
    if n == 1:
        return [1]
    summands = []
    for i in range(1,n+1):
        if n > i*2:
            summands.append(i)
            n -= i
        else:
            summands.append(n)
            break
    #write your code here
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
