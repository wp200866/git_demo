# magicains = ['alice', 'david', 'carolina']
# for magicain in magicains:
#     print(magicain)
#
# for magicain in magicains:
#     print(f'{magicain.title()}, thant was a great trick!')
#
# digits = []
# for i in range(0, 10000):
#     digits.append(i)
# print(digits)
# print(min(digits))
# print(max(digits))
# print(sum(digits))
#
# squares = [value**2 for value in range(1, 10)]
# print(squares)

# for i in range(1, 21):
#     print(i)

# squares = [value for value in range(1, 1000001)]
# print(max(squares))
# print(min(squares))
# print(sum(squares))
# # for square in squares:
# #     print(square)
#
# squares_j = [value_1 for value_1 in range(1, 20, 1)]
# print(squares_j)
# for square in squares_j:
#     print(square)

# squares = []
# for i in range(3, 31):
#     if i % 3 == 0:
#         squares.append(i)
# print(squares)

# squares = [value**3 for value in range(1, 11)]
# print(squares)

import math
#
# def circle_area(r):
#     result = math.pi*r*r
#     return result
#
# r = 10
result = lambda r : math.pi*r**2
print(result)
# print(f'半径为{r}的圆的面积为{circle_area(r)}')
# print(f'半径为{r}的圆的面积为{result(r)}')

book_info = [
    ("python", 22.5),
    ("java", 20),
    ("软件测试", 25)
]



book_info.sort(key= lambda x:x[1])
print(key)

