def get_largest_element(list_):
    if list_ != []:
        list_ = list(list_)
        largest_element = list_[0]
        for element in list_:
            if element > largest_element:
                largest_element = element
        return largest_element


def get_smallest_element(list_):
    if list_ != []:
        list_ = list(list_)
        smallest_element = list_[0]
        for element in list_:
            if element < smallest_element:
                smallest_element = element
        return smallest_element


def get_sorted_list(list_, desc=False):

    sorted_list = []
    copied_list = list(list_)

    if desc is False:
        while len(copied_list) > 0:
            for element in copied_list:
                element_to_add = get_smallest_element(copied_list)
                sorted_list.append(element_to_add)
                copied_list.remove(element_to_add)
        return sorted_list

    elif desc is True:
        while len(copied_list) > 0:
            for element in copied_list:
                element_to_add = get_largest_element(copied_list)
                sorted_list.append(element_to_add)
                copied_list.remove(element_to_add)
        return sorted_list


a = {3, 5, 6, 1, 2, 8, 7, 9, 4}

print(get_largest_element(a))
print(get_smallest_element(a))

print(get_sorted_list(a, True))