def func_demo():
    # 函数体
    print("这是一个函数")


def fuc_with_params(a, b, c):
    '''
    这一个携带参数和注释的函数
    :param a:
    :param b:
    :param c:
    :return:
    '''
    print(f"传入的参数为： a={a},b={b},c={c}")

# 打印函数 comments 的内容
# print(fuc_with_params.__doc__)
# help(fuc_with_params)

# 定义空函数
def filter_char(s):
    pass

# # 调用函数
# func_demo()
# # 位置参数
# fuc_with_params(1, 2, 3)
# # 位置参数错误例子，数量错误
# fuc_with_params(1,2)

# 错误示范，默认值为空列表
def wrong_demo2(a, b, c=[]):
    c.append(a)
    c.append(b)
    print(a, b, c)

wrong_demo2(1, 2)