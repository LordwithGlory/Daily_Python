import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
# 如果不使用tensorflow中的keras可能报错
from tensorflow.keras import layers
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# 下载数据集
dataset_path=keras.utils.get_file("auto-mpg.data", "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
print(dataset_path)

column_names=['MPG','Cylinders','Displacement','Horsepower','Weight','Acceleration', 'Model Year', 'Origin']
# names指定表头 na_values用来替换NaN/NA的值 skipinitialspace忽略分隔符后的空白 seq是表示csv的分割 comment标志着注视行开头
raw_data=pd.read_csv(dataset_path,names=column_names,na_values='?',comment='\t',sep=" ",skipinitialspace=True)
dataset=raw_data.copy()
# 对于每行为空的进行计数
# print(dataset.isna().sum())
# 删除存在空的那些行
dataset=dataset.dropna()
# 获取并删除茉个属性
origin=dataset.pop('Origin')
# 添加某些行
dataset['USA']=(origin==1)*1.0
dataset['EUP']=(origin==2)*1.0
dataset['JAP']=(origin==3)*1.0
# print(dataset.tail())

# frac表示抽样的概率 random_state表示随机种子，如果值为1说明可以重复选例子
train_data=dataset.sample(frac=0.8,random_state=0)
# 剔除了train_data
test_data=dataset.drop(train_data.index)
# 为联合关系绘制散点图 为单变量绘制直方图（对角线是直方图）
sns.pairplot(train_data[["MPG", "Cylinders", "Displacement", "Weight"]],diag_kind="kde")

train_stats=train_data.describe()
# 删除某列属性
train_stats.pop("MPG")
# 进行转置操作
train_stats=train_stats.transpose()

# 分离特征值
train_labels=train_data.pop("MPG")
test_labels=test_data.pop("MPG")
# 进行归一化操作
def norm(x):
    # 虽然mean这个维度比较小，但是可以让每个维度都减去mean
    return (x-train_stats['mean']/train_stats['std'])
normed_train_data=norm(train_data)
normed_test_data=norm(test_data)

model=keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(train_data.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])
print(model.summary())

# 用来进行打印进度
class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0: print('')
        print('.', end='')
# RMSProp 优化器 可以设置学习率 衰减率 模糊因子 学习率衰减值
optimizer=tf.keras.optimizers.RMSprop(0.001)
# mae是平均绝对误差 
model.compile(loss='mse',optimizer=optimizer,metrics=['mae','mse'])
# patience 值用来检查改进 epochs 的数量，callbacks里面加入early_stop可以提前停止
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
history=model.fit(train_data,train_labels,epochs=1000,validation_split=0.2,verbose=0,callbacks=[PrintDot()])
hist=pd.DataFrame(history.history)
# print(hist.tail)
# epoch不属于history.history中的参数，因此增加了这个属性
hist['epoch']=history.epoch
# print(hist.tail())

plt.figure()
plt.xlabel("Epoch")
plt.ylabel("Mean abs error[MPG]")
plt.plot(hist['epoch'],hist['mae'],label='train epoch')
plt.plot(hist['epoch'],hist['val_mae'],label='valid epoch')
plt.ylim([0,5])

# xisa可以确定坐标轴的形状等参数
plt.figure()
plt.xlabel("Epoch")
plt.ylabel("Mean abs error[MPG]")
plt.plot(hist['epoch'],hist['mae'],label='train epoch')
plt.plot(hist['epoch'],hist['val_mae'],label='valid epoch')
plt.legend()
plt.show()

model.evaluate(test_data,test_labels,verbose=2)