import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split#数据集划分
from sklearn.preprocessing import StandardScaler#归一化
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import r2_score
df=pd.read_excel('homeprice.xlsx')
df.columns=['No','TransDate','Houseage','DistMRT','Numstores','latitude','lontitude','price']
df.drop(['No'],axis=1,inplace=True)
print('原始数据集形状',df.shape)#没写
print('缺失值',df.isnull().sum())#没写
print('基本统计量：',df.describe().round(2))#没写

#预处理
#2.1异常值处理
Q1=df['price'].quantile(0.25)
Q3=df['price'].quantile(0.75)
IQR=Q3-Q1

lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
# 'X1_transaction_date', 'X2_house_age', 'X3_distance_to_MRT',
#        'X4_number_of_stores', 'X5_latitude', 'X6_longitude', 'Y_price'],
df=df[(df['price']>=lower)&(df['price']<=upper)]
print(f'清洗后的样本数：{len(df)}')
#对数变换

# np.log(df['X3_distance_to_MRT']+1)
df['logmrt']=np.log1p(df['DistMRT'])
#计算欧式距离
x_ave=df['latitude'].mean()
y_ave=df['lontitude'].mean()
# df['distcentre']=((df['X5_latitude']-x_ave)**2+(df['X6_longitude']-y_ave)**2)*111
df['distcentre']=np.sqrt((df['latitude']-x_ave)**2+(df['lontitude']-y_ave)**2)*111

# df.drop(['X5_latitude','X6_longitude'],axis=1,inplace=True)
#定义x和y
x=np.column_stack([
    # df['TransDate'],
    df['Houseage'],
    df['logmrt'],
    df['Numstores'],
    df['latitude'],
    df['lontitude'],
    # df['distcentre'],
    ]
)
# y=df['distance']
y=df['price']
#划分测试和训练
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
#定义模型
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)
models={
    'linear':LinearRegression(),
    'ridge':Ridge(alpha=100),
    'lasso':Lasso(alpha=1.0),
}

#训练
print('训练结果')
for name,model in models.items():
    model.fit(x_train_scaled,y_train)
    # r2_test=round(model.score(x_test_scaled,y_test),4)
    # r2_train=round(model.score(x_train_scaled,y_train),4)
    r2_train=r2_score(y_train,model.predict(x_train_scaled))
    r2_test=r2_score(y_test,model.predict(x_test_scaled))
    print(f'r2_test:{r2_test},r_train:{r2_train}')
