from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]


nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

print(top_k_frequent(nums, k))