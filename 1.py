def filter_list(my_list):
    return [elem for elem in my_list if type(elem) == int]  

if __name__ == '__main__':
    print("filter_list([1, 2, 'a', 'aas14', 7]) -> ", filter_list([1, 2, 'a', 'aas14', 7]))
