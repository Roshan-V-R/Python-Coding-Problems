#1. Sum of even numbers
def sum_of_evens(nums):
    sum = 0
    for i in nums:
        if i % 2 == 0:
            sum+=i
    return sum

print(sum_of_evens([1,2,3,4,5,6]))

#2. Count of items in dictionaries
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = {}
for fruit in fruits:
    if fruit not in count:
        count[fruit] = 1
    else:
        count[fruit]+=1
print(count)

#3. Write a function remove_duplicates(nums) that takes
# a list of integers and returns a new list with duplicates
# removed while preserving the original order of first occurrence.

def remove_duplicates(nums):
    new_list = []
    new_set = set()
    for i in nums:
        if i not in new_set:
            new_list.append(i)
            new_set.add(i)
    return new_list

print(remove_duplicates([4, 3, 2, 3, 1, 4, 3]))

