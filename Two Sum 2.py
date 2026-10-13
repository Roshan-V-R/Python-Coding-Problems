def two_sum(nums,target):
    l = 0
    r = len(nums) - 1
    while l < r:
        current_sum = nums[l] + nums[r]
        if current_sum == target:
            return [l+1, r+1]
        elif current_sum < target:
            l+=1
        else:
            r-=1
print(two_sum([2, 7, 11, 15], 18))