def common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))


arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

print("Common Elements:", common_elements(arr1, arr2))