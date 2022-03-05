def sort_list(input_list: list) -> list:
    i: int = 0
    while i < len(input_list):
        j: int = 0
        while j < len(input_list) - i - 1:
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
            j += 1
        i += 1
    return input_list


print(sort_list([1, 3, 2, 7]))
print(sort_list([3, 2, 4, 89]))
