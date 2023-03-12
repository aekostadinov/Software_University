def print_row(n, r):
    for space in range(n - r):
        print(" ", end="")
    for star in range(1, r):
        print("*", end=" ")
    print("*")


def print_up(n):
    for r in range(1, n + 1):
        print_row(n, r)


def print_bottom(n):
    for r in range(n - 1, 0, -1):
        print_row(n, r)


def print_rhombus(n):
    print_up(n)
    print_bottom(n)


n = int(input())
print_rhombus(n)
