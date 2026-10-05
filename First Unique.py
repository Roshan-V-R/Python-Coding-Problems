#Write a function first_unique(nums) that returns the first number that appears exactly once.
# If none exists, return None.
def first_unique(nums):
    frequency = {}
    for i in nums:
        if i not in frequency:
            frequency[i]=1
        else:
            frequency[i]+=1
    for i in nums:
        if frequency[i] == 1:
            return i
    else:
        return None

print(first_unique([7]))