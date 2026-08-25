# 功能要求
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
image = np.array([
    [120, 200, 150, 80, 60],
    [90, 255, 180, 75, 40],
    [30, 100, 220, 160, 70],
    [50, 140, 190, 210, 95],
    [80, 60, 170, 240, 130]
])
reverse_image=255-image

binary_image=np.where(image>=128,255,0)
bright_image=np.clip(image+30,0,255)
fex,axes=plt.subplots(2,2,figsize=(8,8))
axes[0,0].imshow(image,cmap='gray')
axes[0,0].set_title('原始图像')
axes[0,0].axis('off')

max_pos=np.unravel_index(np.argmax(image),image.shape)

axes[0, 0].annotate(
    "最亮像素",
    xy=(max_pos[1], max_pos[0]),
    xytext=(3, 0),
    arrowprops=dict(facecolor='blue', shrink=0.05),
    color='red'
)


# 反色图像
axes[0, 1].imshow(reverse_image, cmap='gray')
axes[0, 1].set_title("反色图像")
axes[0, 1].axis('off')


# 二值化图像
axes[1, 0].imshow(binary_image, cmap='gray')
axes[1, 0].set_title("二值化图像")
axes[1, 0].axis('off')


# 变亮图像
axes[1, 1].imshow(bright_image, cmap='gray')
axes[1, 1].set_title("变亮图像")
axes[1, 1].axis('off')


plt.tight_layout()

plt.savefig("image_process_result.png")

plt.show()


# 绘制像素直方图
plt.figure(figsize=(6, 4))

plt.hist(
    image.flatten(),
    bins=10,
    color='skyblue',
    edgecolor='black'
)

plt.title("像素分布直方图")
plt.xlabel("像素值")
plt.ylabel("数量")

plt.show()
# img=plt.imread(
    # filr_path='test.jpg'
# )
# print(img.shape)
# print(img.ndim)
# print(img.dtype)

# 2. 图像灰度化处理
# 灰度化公式：gray_image = image.mean(axis=2)
# 要求使用 NumPy 向量化运算，不允许逐像素循环
    
# 3. 多图对比展示
# 创建一个 2 × 2 子图布局：
# - 子图 (0,0)：显示原始图像
# - 子图 (0,1)：显示反色图像
# - 子图 (1,0)：显示二值化图像
# - 子图 (1,1)：显示变亮后的图像
# 要求添加标题、使用灰度颜色映射 gray并且隐藏坐标轴
# 4. 图像增强处理
# - 实现 图像反色
# - 实现 图像二值化
#   要求：
#   - 像素值 ≥ 128 显示为 255
#   - 像素值 < 128 显示为 0
print(np.where(s>=128,'255','0'))
# - 实现 图像变亮
#   - 所有像素值 +30
#   - 防止超过 255
bright=arr+30
bright=np.clip(bright,0,255)
# - 添加黑色边框
# - 添加标题与坐标轴标签
# 5. 像素分布分析
# 使用 plt.hist() 绘制灰度图像的像素分布直方图。
# 要求：
# - bins=20
# - 颜色为蓝色
# - 添加黑色边框
# - 添加标题与坐标轴标签
# 6. 图像关键点标注
# 在原始图像中：
# - 找出最亮像素的位置
# - 使用 annotate() 添加箭头标注
# - 标注文字为最亮像素
# 7. 图像保存与风格设置
# 要求：
# - 设置中文字体
# - 使用 tight_layout() 防止重叠
# - 将最终结果保存为 image_process_result.png
# # 参考代码