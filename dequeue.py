from collections import deque

res = deque()
final = []


def solve(user_input):
    fun = user_input.split(" ")
    if fun[0] == "PUSH":
        val = fun[1]
        res.append(val)
    elif fun[0] == "POP":
        try:
            final.append(res.pop())
        except:
            final.append("Empty")
    elif fun[0] == "INJECT":
        val = fun[1]
        res.appendleft(val)
    elif fun[0] == "EJECT":
        try:
            res.popleft()
        except:
            pass
    else:
        print(*final)
        raise EOFError


if __name__ == "__main__":
    for _ in range(8):
        try:
            user_string = input()
            solve(user_string)
        except EOFError:
            break
