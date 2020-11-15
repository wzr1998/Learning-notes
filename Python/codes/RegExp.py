import re

string = "1|11|111|1111|11111"
str_list = [
    18946110350,
    18946110351,
    1894611030,
    28946110350,
]

print(re.findall("\d{2,4}", string))

for str1 in str_list:
    print(re.findall("1\d{6}0350$", str(str1)), not not str1)

str_nums = "3627a949bbc0455js0537499py54171go152c++7854"


def convert(value):
    return str(0 if int(value.group()) < 5 else 1)


print(re.sub('\d', convert, str_nums))
print(re.sub('[a-z+]+', '|', str_nums))



# str22 = "11111222223333344444"
# print(re.findall("\d(\d)\d", str22))
#
# def convert1(value):
#     print(value.group(2))
#     #return str(0 if int(value.group()) < 5 else 1)
#     return "#"
# print(re.sub('\d(\d(\d)\d)\d', convert1, str22))


str22 = "1181011228202233830334484044"
print(re.findall("\d((\d)8(\d))0(\d)\d", str22))

def convert1(value):
    print(value.group(0, 1, 2), value.span(1))
    return "#"
print(re.sub('\d((\d)8(\d))0(\d)\d', convert1, str22))

