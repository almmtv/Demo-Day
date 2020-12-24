n = int(input())
table = []
for i in range(n):
    table += [[int(i) for i in input().split()[1:]]]
q = int(input())
output = []
for i in range(q):
    x, y = [int(i) for i in input().split()]
    try:
        output += [table[x - 1][y - 1]]
    except IndexError:
        output += ['ОШИБКА!']
for i in output:
    print(i)
