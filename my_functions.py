def pyramid_num(rows):
    """prints half pyramid of numbers. Rows are the argument"""
    x = 1
    for i in range(0, rows):
        for d in range(0, i+1):
            print(x, end=" ")
            x = x + 1
        print()


def stars_pyramid(rows):
    """prints half pyramid of stars. Rows are the argument"""
    i = 1
    while i < rows + 1:
        print("*" * int(i))
        i += 1


def full_pyramid(rows):
    """prints full pyramid of stars. Rows are the argument"""
    m = 2 * rows - 2
    for i in range(0, rows):
        for x in range(0, m):
            print(end=" ")
        m -= 1
        for f in range(0, i+1):
            print("*", end=" ")
        print("\r")
