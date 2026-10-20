sales = [10, 20, 30, 40, 50, 60]
k = 3

averages = []

for i in range(len(sales) - k + 1):
    total = 0

    for j in range(i, i + k):
        total += sales[j]

    averages.append(round(total / k, 2))

print("Window averages:", averages)