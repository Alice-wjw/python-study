from student import Student
Students=[Student('张三',18,90.0,85.0),
              Student('李四',19,78.0,82.0),
              Student('王五',18,60.0,65.0)]
#列表添加又忘记了,是append，还有remove，pop等用法
def add(name,age,math_score,chinese_score):
    s=Student(name,age,math_score,chinese_score)  
    Students.append(s)
def delete(name):
    for student in Students:
        if student.name==name:
            Students.remove(student)
def change(name,key,value):
    for student in Students:
        if student.name==name:
            if key=='age':
                student.age=value
            elif key=='chinese_score':
                student.chinese_score==value
            elif key=='math_score':
                student.math_score==value
def search(name):
    for student in Students:
        if student.name==name:
            student.printer()
def allshow():
    for i in Students:
        i.printer()

