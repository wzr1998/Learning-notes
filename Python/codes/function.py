def max_min(list_arg):
    return max(list_arg), min(list_arg)


max_num, min_num = max_min(range(1, 10, 3))
print(max_num, min_num)

print("\n------------------------------------------------\n序列解包\n------------------------------------------------")


def fn(fn_num):
    return fn_num, fn_num * 2, fn_num * 3, fn_num * 4


a, b, c, d = fn(2)
print(a, b, c, d)

x, y, *z = fn(2)
print(x, y, z)

j, *q, k = fn(2)
print(j, q, k)

*l, m, n = fn(2)
print(l, m, n)

(aa, bb), [cc, dd, (ee, ff)] = (11, 22), [33, 44, (55, 66)]
print(aa, bb, cc, dd, ee, ff)
print("\n------------------------------------------------\n关键字参数\n------------------------------------------------")


def say(people, word):
    print(people + " say: " + word)


say(word="王卓然", people="卓然牛牛牛")
say(**{"people": "卓然", "word": "卓然666"})

print("\n------------------------------------------------\n默认参数\n------------------------------------------------")


def user(name, age=18, sex=1, school="HLJU"):
    print(
        "name: " + name,
        "sex: " + ("男" if sex else "女"),
        "age: " + str(age),
        "school: " + school
    )


user("王卓然")
user("然宝宝", sex=0, age=14, school="CAU")


def f(a, L=[]):
    L.append(a)
    return L, id(L)


print(f(1))
print(f(2))
print(f(3))

print("\n------------------------------------------------\n可变参数\n------------------------------------------------")


def fn_rest(a, *Arg, b=233):
    print(a, b, Arg)


fn_rest(1, 2, 3, 4, 5)
fn_rest(1, *(2, 3, 4, 5), b=666)

print([1, *[2, 3, *(4, 5)]])


def ffn(*Arg):
    sum = 0
    for num in Arg:
        sum += num ** 2
    return sum


print("求平方和：", end="")
print(ffn(1, 2, 3, 4))

print("\n------------------------------------------------\n可变关键字参数\n------------------------------------------------")


def fn_dict(param, *param_tuple, **param_dict):
    print(param, param_tuple, end="：")
    for key, value in param_dict.items():
        print(key + ":" + value, end=",")


fn_dict("王卓然", "敲", "喜", "欢", fruit="大橘子", drinks="快乐水", activity="吃吃喝喝玩玩睡睡")

print("\n------------------------------------------------\nglobal关键字\n------------------------------------------------")


def fn_global(i):
    global global_num
    global_num = 1
    global_num += i


fn_global(2)
print(global_num)

print(
    "\n------------------------------------------------\nnonlocal关键字\n------------------------------------------------")


def outer_fn(i):
    sum_num = i

    def inner_fn(j):
        nonlocal sum_num
        sum_num += j
        print(sum_num)

    inner_fn(2)


outer_fn(1)

print("\n------------------------------------------------\n闭包\n------------------------------------------------")


def add_create(total):
    def add(current):
        nonlocal total
        total += current
        return {"data": total, "add": add}

    return add


print(add_create(1)(2)["add"](3)["add"](4)["add"](5)["data"])


def add_create(total):
    def add(current):
        nonlocal total
        total += current
        return total

    return add


add = add_create(1)
print(add(2), add(3), add(4), add(5))


def outer_fn(num1):
    def inner_fn(num2):
        nonlocal num1
        num1 += num2
        return num1

    return inner_fn


inner_fn = outer_fn(1)
print(inner_fn(2), inner_fn(3), inner_fn(4))


def hello_create(name):
    def say_hello(text):
        print("{}说：{}".format(name, text))

    return say_hello


wzr_say = hello_create("王卓然")
wzr_say("今天也要加油鸭！")
wzr_say("今晚敲冷哒！")
rbb_say = hello_create("然宝宝")
rbb_say("又是开心的一天！")
rbb_say("然宝宝要征服全世界！")
print(wzr_say.__code__.co_freevars[0])
print(wzr_say.__closure__[0].cell_contents)

print("\n------------------------------------------------\n装饰器\n------------------------------------------------")

import time


def decorator_fn(func):
    t1 = time.time()

    def inner_fn(*Arg, **kwargs):
        return func(*Arg, **kwargs)

    t2 = time.time()
    print("函数用时：", t2 - t1)
    return inner_fn


@decorator_fn
def factorial_fn(n):
    # return reduce(lambda factorial, cur: factorial*cur, range(1, n+1), 1)
    return 1 if not n - 1 else n * factorial_fn(n - 1)


print(factorial_fn(50))

print("\n------------------------------------------------\n含参装饰器\n------------------------------------------------")


def decorator(param):
    def decorator_fn(func):
        def inner_fn(*args, **kwargs):
            return func(*args, **kwargs)

        return inner_fn

    return decorator_fn


@decorator(param=1)
def fn():
    pass


fn()
