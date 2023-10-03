#Сортировка пузырьком
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

random_list = [5, 2, 4, 6, 1, 3]
bubble_sort(random_list)
print(random_list)

# Результат:
# [1, 2, 3, 4, 5, 6]
