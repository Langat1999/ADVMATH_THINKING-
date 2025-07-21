#Point in Polygon (Ray Casting Algorithm)
#Concept: The Ray Casting algorithm determines whether a point lies inside a polygon. A horizontal “ray” is cast from the test point; if it intersects the polygon edges an odd number of times, the point is inside.
#A loop cycles through each edge of the polygon, counting how many times a horizontal line drawn from the test point intersects the polygon’s edges. If the count is odd, the point is inside; if even, it’s outside
def is_point_in_polygon(point, polygon):
    """Determine if a point (x, y) lies inside a polygon defined by a list of vertices."""
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]

        # Check if the horizontal ray intersects the edge
        if min(p1y, p2y) < y <= max(p1y, p2y):
            if x <= max(p1x, p2x):
                if p1y != p2y:
                    xinters = (y - p1y) * (p2x - p1x) / ((p2y - p1y) + 1e-10) + p1x
                else:
                    xinters = p1x
                if p1x == p2x or x <= xinters:
                    inside = not inside

        p1x, p1y = p2x, p2y

    return inside