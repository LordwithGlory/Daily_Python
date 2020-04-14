import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
from tensorflow import keras
from keras.datasets import mnist

print("Eager_mode: ", tf.executing_eagerly())
# 该函数用来获得当前主机上某种特定运算设备类型
print("GPU is ","avivable " if tf.config.experimental.list_physical_devices("GPU") else "not avialbe")

# 按照6:4的来划分原训练集合为训练集和验证集,但是这个好像因为p各种版本问题有问题
# train_validation_split = tfds.Split.TRAIN.subsplit([6, 4])
(train_data,valid_data),test_data=tfds.load(
    name="imdb_reviews",
    # split选择拆分数据集，默认为tfds.Split.TRAIN和tfds.Split.TEST,
    # 表示划分为train集合和test集合
    # 由于p各种版本问题有问题
    # split=(train_validation_split, tfds.Split.TEST),
    # 因为必须要和上面的匹配所以需要是两个参数
    split=(('train[:60%]','train[60%:]'),'test'),
    as_supervised=True
)
# 这个方法获取的是tf张量，而使用datasets里面数据获得的是numpy,
# 因此tuple的很多方法不能用
print(test_data)

# batch函数用来将数据batch化 iter为一个迭代函数
train_examples_batch,train_label=next(iter(train_data.batch(10)))
# print(train_examples_batch)

# 使用tensorflow中的模型进行预测已经包含了表示文本的方法 模型的层数 每层的隐藏神经元
embedding = "https://hub.tensorflow.google.cn/google/tf2-preview/gnews-swivel-20dim/1"
# 构建Tensorflow Hub 模型嵌入（embed）语句的Keras层
hub_layer = hub.KerasLayer(embedding,input_shape=[],dtype=tf.string,trainable=True)
# 将文本表示为数据
# print(hub_layer(train_examples_batch))

model=keras.Sequential()
# 第一层将文本转换为嵌入向量
model.add(hub_layer)
# 第二层是16个隐藏单元的全联接层
model.add(tf.keras.layers.Dense(16, activation='relu'))
# 第三层是与单个输出节点相连接，使用 Sigmoid 激活函数
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
print(model.summary())

# metrics是评价函数，和损失函数 相似，只不过评价函数的结果不会用于训练过程中作为参数。
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy'])
# shuffle用来将元素打乱 数值越大随机程度越大，batch则是按照顺序取出n行数据
model.fit(train_data.shuffle(1000).batch(512),epochs=20,validation_data=valid_data.batch(512),verbose=1)

result=model.evaluate(test_data.batch(512),verbose=2)
print(result)
# metrics_names为评价指标，zip是将其打包为元祖,目测是一一对应
# 跑tensor居然会这么大声音
for name,value in zip(model.metrics_names,result):
    print("%s:%.3f",name,value)