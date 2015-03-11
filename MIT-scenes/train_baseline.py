from lasagne import layers, nonlinearities,objectives, updates
import theano
import theano.tensor as T
import sys
import numpy as np

'''
SCORES: FC6 LogisticRegression: 0.56315789473684208
		FC7 LogisticRegression: 0.55263157894736847
'''


batch_size = 50
total = 5350
X_batch = T.matrix()
y_batch = T.ivector()
batch_index = T.iscalar()

l1 = layers.InputLayer((100, 4096))
l2 = layers.DenseLayer(l1, num_units=67, nonlinearity=nonlinearities.softmax)
objective = objectives.Objective(l2,loss_function=objectives.multinomial_nll)
loss_train = objective.get_loss(X_batch, target=y_batch)

# load datasets
X_train_fc6 = theano.shared(np.load('/root/proj/MIT_dumped/X_train_fc6.npy').astype(theano.config.floatX))
X_test_fc6 = theano.shared(np.load('/root/proj/MIT_dumped/X_test_fc6.npy').astype(theano.config.floatX))
y_train = T.cast(theano.shared(np.load('/root/proj/MIT_dumped/y_train.npy')),'int32')
y_test = T.cast(theano.shared(np.load('/root/proj/MIT_dumped/y_test.npy')),'int32')

all_params = layers.get_all_params(l2)

LEARNING_RATE =0.008
MOMENTUM=0.9
upds = updates.nesterov_momentum(loss_train, all_params, LEARNING_RATE, MOMENTUM)
pred = T.argmax(
    l2.get_output(X_batch, deterministic=True), axis=1)
accuracy = T.mean(T.eq(pred, y_batch), dtype=theano.config.floatX)

print "begin compiling fc6..."
train = theano.function([batch_index], loss_train, updates=upds, givens={X_batch:X_train_fc6[batch_index*batch_size:(batch_index+1)*batch_size], y_batch:y_train[batch_index*batch_size:(batch_index+1)*batch_size]})
num_epochs = 100
for epoch in range(num_epochs):
        print "epoch %s" % epoch
	for batch in range(total/batch_size):
		loss = train(batch)

test = theano.function([], accuracy, givens={X_batch:X_test_fc6, y_batch:y_test})
print test()




batch_size = 50
total = 5350
X_batch = T.matrix()
y_batch = T.ivector()
batch_index = T.iscalar()

l1 = layers.InputLayer((100, 4096))
l2 = layers.DenseLayer(l1, num_units=67, nonlinearity=nonlinearities.softmax)
objective = objectives.Objective(l2,loss_function=objectives.multinomial_nll)
loss_train = objective.get_loss(X_batch, target=y_batch)

# load datasets
X_train_fc7 = theano.shared(np.load('/root/proj/MIT_dumped/X_train_fc7.npy').astype(theano.config.floatX))
X_test_fc7 = theano.shared(np.load('/root/proj/MIT_dumped/X_test_fc7.npy').astype(theano.config.floatX))
y_train = T.cast(theano.shared(np.load('/root/proj/MIT_dumped/y_train.npy')),'int32')
y_test = T.cast(theano.shared(np.load('/root/proj/MIT_dumped/y_test.npy')),'int32')

all_params = layers.get_all_params(l2)

LEARNING_RATE =0.05
MOMENTUM=0.9
upds = updates.nesterov_momentum(loss_train, all_params, LEARNING_RATE, MOMENTUM)
pred = T.argmax(
    l2.get_output(X_batch, deterministic=True), axis=1)
accuracy = T.mean(T.eq(pred, y_batch), dtype=theano.config.floatX)

print "begin compiling fc7..."
train = theano.function([batch_index], loss_train, updates=upds, givens={X_batch:X_train_fc7[batch_index*batch_size:(batch_index+1)*batch_size], y_batch:y_train[batch_index*batch_size:(batch_index+1)*batch_size]})
num_epochs = 100
for epoch in range(num_epochs):
        print "epoch %s" % epoch
	for batch in range(total/batch_size):
		loss = train(batch)

test = theano.function([], accuracy, givens={X_batch:X_test_fc7, y_batch:y_test})
print test()
