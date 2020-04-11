import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

import os

def plot_image(i,prediction_arrary,true_lable,img):
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img,cmap=plt.cm.binary)
    predict_lable=np.argmax(prediction_arrary)
    if predict_lable==true_lable:
        color="blue"
    else:
        color="red"
    # print(prediction_arrary)
    plt.xlabel("{} {:2.0f} % ({})".format(class_names[predict_lable],100*np.max(prediction_arrary),class_names[true_lable]),color=color)

def plot_value_array(i,prediction_arrary,true_label):
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    # 绘制柱状图,第一个是x轴位置，第二个是高度（两个数组来画每个柱子）
    thisplot=plt.bar(range(10),prediction_arrary,color="#777777")
    # 设置y值的显示范围(最大值最小值)
    plt.ylim([0,1])
    # 将预测的设置为红色
    thisplot[np.argmax(prediction_arrary)].set_color('red')
    # 将正确的设置为蓝色
    thisplot[true_label].set_color('blue')

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
fashion_mnist=keras.datasets.fashion_mnist
(train_img,train_lables),(test_img,test_lables)=fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# print(train_img.shape)
# print(len(train_lables))
# print(train_lables)

# 展示第一个图像
# plt.figure()
# plt.imshow(train_img[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

train_img=train_img/255.0
test_img=test_img/255.0

# 设置图像背景的大小
plt.figure(figsize=(50,10))
for i in range(25):
    # 将figure对象分为多行多列，设置子图的位置
    # 位置从左到右从上到下编号
    plt.subplot(5,5,i+1)
    # 设置x轴的刻度
    plt.xticks([])
    # 设置y轴刻度（本次是将其设置为空）
    plt.yticks([])
    # 设置图像网格化表示（本次是禁止）
    plt.grid(False)
    # 在子图中使用自定义的colormap这里是二进制
    plt.imshow(train_img[i],cmap=plt.cm.binary)
    plt.xlabel(class_names[train_lables[i]])
plt.show()

model=keras.Sequential([
    # 将二维的数据变为一维数据，没有学习参数，只是格式化数据
    keras.layers.Flatten(input_shape=(28,28)),
    # 添加一个128个神经元 激活函数为rule的全连接层
    keras.layers.Dense(128, activation='relu'),
    # 这一层返回十个值的数组表示某种可能性的概率
    keras.layers.Dense(10)
])

model.compile(
    # 设置优化方法，有sgd等多种可以选择
    optimizer='adam',
    # 用来衡量训练中的精准度
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    # 用于评估性能的指标
    metrics=['accuracy']
)

model.fit(train_img,train_lables,epochs=10)
# 当测试的准确度小雨训练准确度说明存在过拟合
test_loss, test_acc=model.evaluate(test_img,test_lables,verbose=2)
# print('\n测试准确度:',test_acc)
# print('\n测试损失:',test_loss)
print(model.predict(test_img))

# 进行归一化 让概率在[0,1]
probility_model=tf.keras.Sequential([model,tf.keras.layers.Softmax()])
# 如果对于二维的预测会报错test_img[0]，所以需要使用expand_dims方法,当然返回值也是三维的
one_predict=probility_model.predict(np.expand_dims(test_img[501],0))
plot_value_array(501,one_predict[0],test_lables[501])
# 将x坐标进行一一对应，并设置旋转角度为45度
plt.xticks(range(10),class_names,rotation=45)
predictions=probility_model.predict(test_img)
plt.show()
# print(predictions[0])
# print(class_names[np.argmax(predictions[0])])

# 针对一个进行展示
# plt.figure(figsize=(6,3))
# plt.subplot(1,2,1)
# plot_image(0,predictions[0],test_lables[0],test_img[0])
# plt.subplot(1,2,2)
# plot_value_array(0,predictions[0],test_lables[0])
# plt.show()

plt.figure(figsize=(20,20))
for i in range(24):
    plt.subplot(8,6,1+i*2)
    plot_image(100+i,predictions[100+i],test_lables[100+i],test_img[100+i])
    plt.subplot(8,6,2+i*2)
    plot_value_array(i+100,predictions[i+100],test_lables[i+100])
# 让图像充满整个区域
plt.tight_layout()
plt.show()