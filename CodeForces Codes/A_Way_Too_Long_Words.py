lines = int(input())
while lines > 0:
    sent = input()
    leng_sent = len(sent)
    if leng_sent > 10:
        first = sent[0]
        last = sent[-1]
        i = 1
        j = leng_sent - 1
        size = 0
        while i < j:
            size += 1
            i+=1
        new_word = first + str(size) + last
        print(new_word)
    else:
        print(sent)
    lines -= 1