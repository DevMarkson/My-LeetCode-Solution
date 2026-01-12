class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total = 0

        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            total += max(dx, dy)
        return total