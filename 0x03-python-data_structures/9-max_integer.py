#!/urs/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    great = 0
    for n in my_list:
        great = great if great > n else n
    return great
