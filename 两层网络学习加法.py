import tensorflow as tf
from numpy.random import RandomState


dataset_size = 202

#定义变量两层的w
w_r = tf.Variable(tf.random_normal([2,5], stddev=2))
w_y = tf.Variable(tf.random_normal([5,1], stddev=2))
#定义常量两层的b
b_r = tf.Variable(tf.constant(2.0, shape=[5]))
b_y = tf.Variable(tf.constant(2.0, shape=[1]))
rdm = RandomState(1)
X = rdm.rand(dataset_size,2)
print(X)
Y = [[x1 + x2 ]for (x1,x2) in X]
print(Y)
#表示能够接收更新
x = tf.placeholder(tf.float32,shape=(1,2))
t = tf.placeholder(tf.float32,shape=(1,1))
#正向传播
b = tf.nn.tanh(tf.matmul(x,w_r)+b_r)
y = tf.nn.relu(tf.matmul(b,w_y)+b_y)
#损失函数，多用于连续的，大规模数据
#loss = tf.nn.softmax_cross_entropy_with_logits(logits = y,labels = t)
#损失函数，多用于离散的，小数据集的函数
loss = tf.reduce_mean(tf.square(t-y)) + tf.contrib.layers.l2_regularizer(.5) (w_r) + tf.contrib.layers.l2_regularizer(.5)(w_y)
#梯度下降
train_step = tf.train.AdamOptimizer(0.001).minimize(loss)
#建立会话来运行TensorFlow
sess = tf.InteractiveSession()
#初始化所有变量的值
tf.global_variables_initializer().run()
#循环T次来进行训练
for i in range(50):
         print(i)
         for v in range(100):
                  for j in range(199):
                           a = j
                           sess.run(train_step,feed_dict={x:X[a:a+1],t:Y[a:a+1]})
                  
print(sess.run(w_r))
print(sess.run(b_r))
print(sess.run(y,feed_dict={x:[[1.0,0.834434]]}))
sess.close()
