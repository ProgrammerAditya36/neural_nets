import numpy as np
# Chapter 3: Adding Layers
class Layer_Dense:
	def __init__(self, n_inputs, n_neurons):
		self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))
	def forward(self, inputs):
		self.output = np.dot(np.array(inputs), self.weights)+ self.biases

# Chapter 4: Activation Functions
class Activation_ReLU:
	# Forward pass
	def forward(self, inputs):
		self.output = np.maximum(0, inputs)


# Softmax activation
class Activation_Softmax:
	def forward(self, inputs):
		exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
		probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
		self.output = probabilities

# Chapter 5: Calculating Network Error Loss 
class Loss:
	def calculate(self, output, y):
		sample_losses = self.forward(output, y)
		data_loss = np.mean(sample_losses)
		return data_loss


class Loss_CategoricalCrossentropy(Loss):
	def forward(self, y_pred, y_true):
		samples = len(y_pred)
		y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)
		if len(y_true.shape) == 1:
			correct_confidences = y_pred_clipped[range(samples), y_true]
		elif len(y_true.shape) == 2:
			correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
		negative_log_likelihood = -np.log(correct_confidences)
		return negative_log_likelihood