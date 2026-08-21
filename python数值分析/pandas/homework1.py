import pandas as pd
import numpy as np
data=[8.5,4.0,6.0,15.0]
s_price=pd.Series(data,index=['苹果','香蕉','橙子','葡萄'])
print('水果价格',s_price)
data2=[['苹果',100,'陕西'],
    ['香蕉',150,'广东'],
    ['橙子',80,'江西'],
    ['葡萄',50,'新疆']
]
df_inventory=pd.DataFrame(
    data2,
    columns=['水果','库存','产地']
)
print(df_inventory)
print('香蕉到葡萄的所有行:',s_price['香蕉':'葡萄'])
print('香蕉到葡萄的所有行:',s_price.loc['香蕉':'葡萄'])
print('香蕉到葡萄的所有行:',df_inventory.iloc[[1,2,3]])
print('第0行和第2行的"水果"和"库存"列',df_inventory.iloc[[0,2]])
print('所有水果的总库存',df_inventory['库存'].sum())
print('按库存量从高到低排序',df_inventory.sort_values(ascending=False,by='库存'))
data3=[['苹果',100,'陕西',0.05],
    ['香蕉',150,'广东',np.nan],
    ['橙子',80,'江西',0.02],
    ['葡萄',50,'新疆',np.nan]]
df_inventory=pd.DataFrame(data3,columns=['水果','库存','产地','损耗率'])
print('缺失值填充：',df_inventory.fillna(0))