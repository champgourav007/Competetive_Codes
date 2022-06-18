if __name__ == "__main__":
    n = int(input())
    ele = list(map(str, input().split()))
    emotion = list(map(str, input().split()))
    em_d = {"Happy":10,"Sad":5,"Neutral":2,"None":1}
    digits = []
    for i in ele:
        val = ""
        for j in i:
            try:
                d = int(j)
                val += j
            except:
                break
        digits.append(int(val))
    print(digits)