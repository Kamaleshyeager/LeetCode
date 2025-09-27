import math
from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def getDist(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.sqrt(dx * dx + dy * dy)

        max_area = 0.0
        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a = getDist(points[i], points[j])
                    b = getDist(points[j], points[k])
                    c = getDist(points[k], points[i])

                    S = (a + b + c) / 2.0

                    radicand = S * (S - a) * (S - b) * (S - c)
                    radicand = max(0.0, radicand)  # safeguard

                    area = math.sqrt(radicand)
                    max_area = max(max_area, area)

        return max_area