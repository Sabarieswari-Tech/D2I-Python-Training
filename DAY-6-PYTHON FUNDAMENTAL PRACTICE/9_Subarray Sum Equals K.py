nums = [1, 1, 1]
k = 2

count = 0
prefix_sum = 0
frequency = {0: 1}

for num in nums:
    prefix_sum += num

    if prefix_sum - k in frequency:
        count += frequency[prefix_sum - k]

    frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

print("Count:", count)