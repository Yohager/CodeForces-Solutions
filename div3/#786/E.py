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

def MatI(n):
    res = []
    for _ in range(n):
        res.append(LII())
    return res 

import math 


def calc(n,nums):
    ans = float('inf')
    # case 1 choose the minimum two positions
    f,s = sorted(nums)[0], sorted(nums)[1]
    ans = min(ans,math.ceil(f/2) + math.ceil(s/2))
    # case 2 choose one pos and let the left and right to be zero 
    for i in range(1,n-1):
        ans = min(ans,math.ceil((nums[i-1]+nums[i+1])/2))
    # case 3 choose two adjacent positions 
    # choose the max one and decrease to the min one 
    for i in range(1,n):
        x,y = max(nums[i],nums[i-1]), min(nums[i],nums[i-1])
        cur = min(x-y,math.ceil(x/2))
        x -= 2*cur 
        y -= cur 
        if x > 0 and y > 0:
            cur += math.ceil((x+y)/3)
        ans = min(ans,cur)
    return ans 

if __name__ == "__main__":
    n = II()
    nums = LII()
    res = calc(n,nums)
    print(res)