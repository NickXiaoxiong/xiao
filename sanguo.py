# 读取人物名称

f = open('name.txt')
data = f.read()
print(data.split('|'))

# # 读取兵器名称
# f2 = open('weapon.txt')
# # data2 = f2.read()
# i = 1
# for line in f2.readlines():
#     if i % 2 == 1:
#         print(line.split('\n'))
#     i += 1
#
# f3 = open('sanguo.txt')
# print(f3.read().replace('\n',''))

def func(filename):
    print(open('name.txt').read())
    print('test func')

func('name.txt')
