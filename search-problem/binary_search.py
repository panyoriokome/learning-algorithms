def binary_search(nums: list, item:int):
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

nums = [1, 3, 5, 7, 9]
print(binary_search(nums, 3))
print(binary_search(nums, 1))
print(binary_search(nums, 9))
print(binary_search(nums, 4))