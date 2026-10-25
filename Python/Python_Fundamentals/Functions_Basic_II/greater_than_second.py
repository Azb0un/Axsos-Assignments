def values_greater_than_second(my_list):
    if len(my_list) < 2:
        return False

    second = my_list[1]
    new_list = []

    for value in my_list:
        if value > second:
            new_list.append(value)

    print(len(new_list))
    return new_list

print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))