# You are given a list of points where each point is a 2D coordinate on a plane.
# You start at the first point and must visit all other points in order.
# Return the minimum time required to visit all points, where:
# You can move in horizontal, vertical, or diagonal directions.
# 1 unit per second in any of those directions.

points = [[1,1],[3,4],[-1,0]]
# Output: 7

def minTimeToVisitAllPoints(points):
    time= 0;
    
    for i in range(1,len(points)):
        x1,y1 = points[i-1]
        x2,y2 = points[i]
        
        dx = abs(x2-x1)
        dy = abs(y2-y1)
        
        time += max(dx,dy)
    
    return time

print(minTimeToVisitAllPoints(points))
        