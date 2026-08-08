# def insert_student_name(name):
    # return 0

# def insert_students_age(age):
    # return 0

# def add(math,china):
    # return math+china
#刚开始没想到用字典存储，然后发现数据很乱,理清数据结构后添加数据就是字典里添加一个，否则就是一堆的无序数据
#然后发现字典的语法忘记了。
# def average()
#发现列表的语法也忘记了，忘记列表怎么添加了,我其实想用类，但类的语法细节也忘记了
# def add_student(name,age,math_score,chinese_score):
    # students.pop()
def grader(score):
    if score>=90:
        grade='A'
    elif score>=80:
        grade='B'
    elif score>=70:
        grade='C'
    elif score>=60:
        grade='D'
    else:
        grade='F'
    return grade
def printer(student):
    print("姓名:",student["name"])
    print("年龄:",student["age"])
    print("数学成绩:",student["math_score"])
    print("语文成绩:",student["chinese_score"])
    print('总成绩:',student["total_score"])
    print('平均成绩:',student["average_score"])
    print("成绩等级",student["grade"])

if __name__ =="__main__":
    students=[
        {
            "name":"张三",
            "age":18,
            "math_score":90.0,
            "chinese_score":85.0

        },
        {"name":"李四",
         "age":20,
         "math_score":78.0,
         "chinese_score":82.0
        },
        {
            "name":"",
            "age":18,
            "math_score":60.0,
            "chinese_score":65.0
             
        }
    ]
    #我怎么做到是一一对应的计算出数据呢？,我知道了我可以往字典里添加东西
    for student in students:
        student["total_score"]=student["math_score"]+student["chinese_score"]
        student["average_score"]= student["total_score"]/2
        student['grade']=grader(student["average_score"])
        print("-----------------------------")
        #我想写个输出函数，但是我不知道列表里的一项怎么写到函数的输入里，如果是类，可以把类写进入，但现在是一个列表,但是一个字典也可以直接作为输入
        printer(student)
print("--------------------------")
print("修改成绩")  
students[0]["math_score"]=95.0
student=students[0]
student["total_score"]=student["math_score"]+student["chinese_score"]
student["average_score"]= student["total_score"]/2
student['grade']=grader(student['average_score'])
print("修改后的学生信息")
printer(student)
