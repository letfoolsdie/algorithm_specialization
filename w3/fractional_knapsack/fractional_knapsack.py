# Uses python3
import sys

def get_optimal_value(capacity, weighs, values):
    value = 0
    remcap = capacity
    item_vals = [values[i]/weighs[i] for i in range(len(weighs))]
    for i in range(len(weighs)):
        maxval = item_vals.index(max(item_vals))
        if weighs[maxval] <= remcap:
            value += values[maxval]
            remcap -= weighs[maxval]
            weighs.remove(weighs[maxval])
            values.remove(values[maxval])
            item_vals.remove(item_vals[maxval])
            
        else:
            value += remcap*max(item_vals)
            return value
    
#    value = 0.
    # write your code here

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

#
#cap = 10
#weighs = [30]
#values = [500]
