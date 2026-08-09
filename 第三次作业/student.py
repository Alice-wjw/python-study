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

   