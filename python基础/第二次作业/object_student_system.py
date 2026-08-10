class Student:
    def __init__(self,name,age,math_score,chinese_score):
        self.name=name
        self.age=age
        self.math_score=math_score
        self.chinese_score=chinese_score
    def totalr(self):
        self.total= self.chinese_score+self.math_score
        return self.total
    def averager(self):
        self.average= (self.chinese_score+self.math_score)/2
        return self.average
    def grader(self):
        score=self.averager()
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
    def printer(self):
          self.totalr()
          self.averager()
          self.grader()
          print(f'姓名：{self.name}')
          print(f'年龄：{self.age}')
          print(f'数学成绩：{self.math_score}')
          print(f'语文成绩：{self.chinese_score}')
          print(f'总成绩:{self.total}')
          print(f'平均成绩:{self.average}')
          print(f'成绩等级:{self.grader()}')

    def changer(self,flag,value):
        if flag=="姓名":
              self.name=value
if __name__=='__main__':
      
# Student()
# list=[Student,Student]
# list[0]
    Students=[Student('张三',18,90.0,85.0),
              Student('李四',19,78.0,82.0),
              Student('王五',18,60.0,65.0)
                              
                        ]
    for student in Students:
        student.printer()        
#修改成绩还是很难做到啊，这个列表我怎么才能直接改它？
#score打错了，debug发现了
print('---------------')
print('修改学生成绩')
Students[0].math_score=95.0

print('修改后的学生信息：')
Students[0].printer()
        