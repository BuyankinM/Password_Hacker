def squares(nn):
    for i in range(1, nn + 1):
        yield i ** 2


n = int(input())
for val in squares(n):
    print(val)
