def lin_search(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return -1
