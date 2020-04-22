import tensorflow as tf
import numpy as np
from tensorflow import keras

import matplotlib.pyplot as plt

imdb=keras.datasets.imdb
# num_words保留训练数据中出现频率最高的x个单词
(train_data,train_labels),(test_data,test_labels)=imdb.load_data(num_words=10000)
print("Training entries:{},labels:{},type:{} {}".format(train_data.shape,train_labels.shape,type(train_data),type(train_labels)))
# 电影评论长度是不同的，但是我们需要把他转换为相同的
# print(train_data[0],train_labels[0])

# 获得单词和整数映射的词典,所以处理后的data的确应该是这样的
word_index=imdb.get_word_index()
# print(word_index)
word_index={k:(v+3) for k,v in word_index.items()}
# 添加了几个dict
word_index["<PAD>"]=0
word_index["<START>"]=1
word_index["<UNK>"]=2
word_index["<UNUSED"]=3

reverse_word_index=dict([(v,k) for k,v in word_index.items()])
train_sen=""
for word in train_data[0]:
    train_sen+=reverse_word_index.get(word,'?')+" "
# print(train_sen)

# 将输入的数据转换为具有相同长度的向量
train_data=keras.preprocessing.sequence.pad_sequences(train_data,
    value=word_index["<PAD>"],# 如果填充的话使用的填充值
    padding='post',# 如果不够maxlen的话填充的位置，pre表示在前面，post表示在后面
    maxlen=256)# maxlen表示向量的长度

test_data=keras.preprocessing.sequence.pad_sequences(test_data,
    value=word_index["<PAD>"],
    padding='post',
    maxlen=256)

# print(train_data[0])
vocab_size=10000
model=keras.Sequential()
# 将正整数转换为具备固定大小的向量
# 第一个长度是字典的长度，第二个代表全连接的维度output_dim
# 将输入的二维shape转换为添加了output_dim的三维向量
model.add(keras.layers.Embedding(vocab_size, 16))
# 将序列维度平均值为每个样本返回一个定长输出向量
model.add(keras.layers.GlobalAveragePooling1D())
# 指定输出维度以及激活函数的全连接层
model.add(keras.layers.Dense(16,activation='relu'))
model.add(keras.layers.Dense(1,activation='sigmoid'))
print(model.summary())
model.compile(optimizer="adam",
    loss='binary_crossentropy',
    metrics=['accuracy'])
# 创建一个验证集
x_val=train_data[:10000]
partial_x_train=train_data[10000:]

y_val=train_labels[:10000]
partial_y_train=train_labels[10000:]

history=model.fit(partial_x_train,
    partial_y_train,
    epochs=40,
    batch_size=512,
    validation_data=(x_val,y_val),
    verbose=1)
result=model.evaluate(test_data,test_labels,verbose=2)

history_dict=history.history
print(history_dict.keys)
acc=history_dict['accuracy']
val_acc=history_dict['val_accuracy']
loss=history_dict['loss']
val_loss=history_dict['val_loss']
epochs=range(1,len(acc)+1)

plt.plot(epochs,loss,'bo',label='Training loss')
plt.plot(epochs,val_loss,'b',label='Validation loss')
plt.plot(epochs,acc,'ro',label='Training accurcy')
plt.plot(epochs,val_acc,'r',label='Validation accurcy')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('loss')
# 展示图例就是什么图形什么样子
plt.legend()
plt.show()