import sys
import os
from io import BytesIO, IOBase
from collections import Counter, defaultdict
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

def MatI(n):
    res = []
    for _ in range(n):
        res.append(LII())
    return res 

def calc(n,k,arr):
    idxs = []
    for i in range(n):
        if arr[i] == '1':
            idxs.append(i)
    if not idxs:
        # 没有1
        return (n+k) // (k+1)
    # 统计头尾的情况
    elif len(idxs) == 1:
        # 只有一个1
        l,r = idxs[0], n-idxs[0]-1
        return max(0,l//(k+1)) + max(0,r//(k+1))
    else:
        # 超过两个1
        tmp = []
        for i in range(1,len(idxs)):
            tmp.append(idxs[i]-idxs[i-1]-1)
        ans = 0
        for t in tmp:
            cur = max(0,(t-k) // (k+1))
            ans += cur
        # 加上头尾
        l,r = idxs[0], n-idxs[-1]-1
        return ans + max(0,l//(k+1)) + max(0,r//(k+1))
        


if __name__ == "__main__":
    tn = II()
    for _ in range(tn):
        n,k = LII()
        nums = I()
        res = calc(n,k,nums)
        print(res)