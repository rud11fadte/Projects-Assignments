
def table(n, m, o):
    for t in range(1, (10 + 1)):
        print(str(n) + "*" + str(t) + "=" + str(n * t) + "\t|\t" +
              str(m) + "*" + str(t) + "=" + str(m * t) + "\t|\t" +
              str(o) + "*" + str(t) + "=" + str(o * t))

table(1, 2, 3)
print(" ")

# Pattern increase in each line
def loops(t, l):
    for i in range(t):
        for j in range(0, i + 1):
            print(l, end="")
        print("")

loops(5, 1)
print()

# Pattern X
def sym(t):
    for i in range(t):
        for j in range(i + 1):
            print("*", end="")
        print("")
    for i in range(t):
        for j in range(t - i - 1):
            print("*", end="")
        print("")

sym(5)

# Check if matrix
def isMatrix(L):
    if not isinstance(L, list):
        return False
    row_length = len(L[0])
    for i in L:
        if not isinstance(i, list):
            return False
        if len(i) != row_length:
            return False
    return True

print(isMatrix([[2, 3, 6, 7], [7, 2, 0, 9]]))