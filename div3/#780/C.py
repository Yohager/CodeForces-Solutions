def func(arr):
    s = set()
    ans = len(arr)
    for x in arr:
        if x in s:
            ans -= 2
            s.clear()
        else:
            s.add(x)
    return ans 


if __name__ == "__main__":
    n = int(input())
    res = []
    for i in range(n):
        cur = list(input())
        res.append(func(cur))
    for r in res:
        print(r)