# a
def print_triangle(n):
    if n > 0:

        print_triangle(n - 1)

        print("*" * n)


# b
def print_opposite_triangles(n):
    asterisk = "*"
    if (n == 0):
        return None

    print(asterisk * n)

    print_opposite_triangles(n - 1)
    print(asterisk * n)

#c
def print_ruler(n):
    string = "-"
    if (n == 0):
        return None

    print_ruler(n - 1)

    print(string * n)

    print_ruler(n - 1)