# def solution(arr):
#     res = 0
#     for num in range(len(arr)):
#         priority = 1
#         sum = 0
#         for j in sorted(arr):
#             sum += priority * j
#             priority += 1
#         res = max(res, sum)
#         if arr[0] <= arr[len(arr)-1]:
#             arr.remove(arr[0])
#         else:
#             arr.remove(arr[len(arr)-1])
#     return res if res >= 0 else 0

def solution(arr):
    res, sum = 0, 0
    arr.sort()
    for i in range(len(arr)):
        count = 1
        sum = 0
        for num in arr[i:]:
            sum += num * count
            count+=1
        res = max(sum, res)
    return res
            

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solution(arr))
