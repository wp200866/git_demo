"""
闭包函数： 霍格沃滋开学啦，要求打印每个学生的姓名、性别、年级
"""
name = "哈利"
gender = "男生"
grade = 1
#
# def output_students(name, gender, grade=1):
#     print(f"霍格沃滋开学啦，学生名称是{name}, 性别是{gender}, 年龄是{grade}")
#
# output_students("哈利", "男生", 1)
# output_students("罗恩", "男生", 1)
# output_students("赫敏", "女生", 1)

def students_grade(grade):
    def output_students(name, gender):
        print(f"霍格沃滋开学啦，学生名称是{name}, 性别是{gender}, 年龄是{grade}")
