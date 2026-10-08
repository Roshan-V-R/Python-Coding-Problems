#Given an array nums and an integer k,
# return the maximum sum of any contiguous subarray of length k.
def max_sub_array_of_size_k(k,nums):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for r in range(k,len(nums)):
        window_sum += nums[r] - nums[r-k]
        max_sum = max(max_sum,window_sum)
    return max_sum
print(max_sub_array_of_size_k(3,[2, 1, 5, 1, 3, 2]))