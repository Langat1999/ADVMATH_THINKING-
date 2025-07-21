#Convex Hull using Graham’s Scan
#Concept: Given a set of points in the plane, the convex hull is the “rubber band” that tightly encloses all points. Graham’s scan sorts the points angularly around the lowest point and then constructs the hull using a stack to prune concave turns.
#Preprocessing: Find the lowest point as a pivot.
#Sorting: Sort rest of the points based on the angle they make with the pivot (and by distance if they are collinear).
#Building the Hull: Iterate through sorted points. Use the orientation function to keep only those points that make a counterclockwise turn, effectively “pushing out” the convex boundary
import math

def orientation(p, q, r):
    """
    Return the orientation of the triplet (p, q, r).
    Returns:
        > 0 if counterclockwise,
        < 0 if clockwise,
        0 if collinear.
    """
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def distance_sq(p, q):
    """Return the squared Euclidean distance between points p and q."""
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def convex_hull(points):
    # Find the starting point (lowest y-coordinate, then lowest x in case of tie)
    start = min(points, key=lambda p: (p[1], p[0]))

    # Sort points by polar angle and distance from the start
    sorted_points = sorted(points, key=lambda p: (
        math.atan2(p[1] - start[1], p[0] - start[0]),
        distance_sq(start, p)
    ))

    hull = []
    for p in sorted_points:
        # Remove last point in hull if it makes a non-left turn
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull

# Example points