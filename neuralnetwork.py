import numpy as np 
#define normalizing function i.e. the sigmoid function (takes an x value and returns any value between 0 and 1)

def sigmoid(x):
	return 1 / (1+ np.exp(-x))

def sigmoid_derivative(x);
	return x * (1-x)

#each row in the input output table is a training example 

training_inputs = np.array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]]

desired_training_outputs = np.array([[0,1,1,0]]).T  
#above is a 4x1 matrix transposed - corresponding outputs for the defined set of inputs

#now we initialize weights- by assigning random values to weights w1, w2, w3
#random values from -1 to 1  with a mean of zero

#seed random numbers 

np.random.seed(1)

synaptic_weights =  2 * np.random.random((3,1)) - 1 
#3x1 matrix of random values of weights because we have 3 inputs and 1 output - this is weight initialiation 

print('Random starting synaptic weights: ')
print(synaptic_weights)

#below is main loop

for iteration in range(20000):

	input_layer = training_inputs  set input layer to be our training inputs

	outputs = sigmoid(np.dot(input_layer* synaptic_weights))
#above outputs is the weighted sum function- i.e. element wise multiplication of matrices labelled input_layer and synaptic_weights

	error = desired_training_outputs - outputs

	adjusted_weights = error * sigmoid_derivative(outputs) 

	synaptic_weights += np.dot(input_layer.T.adjustments)

print('Synaptic weights after training: ')
print(synaptic_weights)

print('Outputs after training: ')
print(outputs)


