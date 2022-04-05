def counter():
    cnt = [0]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


num1 = counter()
print(num1())
print(num1())
print(num1())
print(num1())


def counter(FIRST=0):
    cnt = [FIRST]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


num5 = counter(5)
num10 = counter(10)

print(num5())
print(num5())
print(num10())
print(num10())
