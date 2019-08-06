def removeDuplicates(nums: [int]) -> int:
    length = len(nums)
    if length == 0:
        return 0

    stack = []
    stack.append(nums[0])

    for element in nums[1:length]:
        if element == stack[-1]:
            nums.remove(element)
        else:
            stack.append(element)

    print(len(nums))
    print(nums)


nums = [1, 1, 2, 2, 3, 3, 3, 4, 5]
removeDuplicates(nums)
