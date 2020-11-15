from enum import Enum, auto


# import enum
class Color(Enum):
    RED = 1#auto()
    GREEN = 1#auto()
    BLUE = 2#auto()


for item in Color.__members__:
    print(item, type(item),  end=" | ")

print()

for item in Color:
    print(item, end=" | ")

print()

print(type(Color.__members__), Color(1))

# print(Color.BLUE, Color.BLUE.name, Color.BLUE.value)
from enum import Enum, unique

# @unique
# class Color1(Enum):
#     RED = 1
#     GREEN = 1
#     BLUE = 2

