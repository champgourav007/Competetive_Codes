def sol(url):
    query = url.split("?")[1]
    all_params = query.split("&")
    all_params_dict = {}
    for i in all_params:
        v = i.split("=")
        all_params_dict[v[0]] = v[1]
    return all_params_dict

if __name__ == "__main__":
    url = input()
    all_params_dict = sol(url)
    t = int(input())
    for _ in range(t):
        params = input()
        if all_params_dict.get(params):
            print(all_params_dict[params])
        else:
            print("-1")
        