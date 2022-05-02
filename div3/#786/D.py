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


def calc(n,nums):
    if n == 1:
        return True 
    if n % 2 == 0:
        # a,b = nums[0], nums[1]
        # minv = min(nums)
        # if a != minv and b != minv:
        #     return False 
        # else:
        r = []
        for i in range(0,n,2):
            r.append([nums[i],nums[i+1]])
        for j in range(1,len(r)):
            if (r[j][0] < r[j-1][0] or r[j][1] < r[j-1][1]) and (r[j][1] < r[j-1][0] or r[j][0] < r[j-1][1]):
                return False 
            # r[j-1][0] and r[j][0] / r[j-1][1] and r[j][1]
            # r[j-1][1] and r[j][0] / r[j-1][0] and r[j][1]
                
    else:
        # a = nums[0]
        # minv = min(nums)
        # if a != minv:
        #     return False 
        # else:
        r = []
        for i in range(0,n-1,2):
            r.append([nums[i],nums[i+1]])
        r.append([nums[-1]])
        # print(r)
        for j in range(1,len(r)-1):
            if (r[j][0] < r[j-1][0] or r[j][1] < r[j-1][1]) and (r[j][1] < r[j-1][0] or r[j][0] < r[j-1][1]):
                return False 
        # check last one 
        # print(r[-1],r[-2])
        if r[-1][0] < min(r[-2][0],r[-2][1]):
            return False 

    return True

if __name__ == "__main__":
    tn = II()
    for _ in range(tn):
        n = II()
        nums = LII()
        res = calc(n,nums)
        if res:
            print('YES')
        else:
            print('NO')
        