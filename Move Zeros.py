#Write a function move_zeros(nums) that moves all zeros to the end of the list while
# preserving the relative order of the non-zero elements.
def move_zeros(nums):
    zeros = []
    non_zeros = []
    for i in nums:
        if i == 0:
            zeros.append(i)
        else:
            non_zeros.append(i)
    non_zeros.extend(zeros)
    return non_zeros

print(move_zeros([0, 1, 0, 3, 12]))

#Two Pointer Method
nums = [0, 1, 0, 3, 12]
w = 0
for i in nums:
    if i != 0:
        nums[w] = i
        w+=1
print(nums)
for i in range(w,len(nums)):
    nums[i] = 0
    w+=1
print(nums)

#Swap Method
nums = [1,2,3]
w = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[w],nums[i] = nums[i],nums[w]
        w+=1
print(nums)
