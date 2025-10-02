m = input("Enter the word: ")

length = len(m)
if length % 2 == 1:
    middle_index = length // 2
    print(m[middle_index])
else:
    first_middle_index = length // 2 - 1
    second_middle_index = length // 2
    print(m[first_middle_index:second_middle_index + 1])