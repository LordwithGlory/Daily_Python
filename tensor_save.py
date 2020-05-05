import tensorflow as tf
from tensorflow import keras
import os
import time

(train_data,train_lable),(test_data,test_label)=keras.datasets.mnist.load_data()
test_label=test_label[:1000]
train_lable=train_lable[:1000]

# reshape的第一个参数表示要自动适配缺失的一个维度
train_data=train_data[:1000].reshape(-1,28*28)/255.0
test_data=test_data[:1000].reshape(-1,28*28)/255.0
def create_model():
    model=tf.keras.models.Sequential([
        keras.layers.Dense(512,activation='relu',input_shape=(784,)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10,activation='softmax')
    ])
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

model=create_model()
loss,acc=model.evaluate(test_data,test_label,verbose=2)
print("The accuracy:{:5.2f}%".format(acc*100))

def update_model(model):
    # 其实这个就是设置了前缀部分
    check_path='temp/cp.ckpt'
    # check_dir=os.path.dirname(check_path)
    # 创建一个保存模型权重的回调
    cp_callback=tf.keras.callbacks.ModelCheckpoint(filepath=check_path,save_weights_only=True,verbose=1)
    model.fit(train_data,train_lable,epochs=10,validation_data=(test_data,test_label),callbacks=[cp_callback])
    # print(os.listdir(check_dir))
    return model
# update之后 从对应文件内获取权重
model.load_weights('temp/cp.ckpt')

def update_many_model():
    check_path="temp/cp{epoch:04d}.ckpt"
    check_dir=os.path.dirname(check_path)
    # 创建一个每10次保存一回的回调
    callbacks=tf.keras.callbacks.ModelCheckpoint(filepath=check_path,verbose=1,save_weights_only=True,period=10)
    model=create_model()
    model.save_weights(check_path.format(epoch=0))
    model.fit(train_data,train_lable,epochs=50,callbacks=[callbacks],validation_data=(test_data,test_label),verbose=0)
    return model,check_dir

# 直接从对应path中加载模型，但是该模型是已经搭好了架子
# model=update_model(model)
_,check_dir=update_many_model()
# 获取最新的checkpoint
lastest=tf.train.latest_checkpoint(check_dir)
model.load_weights(lastest)
loss,acc=model.evaluate(test_data,test_label,verbose=2)
print("The accuracy:{:5.2f}%".format(acc*100))

# 保存为h5模型 并且进行模型加载
model.save('mymodel.h5')
newmodel=keras.models.load_model('mymodel.h5')
# print(newmodel.summary())

# pb模型保存加载
save_model_path="save_models/{}".format(int(time.time()))
# 保存模型为pb类型文件
tf.keras.experimental.export_saved_model(newmodel,save_model_path)
# 从pb类型文件中加载模型
load_model=tf.keras.experimental.load_from_saved_model(save_model_path)
# print(load_model.summary())
print(model.predict(test_data).shape)
# model在进行evaluate fit之前需要进行compile