if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        a,b = list(map(int,input().split()))
        if a == 0:
            print('1')
        elif b == 0:
            print(str(a+1))
        else:
            print(str(a+2*b+1))
    