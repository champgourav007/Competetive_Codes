def sol(boxes, unitsPerBox, truckSize):
    data = zip(boxes, unitsPerBox)
    listData = []
    for i,j in data:
        listData.append([i,j])
    listData.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for b,n in listData:
        box = min(b, truckSize)
        ans += box * n
        truckSize -= box
        if truckSize == 0: return ans
    return ans

if __name__ == "__main__":
    boxes = list(map(int, input().split()))
    unitsPerBox = list(map(int, input().split()))
    truckSize = int(input())
    print(sol(boxes, unitsPerBox, truckSize))