# Uses python3
import sys
from collections import namedtuple
import numpy as np

Segment = namedtuple('Segment', 'start end')

def has_intersection(a1, b1, a2, b2):
    if b1 >= a2 and b2 >= a1:
        return True
    else:
        return False

# def optimal_points(segments):
#     points_a = []
#     points_b = []
#     #write your code here
#     for s in segments:
#         points_a.append(s.start)
#         points_b.append(s.end)
        
#     points_b_arranged_idx = np.argsort(points_b)
#     points_a = np.array(points_a)[points_b_arranged_idx]
#     points_b = np.array(points_b)[points_b_arranged_idx]
#     n = len(points_b)
    
#     za_points = []
#     i = 1
#     while i < n:
#         prev_a = points_a[i-1]
#         prev_b = points_b[i-1]
        
#         comp_a = points_a[i]
#         comp_b = points_b[i]
#         #print(comp_b)
#         if not has_intersection(prev_a, prev_b, comp_a, comp_b):
#             if not prev_b == comp_b:
#                 if prev_b not in za_points:
#                     za_points.append(prev_b)
#                 if comp_b not in za_points:
#                     za_points.append(comp_b)
#                 else:
#                     pass
#             else:
#                 if comp_b not in za_points:
#                     za_points.append(comp_b)
#                 else: pass
#         else:
#             if prev_b not in za_points:
#                 za_points.append(prev_b)
#             else: pass
#         while i < n:
#             if has_intersection(prev_a, prev_b, comp_a, comp_b):
#                 prev_a = points_a[i]
#                 i += 1
#                 if i >= (n):
#                     break
#                 comp_a = points_a[i]
#                 comp_b = points_b[i] 

#             else:
#                 #za_points.append(prev_b)
#                 #za_points.append(comp_b)
#                 break
#         i += 1
#     return za_points
def optimal_points(segments):
    points_a = []
    points_b = []
    #write your code here
    for s in segments:
        points_a.append(s.start)
        points_b.append(s.end)
        
    points_b_arranged_idx = np.argsort(points_b)
    points_a = np.array(points_a)[points_b_arranged_idx]
    points_b = np.array(points_b)[points_b_arranged_idx]
    n = len(points_b)
    
    i = 0
    count = 0
    #pos = points_b[0]
    point = []
    while i<n:
        pos = points_b[i]
        point.append(pos)
        i += 1

        while i < n and pos >= points_a[i]:
            count += 1
            i += 1
            
    return point


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
