print("\n-------------------------------------------\nlambda 匿名函数：\n-------------------------------------------")
print((lambda a: print(2 * a, end=","))(3))

print([y for y in range(1, 30, 3)])
# print(y * y for y in range(10))

fn_lambda = lambda x, y: x + y
print(fn_lambda(1, 2))

print("\n------------------------------------------------\nmap\n------------------------------------------------")
num_list1 = [1, 2, 3, 4, 5]
num_list2 = (6, 7, 8, 9)
result_list = map(lambda i, j: i + j, num_list1, num_list2)
print(list(result_list))

print("\n------------------------------------------------\nreduce\n------------------------------------------------")
from functools import reduce

reduce_result = reduce(lambda result, current: result + current * 2, [1, 2, 3, 4], 0)
print(reduce_result)

print("\n------------------------------------------------\nfilter\n------------------------------------------------")
num_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
filter_result = filter(lambda i: 3 <= i <= 7, num_list)
print(list(filter_result))

print(
    "\n-------------------------------------------\nlist comprehension\n-------------------------------------------")

list_origin = [1, 2, 3, 4, 5, 6]
list_square = [i ** 2 for i in list_origin]
# 有选择性的筛选
list_square_filter = [i ** 2 for i in list_origin if i % 2 == 0]
max_list_item = max(i ** 2 for i in list_origin)
print(list_square)
print(list_square_filter)
print(max_list_item)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

list_matrix_item = [item for row in matrix for item in row]
print(list_matrix_item)

dict_age_origin = {"LiHua": 20, "XiaoMing": 16, "XiaoHong": 22, "WZR": 18, "RanBB": 14}
list_minors = [name for name, age in dict_age_origin.items() if age < 18]
dict_minors = {name: age for name, age in dict_age_origin.items() if age < 18}
print(list_minors)
print(dict_minors)
