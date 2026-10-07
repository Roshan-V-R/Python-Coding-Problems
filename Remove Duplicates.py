#Given an integer array nums sorted in non-decreasing order (e.g., [1, 1, 2, 3, 3, 4]),
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements must be kept the same.
#Return the number of unique elements (let's call it k).
# The first k elements of nums should hold the final unique result.
def remove_duplicates(nums):
    w = 0
    for r in range(1,len(nums)):
        if nums[r] != nums[w]:
            w += 1
            nums[w] = nums[r]
    print("Unique: ",w + 1)
    print("Number list: ",nums[:w+1])

remove_duplicates([1, 1, 2, 3, 3, 4])

