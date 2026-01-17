import itertools

class Solution:
    def largestSquareArea(self, bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
        max_side = 0
        
        # Iterate through every possible pair of rectangles
        for ((ax1, ay1), (ax2, ay2)), ((bx1, by1), (bx2, by2)) in \
            itertools.combinations(zip(bottomLeft, topRight), 2):
            
            # Find the boundaries of the intersection region
            # Left boundary is the rightmost of the two lefts
            # Right boundary is the leftmost of the two rights
            overlap_x = min(ax2, bx2) - max(ax1, bx1)
            overlap_y = min(ay2, by2) - max(ay1, by1)
            
            # If both overlap dimensions are positive, an intersection exists
            if overlap_x > 0 and overlap_y > 0:
                # The largest square that fits in a rectangle is limited by its smaller side
                current_side = min(overlap_x, overlap_y)
                max_side = max(max_side, current_side)
                
        return max_side * max_side