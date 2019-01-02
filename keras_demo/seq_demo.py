
from keras.models import Sequential
from keras.layers import Dense, Activation

# 序贯模型——Sequential
# 一、定义模型
model = Sequential()
model.add(Dense(units=64, input_dim=100))
model.add(Activation("relu"))
model.add(Dense(units=10))
model.add(Activation("softmax"))

# 二、编译模型
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 自定义优化器
# from keras.optimizers import SGD
# model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))

# 三、训练模型
model.fit(x_train, y_train, epochs=5, batch_size=32)
# model.train_on_batch(x_batch, y_batch)

# 四、评估
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

# 五、预测
classes = model.predict(x_test, batch_size=128)