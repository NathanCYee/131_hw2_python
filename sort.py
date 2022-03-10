def sort_list(input_list: list) -> list:
    i: int = 0
    # bubble sort, after each loop the highest would bubble to the top and not be considered for the next loop
    while i < len(input_list):
        j: int = 0
        while j < len(input_list) - i - 1:
            if type(input_list[j]) != type(input_list[j + 1]):  # bad input, types are not equal
                return []
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
            j += 1
        i += 1
    return input_list
