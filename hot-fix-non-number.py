def sum_of_list_fixed(l):
    total = 0
    for val in l:
        if val.isnumeric():
            total = total + val
        else:
            pass
    return total 