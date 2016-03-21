# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
#    seg = [x._asdict() for x in segments]
    points = []
    for i in range(len(segments)):
        minend = min([i.end for i in segments])
        points.append(minend)
        segments = [s for s in segments if s.start>minend]
        if len(segments) == 0:
            break
    return points
    #write your code here
#    for s in segments:
#        points.append(s.start)
#        points.append(s.end)
#    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#    print(segments)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

#R = [Segment(1,3), Segment(2,5), Segment(3,5)]
#R1 = [Segment(4,7), Segment(1,3),Segment(2,5),Segment(5,6)]