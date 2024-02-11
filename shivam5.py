def sol(json):
    if not json:
        return ''
    
    result = []
    multiplier = 2
    i = 0
    
    while i < len(json):
        if json[i] in ['{', '[']:
            result.append('  ' * multiplier + json[i])
            multiplier += 1
            i += 1
        elif json[i] in ['}', ']']:
            multiplier -= 1
            result.append('  ' * multiplier + json[i])
            i += 1
        elif json[i] == ',':
            result[-1]+= ','
            i += 1
        else:
            start = i
            while i < len(json) and json[i] not in ['{', '}', ',', '[', ']']:
                i += 1
            curr_s = json[start:i]
            result.append('  ' * multiplier + curr_s)
    
    for r in result:
        print(r)


if __name__ == "__main__":
    json = input()
    print(sol(json))