import pandas as pd
vall=[10,20,30,40,50]
s1=pd.Series(vall)
print(s1)
print(type(s1))
val2=['苹果','香蕉','橙子','葡萄']
index2=['水果1','水果2','水果3','水果4']
s2=pd.Series(val2,index=index2)
print(s2)
dic1={'姓名':'张三','年龄':20,'性别':'男','成绩':95}
s3=pd.Series(dic1)
print(s3)
print(s2.index)
print(type(s2.index))
print(s2.values)
print(type(s2.values))
data1=[['张三',20,'男',98],['李四',19,'女',92]]
d=['姓名','年龄','性别','成绩']
c=pd.DataFrame(data1,columns=d)
print(c)
s=pd.Series([10,20,30,40,50])
print(s.sum())
print(s.mean())
print(s.max())
print(s.min())
print(s.std())
print(s.var())
print(s.median())
print(s.count())
s=pd.Series([88,95,76],index=['张三','李四','王五'])

print(s.sort_values())
print(s.sort_values(ascending=False))

print(s.sort_index())

s = pd.Series([1, 2, 2, 3, 3, 3])

print("唯一值：", s.unique())
print("唯一值个数：", s.nunique())

print("\n删除重复值：")
print(s.drop_duplicates())

s = pd.Series(["苹果", "香蕉", "苹果", "橙子", "苹果"])

print("统计每个元素出现次数：")
print(s.value_counts())

