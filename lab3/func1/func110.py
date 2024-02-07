def unique_elements(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

original_list = input()
unique_list = unique_elements(original_list)
print(unique_list)
