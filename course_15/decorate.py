# def hogwarts():
#     print("霍格沃滋测试学院")

#
import datetime


def timer(func):
    def inner():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print(f"函数的执行时间{end_time-start_time}")
    return inner

@timer
def hogwarts():
    print("霍格沃滋")

hogwarts()