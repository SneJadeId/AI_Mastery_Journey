def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

    return []


nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

print(two_sum(nums, target))