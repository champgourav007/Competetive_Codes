user_name = input()
new_lst = []
for i in user_name:
    if i not in new_lst:
        new_lst.append(i)
        
if len(new_lst)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")