# Question 1
#Using the given list, print out a filtered version of the list with only the numbers that are less than ten.
alist = [1,11,14,5,8,9]

alist = [1, 11, 14, 5, 8, 9]
filtered_list = [num for num in alist if num < 10]
print(filtered_list)

# Question 2
#Merge and sort the two lists below
#Hint: You can use the .sort() method
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

l_1 = [1, 2, 3, 4, 5, 6]
l_2 = [3, 4, 5, 6, 7, 8, 10]

merged_list = l_1 + l_2
merged_list.sort()

print(merged_list)

# Question 3
# Square every number from 1 to 15

squared_numbers = [num**2 for num in range(1, 16)]
print(squared_numbers)

# Question 4
#Using List Comprehension and the given list, print out a filtered list with only the names that start with the letter 'a'. The names in the outputted list should be title cased and have no whitespace.
names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
#expected output = ['Amy', 'Alex']

names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']

filtered_list = [name.strip().title() for name in names_list if name.strip().lower().startswith('a')]
print(filtered_list)

# Question 5
# Print all Prime numbers from 1 to 100

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in range(1, 101) if is_prime(num)]
print(prime_numbers)