matrix = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)
initial = [[1 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        if matrix[i][j] % 2:
            initial[i][j] = 1 - initial[i][j]
            if i > 0:
                initial[i-1][j] = 1 - initial[i-1][j]
            if i < 2:
                initial[i+1][j] = 1 - initial[i+1][j]
            if j > 0:
                initial[i][j-1] = 1 - initial[i][j-1]
            if j < 2:
                initial[i][j+1] = 1 - initial[i][j+1]
for i in range(3):
    for j in range(3):
        print(initial[i][j], end="")
    print()