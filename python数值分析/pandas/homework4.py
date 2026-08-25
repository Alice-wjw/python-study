import pandas as pd
# 1. 数据读取与合并
# - 读取两个 CSV 文件
dfusr=pd.read_csv('user_info.csv',encoding='utf-8')
dfsale=pd.read_csv('sales_data.csv',encoding='utf-8')
# - 使用 merge() 按“学号”进行数据合并
df_total=pd.merge(
    dfusr,
    dfsale,
    on='学号',
    how='inner'
)
print(df_total)
# df_copy['日期']=df_copy['日期'].dt.weekday
# 2. 数据清洗与转换
# 完成以下数据处理：
# - 日期转换为 datetime 类型
df_total['日期']=pd.to_datetime(df_total['日期'])
print(df_total['日期'].dtype)
# - 提取月份信息
df_total['月份']=df_total['日期'].dt.month
print(df_total)
# - 删除销售额为空的数据
#你需要重新赋值一次
#这部分错了df_total.dropna()
df_total=df_total.dropna(subset=['销售额'])
# 3. 数据分箱
# 根据销售额进行订单等级划分：
df_cut=pd.cut(
    df_total['销售额'],
    bins=[0,100,500,2000],

    labels=['普通','优质','至尊']
)
#这没意义啊
df_total['订单等级']=pd.cut(
    df_total['销售额'],
    bins=[0,100,500,2000],
    
    labels=['普通','优质','至尊']
)
print(df_total[['销售额','订单等级']].head() )
# 4. 分组聚类
# - 按所属校区统计：
#   - 总销售额
#   - 平均销售额
df=df_total.groupby('所属校区')
print('总销售额',df['销售额'].sum())
print('平均销售额',df['销售额'].mean())
# - 创建数据透视表：
#   - 行索引：月份
#   - 列索引：类别
#   - 值：销售额总和
pivot=pd.pivot_table(
    data=df_total,
    index='日期',
    columns='类别',
    values='销售额',
    aggfunc='sum'
)
print(pivot)
# 5. 时间序列统计
# 完成以下操作：
# - 将日期设置为索引
df_total.index=df_total['日期']
print(df_total)
df_total=df_total.sort_index()
# - 按周统计销售额总和
weekly=df_total['销售额'].resample('W').sum()
print(weekly)
# - 观察销售趋势变化
# 要求使用 resample()
print()
# 6. 结果导出
# 将最终分析结果导出：Q1_Analysis_Report.csv
# 要求：
# - 不保留行索引
# - 使用 utf-8-sig 编码
df_total.to_csv(
    path_or_buf='Q1_Analysis_Report.csv',
    index=False,
    encoding='utf-8-sig'
)