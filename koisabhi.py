def solution(arr, coco):
    pos, neg = -float("inf"), 0
    res, final_res = 1, 0
    n = len(arr)
    for i in range(n):
        c, rem_pos, rem_neg = 0, 0, 0
        for i in arr:
            val = coco - i
            if val > 0:
                if pos < val:
                    pos = val
                    rem_pos = i
            else:
                if abs(neg) < abs(val):
                    neg = val
                    rem_neg = i
                neg = max(abs(neg), abs(val))
        if pos >= 0:
            coco -= rem_pos
            res += 1
            arr.remove(rem_pos)
        else:
            coco += rem_neg
            res -= 1
            arr.remove(rem_neg)
        final_res = max(res, final_res)
        pos, neg = -float("inf"), 0
    return final_res


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    coco = int(input())
    print(solution(arr, coco))
