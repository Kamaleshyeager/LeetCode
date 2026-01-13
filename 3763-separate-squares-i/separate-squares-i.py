class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        min_y = min(squares, key=lambda x: x[1])[1]
        max_y = max(y + s for _, y, s in squares)

        ta = sum(s[2] ** 2 for s in squares)
        half = ta / 2
        T = 10**-5

        def _area_under_y(y):
            a = 0
            for _, y0, s in squares:
                if y0 >= y:
                    continue
                elif y0 + s <= y:
                    a += s*s
                else:
                    a += s * (y - y0)
            return a

        def search(bottom, top):
            if top - bottom <= T:
                return top

            mid = (top + bottom) / 2

            auy = _area_under_y(mid)

            if auy >= half:
                top = mid
            elif half > auy:
                bottom = mid

            return search(bottom, top)

        return search(min_y, max_y)