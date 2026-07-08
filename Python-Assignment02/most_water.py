def max_water(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height

        max_area = max(max_area, area)

        # Move the pointer with the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Input
height = list(map(int, input("Enter heights separated by spaces: ").split()))

# Output
print("Maximum Water:", max_water(height))