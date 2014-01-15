import testtools
import unittest


class Solution:
    def __init__(self):
        pass

    def read(self, t, m, lst):
        ansSolution = []
        a = []
        ans = 1
        for it in range(0, m):
            a.append(int(0))
        for it in lst:
            curStr = it.split(' ')
            op = curStr[0]
            if op == 'defragment':
                b = []
                for i in range(0, m):
                    if a[i] != 0:
                        b.append(a[i])
                en = m - len(b)
                for i in range(0, en):
                    b.append(int(0))
                a = b
                continue
            if op == 'alloc':
                n = int(curStr[1])
                cur = 0
                pos = -1
                for i in range(0, m):
                    if a[i] != 0:
                        cur = 0
                        continue
                    cur += 1
                    if cur >= n:
                        pos = i - cur + 1
                        break
                if pos == -1:
                    ansSolution.append('NULL')
                else:
                    ansSolution.append(ans)
                    ans += 1
                    for i in range(0, n):
                        a[pos + i] = ans - 1
                continue
            fl = 1
            num = int(curStr[1])
            for i in range(0, m):
                if a[i] == num:
                    a[i] = 0
                    fl = 0
            if fl or num == 0:
                ansSolution.append('ILLEGAL_ERASE_ARGUMENT')
        return ansSolution


class TestSolution(testtools.TestCase):
    def test1_read(self):
        test1 = Solution()
        self.assertEqual([1], test1.read(1, 1, ['alloc 1']))
    def test2_read(self):
        test2 = Solution()
        self.assertEqual(['NULL'], test2.read(1, 1, ['alloc 3']))
    def test3_read(self):
        test3 = Solution()
        self.assertEqual(['NULL', 1], test3.read(2, 1, ['alloc 3', 'alloc 1']))


if __name__ == "__main__":
    unittest.main()


