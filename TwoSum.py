#Brute force Method
nums = [11, 7, 2, 15]
target = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print([i,j])

#Hash method
def two_sum(nums,target):
    seen = {}
    for r in range(len(nums)):
        num = nums[r]
        complement = target - num
        if complement in seen:
            return [seen[complement],r]
        seen[num] = r
print(two_sum([2, 7, 11, 15], 9))