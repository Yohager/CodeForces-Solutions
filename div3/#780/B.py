if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        cnt = int(input())
        nums = list(map(int,input().split()))
        if cnt == 1:
            if nums[0] == 1:
                print('Yes')
            else:
                print('No')
        else:
            f,s = 0,0
            for i in range(cnt):
                if nums[i] > f:
                    s = f 
                    f = nums[i]
                elif nums[i] > s:
                    s = nums[i]
            # print(f,s)
            print('Yes') if f-s <= 1 else print('No')