#Write a function most_frequent(nums) that returns the number that appears most frequently in the list.
def most_frequent(nums):
    frequency = {}
    max_count = 0
    answer = None
    for i in nums:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i]+=1

    for i in nums:
        if frequency[i] > max_count:
            max_count = frequency[i]
            answer = i

    return answer
print(most_frequent([7]))