curStr = raw_input().split(' ')
t, m = int(curStr[0]), int(curStr[1])
a = []
ans = 1
for it in range(0, m):
    a.append(int(0))
for it in range(0, t):
    curStr = raw_input().split(' ')
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
            print 'NULL'
        else:
            print ans
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
        print 'ILLEGAL_ERASE_ARGUMENT'

