class Solution(object):
    def spiralOrder(self, matrixrix):
        """
        :type matrixrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrixrix) == 0:
            return []

        res = []
        m, n = 0, len(matrixrix) - 1
        i, j = 0, len(matrixrix[0]) - 1

        while m <= n and i <= j:
            if m == n:
                for idx in range(i, j + 1):
                    res.append(matrixrix[m][idx])
                return res
            if i == j:
                for idx in range(m, n + 1):
                    res.append(matrixrix[idx][i])
                return res

            for idx in range(i, j):
                res.append(matrixrix[m][idx])

            for idx in range(m, n):
                res.append(matrixrix[idx][j])

            for idx in range(j, i, -1):
                res.append(matrixrix[n][idx])

            for idx in range(n, m, -1):
                res.append(matrixrix[idx][i])

            i, j = i + 1, j - 1
            m, n = m + 1, n - 1

        return res

if __name__ == '__main__':
    mat = [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]

    so = Solution()

    print so.spiralOrder(mat)

    mat2 = [
            [ 1, 2, 3, 4],
            [ 5, 6, 7, 8],
            [ 9, 10, 11, 12],
            [ 13, 14, 15, 16]
        ]

    print so.spiralOrder(mat2)
    print so.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
    print so.spiralOrder([[1]])
    print so.spiralOrder([[1], [2]])
    print so.spiralOrder([[7],[9],[6]])
    print so.spiralOrder([[1,2],[3,4],[5,6],[7,8]])
    print so.spiralOrder([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
    print so.spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])


