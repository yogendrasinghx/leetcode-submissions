class Solution:

    def addBinary(self, a: str, b: str) -> str:
        n = len(a)
        m = len(b)
        if (n > m):
            t = n
            b = "0" * (n - m) + b

        else:
            t = m
            a = "0" * (m - n) + a

        c = ['0' for i in range(t + 1)]
        a = a[::-1]
        b = b[::-1]
        s = ""
        for i in range(t):
            if a[i] == '0' and b[i] == '0' and c[i] == '0':
                s = s + '0'
            elif a[i] == '0' and b[i] == '0' and c[i] == '1':
                s = s + '1'
            elif a[i] == '0' and b[i] == '1' and c[i] == '0':
                s = s + '1'
            elif a[i] == '0' and b[i] == '1' and c[i] == '1':
                s = s + '0'
                c[i + 1] = '1'
            elif a[i] == '1' and b[i] == '0' and c[i] == '0':
                s = s + '1'
            elif a[i] == '1' and b[i] == '0' and c[i] == '1':
                s = s + '0'
                c[i + 1] = '1'
            elif a[i] == '1' and b[i] == '1' and c[i] == '0':
                s = s + '0'
                c[i + 1] = '1'
            elif a[i] == '1' and b[i] == '1' and c[i] == '1':
                s = s + '1'
                c[i + 1] = '1'
            else:
                s = s + '0'
        if c[-1] == '1':
            return c[-1] + s[::-1]
        else:
            return s[::-1]