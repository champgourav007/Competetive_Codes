n = int(input())
b, h = map(int, input().split())
arr = list(map(int, input().split()))
stack = []
max_vol = 0
i = 0
tot_vol = 0
for i in arr:
    tot_vol += i*b*h
stack = list()
max_vol = 0

index = 0
while index < len(arr):

    if (not stack) or (arr[stack[-1]] <= arr[index]):
        stack.append(index)
        index += 1

    else:
        
        top_of_stack = stack.pop()
        vol = (arr[top_of_stack] * ((index - stack[-1] - 1+b) if stack else index+b))*h
        max_vol = max(max_vol, vol)

while stack:
    top_of_stack = stack.pop()
    vol = (arr[top_of_stack] *((index - stack[-1] - 1 + b) if stack else index+b)) * h
    max_vol = max(max_vol, vol)
print(tot_vol - (max_vol))
