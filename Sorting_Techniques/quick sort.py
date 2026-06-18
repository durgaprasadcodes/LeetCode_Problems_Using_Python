def quick_sort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)

        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


nums = [4, 3, 5, 2, 6, 7, 8, 1]
quick_sort(nums, 0, len(nums) - 1)
print(nums)