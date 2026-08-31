import pandas as pd
data={
    '姓名':['张三-1班','李四-2班','王五-3班','赵六-4班','李武-1班'],
    '语文':[88,92,85,89,90],
    '数学':[95,89,93,87,45],
    '英语':[92,88,90,34,23],
    '备注':['无','无','无','临时数据','临时数据']
}

df_wide=pd.DataFrame(data)
print(df_wide.drop(columns=['语文']))
print(df_wide)
df_re=df_wide.copy()
df_re['平均分']=(df_re['语文']+df_re['数学']+df_re['英语'])/3
print(df_re)
df2=df_re.assign(
    grade=lambda x :x['平均分']>=60
)
print(df2)
#lambax中的x是索引

df_split=df_wide['姓名'].str.split('-',expand=True)
print(df_split)
df_split.columns=['姓名','班级']
print(df_split)
df_result=pd.concat([df_split,df_re],axis=0)

# 创建学生成绩数据
data = {
    "姓名": ["张三", "李四", "王五", "赵六", "孙七"],
    "班级": ["一班", "一班", "二班", "二班", "一班"],
    "语文": [88, 92, 85, 90, 87],
    "数学": [95, 89, 93, 87, 91]
}

df = pd.DataFrame(data)

print("原始成绩数据：")
print(df)

# 按班级分组
grouped = df.groupby("班级")

print("\n分组对象：")
print(grouped)
# 创建包含性别的数据
data = {
    "姓名": ["张三", "李四", "王五", "赵六", "孙七"],
    "班级": ["一班", "一班", "二班", "二班", "一班"],
    "性别": ["男", "女", "男", "男", "女"],
    "语文": [88, 92, 85, 90, 87]
}

df = pd.DataFrame(data)

print("原始数据：")
print(df)

# 多列分组
grouped = df.groupby(["班级", "性别"])
print('分组',grouped)
print("\n按班级和性别分组后的语文平均分：")
print(grouped["语文"].mean())

data = {
    "姓名": ["张三", "李四", "王五", "赵六", "孙七"],
    "班级": ["一班", "一班", "二班", "二班", "一班"],
    "语文": [88, 92, 85, 90, 87],
    "数学": [95, 89, 93, 87, 91]
}

df = pd.DataFrame(data)

# 分组后统计均值
result = df.groupby('班级')[['语文','数学']].mean()

print("按班级统计平均分：")
print(result)
#分组后的显示肯定是要有统计的值的，否则这个分组没有意义，只会显示一个地址，如果有统计的值则会显示一个简单的表

data = {
    "班级": ["一班", "一班", "二班", "二班"],
    "语文": [88, 92, 85, 90],
    "数学": [95, 89, 93, 87]
}

df = pd.DataFrame(data)

result = df.groupby('班级').agg({
    '语文':['mean','max'],
    '数学':['sum','min']  
})

print("不同列不同聚合统计：")
print(result)

#时间类型开始是object，要转化为datetime
s=pd.Series(['2025-01-01',
'2025-02-15    ',
'2024-01-30'])
print(s.dtype)
s=pd.to_datetime(s)
print(s)


