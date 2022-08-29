class Human(object):
    """
    人类
    """
    message = '这是类属性'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("这是构造方法")


person = Human("哈利波特", 12)

print(person.message)