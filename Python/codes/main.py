list1 = ["1", "2", "3"]
for i, v in enumerate(list1):
    print("%d, %s" % (i, v))

print('----------------------------------------')

list_num = [1, 2, 3]
print(
    list_num.append(2), list_num, '\n',
    list_num.extend([1, 2, 3]), list_num, '\n',
    list_num.insert(2, 2), list_num, '\n',
)

print('----------------------------------------')

list2 = [1, 2, 3]
for i, v in enumerate(list2):
    print(i, v)

print('----------------------------------------')

list1 = (1,)
list2 = (1,)
print(list1 is list2)

print('----------------------------------------')

a = 1.1
b = 1
if a <= b:
    print('a<=b')
else:
    print("a>b")

print('----------------------------------------')
# user = 'wzr'
# password = '123'
# print('请输入用户名：')
# in_user = input()
# print('请输入密码：')
# in_password = input()
# if in_user == user and in_password == password:
#     print("登录成功")
# else:
#     print("登录失败")

print('----------------------------------------')
print("请输入成绩")
score = int(input())
if score > 100:
    print("输入错误")
elif 90 <= score <= 100:
    print("优秀")
elif 80 <= score < 90:
    print("良好")
elif 60 <= score < 80:
    print("及格")
else:
    print("不及格")
print('----------------------------------------')
count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("count=3")
print('----------------------------------------')
for_list = [[1, 2, 3], [4, 5]]
for item in for_list:
    for num in item:
        if num == 5:
            continue
        print(num)
else:
    print("循环结束")

print('----------------------------------------')
for i in range(0, 10, 2):
    print(i, end='|')
print('----------------------------------------')
for_list2 = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in for_list2:
#     if i % 2 - 1:
#         print(i)

# for i in range(1, len(for_list2), 2):
#     print(for_list2[i])

for i in for_list2[1: len(for_list2): 2]:
    print(i)
