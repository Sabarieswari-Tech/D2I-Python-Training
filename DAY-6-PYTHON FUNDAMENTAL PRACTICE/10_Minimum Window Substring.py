s = 'ADOBECODEBANC'
t = 'ABC'

need = {}

for char in t:
    need[char] = need.get(char, 0) + 1

window = {}
left = 0
right = 0
formed = 0
required = len(need)

min_length = float('inf')
min_start = 0

while right < len(s):
    char = s[right]
    window[char] = window.get(char, 0) + 1

    if char in need and window[char] == need[char]:
        formed += 1

    while formed == required:
        if right - left + 1 < min_length:
            min_length = right - left + 1
            min_start = left

        left_char = s[left]
        window[left_char] -= 1

        if left_char in need and window[left_char] < need[left_char]:
            formed -= 1

        left += 1

    right += 1

if min_length == float('inf'):
    result = ''
else:
    result = s[min_start:min_start + min_length]

print("Minimum window:", result)