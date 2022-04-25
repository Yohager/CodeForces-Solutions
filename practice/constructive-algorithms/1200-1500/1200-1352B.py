import sys
import os
from io import BytesIO, IOBase
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def I():
    return input()
def II():
    return int(input())
def MI():
    return map(int, input().split())
def LI():
    return list(input().split())
def LII():
    return list(map(int, input().split()))
def GMI():
    return map(lambda x: int(x) - 1, input().split())

def calc(n,k):
    if n % 2 == 0 and n // 2 >= k:
        t = n // 2
        x = t // k 
        y = t % k
        ans = [2*x] * k 
        for i in range(y):
            ans[i] += 2
        return ans 
    elif (n-k) % 2 == 0:
        # ans = [1] * k 
        t = (n-k) // 2 
        x = t // k 
        y = t % k 
        ans = [1+2*x] * k 
        for i in range(y):
            ans[i] += 2 
        return ans 


def func(n,k):
    if n < k:
        return False 
    if n % 2 == 0:
        if n // 2 >= k:
            return True 
    if (n - k) % 2 == 0:
        return True 
    return False 


if __name__ == "__main__":
    tn = II()
    for _ in range(tn):
        n,k = LII()
        if not func(n,k):
            print('NO')
        else:
            print('YES')
            res = list(map(str,calc(n,k)))
            print(' '.join(res))

 