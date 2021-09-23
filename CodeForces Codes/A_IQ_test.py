ran = int(input())
lst = list(map(int,input().split()))
diff_lst = []
i = 1
while i < len(lst):
    j = i-1
    diff_lst.append(abs(lst[i] - lst[j]))
    i+=1
print(diff_lst)