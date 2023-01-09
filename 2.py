def first_non_repeating_letter(string):
    a = string.upper()
    for elem in list(a):
        if a.count(elem) == 1:  return string[a.find(elem)]
    return ''

if __name__ == '__main__':
    print("first_non_repeating_letter('abababalamaga') -> ", first_non_repeating_letter('abababalamaga'))
