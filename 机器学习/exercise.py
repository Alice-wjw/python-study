from sklearn.preprocessing import StandardScaler
# scaler=StandardScaler()
# #fit,计算均值和标准差并存储
# #fit，transform，用已经存储的均值和标准差进行变换，返回变换后的数组
# X_train_scaled=scaler.fit_transform(X_train)
# X_test_scaled=scaler.transform(X_test)
from sklearn.preprocessing import MinMaxScaler
# scaler=MinMaxScaler(feature_range=(0,1))
# Y_train_scaled=scaler.fit_transform(Y_train)
# Y_test_scaled=scaler.transform(Y_test)
#
from sklearn.linear_model import LinearRegression,Ridge,Lasso
# model =LinearRegression()
# model.fit(X_train,y_train)
# y_pred=model.predict(X_test_scaled)
# # 10:40困了
# model=Ridge(alpha=1.0)
# model.fit(X_train_scaled,Y_train_scaled)
# y_pred2=model.predict(X_test_scaled)
# model=Lasso(alpha=1.0)
# model.fit(X_train_scaled,Y_train_scaled)
# y_pred3=model.predict(X_test_scaled)
#创建数据集
import numpy as np
from sklearn.model_selection import train_test_split
np.random.seed(42)
n_samples=100
X=np.column_stack([
    np.random.uniform(50,200,n_samples),
    np.random.randint(1,6,n_samples),
    np.random.randint(1,30,n_samples),
])
y=0.5 * X[:,0]+3*X[:,1]+0.1*X[:,2]+np.random.normal(0,5,n_samples)
#进行训练集测试集划分
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
#进行归一化
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
print('====StandardScaler====')
print(f'训练集各特征的平均值:{np.round(X_train_scaled.mean(axis=0),4)}')
print(f'训练集各特征的标准差：{np.round(X_train_scaled.std(axis=0),4)}')
#np.round(操作对象，保留位数），四舍五入的函数
models={
    'LinearRegression':LinearRegression(),
    'Ridge(Alpha=1.0)':Ridge(alpha=1.0),
    'Lasso(Alpha=1.0)':Lasso(alpha=1.0),
}

print('\n===训练结果===')
for name,model in models.items():
    #进行训练
    model.fit(X_train_scaled,y_train)
    r2=round(model.score(X_test_scaled,y_test),4)
    coef=np.round(model.coef_,4)
    print(f'\n{name}')
    print(f'测试集的R:{r2}')
    print(f'权重coef：{coef}')
    print(f'偏置intercept：{round(model.intercept_,4)}')
