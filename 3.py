def digital_root(number):
    root = sum(map(int, str(number)))
    print(root)
    if len(str(root)) == 1: 
        return root
    else: 
        return digital_root(root)

if __name__ == '__main__':
    print("digital_root(12345) -> ", digital_root(12345))