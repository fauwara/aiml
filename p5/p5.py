import numpy as np 

x = np.array(([2,9], [1,5], [3,6]), dtype=float)
x = x/np.amax(x, axis=0)
# [2,9]
# [1,5]
# [3,6]
# np.amax(x, axis=0) # -> [3,9] 
# max of 0 axis in array x are 3 and 9
# print(x)


y = np.array(([92], [80], [86]), dtype=float)
y = y/100


def sigmoid(x):
    return 1/(1+np.exp(-x)) # np.exp -> e^ -x

def derivatives_sigmoid(x):
    return x*(1-x)

epoch = 100
learning_rate = 0.6
inp_neurons = 2 # input
hid_neurons = 3 # hidden
out_neurons = 1 # output

wh = np.random.uniform(size=(inp_neurons, hid_neurons))
bh = np.random.uniform(size=(1, hid_neurons))
wo = np.random.uniform(size=(hid_neurons, out_neurons))
bo = np.random.uniform(size=(1, out_neurons))

# print(wo)
# print(wo.T)


for i in range(epoch):
    net_h = np.dot(x, wh) + bh
    hid_output = sigmoid(net_h)
    
    net_o = np.dot(hid_output, wo) + bo
    output = sigmoid(net_o)
    
    deltak = (y-output)*derivatives_sigmoid(output)
    deltah = deltak.dot(wo.T)*derivatives_sigmoid(output)
    
    wh = wh + x.T.dot(deltah) * learning_rate
    wo = wo + hid_output.T.dot(deltak) * learning_rate


print(x)
print()
print(y)
print()
print(output)