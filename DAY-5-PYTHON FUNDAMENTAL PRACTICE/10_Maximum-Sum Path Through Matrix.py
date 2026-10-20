matrix = [
    [1, 3, 3],
    [1, 3, 1],
    [2, 5, 2],
    [4, 2, 1]
]

rows = len(matrix)
cols = len(matrix[0])

dp = [[0] * cols for _ in range(rows)]
path = [[None] * cols for _ in range(rows)]

dp[0][0] = matrix[0][0]

for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:
            continue

        if i == 0:
            dp[i][j] = dp[i][j - 1] + matrix[i][j]
            path[i][j] = (i, j - 1)

        elif j == 0:
            dp[i][j] = dp[i - 1][j] + matrix[i][j]
            path[i][j] = (i - 1, j)

        elif dp[i - 1][j] > dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j] + matrix[i][j]
            path[i][j] = (i - 1, j)

        else:
            dp[i][j] = dp[i][j - 1] + matrix[i][j]
            path[i][j] = (i, j - 1)

i = rows - 1
j = cols - 1
result = []

while True:
    result.append(matrix[i][j])

    if i == 0 and j == 0:
        break

    i, j = path[i][j]

result.reverse()

print("Maximum path sum:", dp[rows - 1][cols - 1])
print("Path:", result)