import numpy as np

x = np.array(([9,2],[1,3],[2,1]), dtype=float)
x = x/np.amax(x, axis=0)

y = np.array((92, 86, 82), dtype=float)
y = y/100


epoch = 1000
lr = 0.6
il = 2
hl = 3
ol = 1

wh = np.random.uniform(size=(il,hl))
bh = np.random.uniform(size=(1,hl))
wo = np.random.uniform(size=(hl,ol))
bo = np.random.uniform(size=(1,ol))


def sigmoid(x):
	return 1/(1+np.exp(x))

def derivative_sigmoid(x):
	return x * (1-x)

for i in range(len(epoch)):
    
	net_h = np.dot(x, wh) + bh
	sigmoid_h = sigmoid(net_h)
	net_o = np.dot(sigmoid_h, wo) + bo
	sigmoid_o = sigmoid(net_o)

	deltak = (y-sigmoid_o)*derivative_sigmoid(sigmoid_o)
	deltah = deltak.dot(wo.T) * derivative_sigmoid(sigmoid_o)

	wh = wh + x.T.dot(deltah) * lr
	wo = wo + sigmoid_h.dot(deltak)* lr

