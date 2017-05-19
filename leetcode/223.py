'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
'''

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = (D - B) * (C - A)
        area2 = (H - F) * (G - E)
        area = area1 + area2

        if C <= E or A >= G: return area
        if B >= H or D <= F: return area

        x1, y1 = 0, 0
        if A < E: x1 = E
        else: x1 = A

        if B < F: y1 = F
        else: y1 = B

        x2, y2 = 0, 0
        if C < G: x2 = C
        else: x2 = G

        if D < H: y2 = D
        else: y2 = H

        cross = 0
        if y2 >= y1 and x2 >= x1:
            cross = (y2 - y1) * (x2 - x1)

        return area - cross
