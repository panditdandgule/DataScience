## import libraries
# standard libraries
import random

# third party libraries
import numpy as np

"""
network.py
~~~~~~~~~~
A module to implement the stochastic gradient descent learning
algorithm for a feedforward neural network.  Gradients are calculated
using backpropagation.
"""


class Network(object):

    def __init__(self, sizes):
        """The list ``sizes`` contains the number of neurons in the
        respective layers of the network.  For example, if the list
        was [2, 3, 1] then it would be a three-layer network, with the
        first layer containing 2 neurons, the second layer 3 neurons,
        and the third layer 1 neuron.  The biases and weights for the
        network are initialized randomly, using a Gaussian
        distribution with mean 0, and variance 1.  Note that the first
        layer is assumed to be an input layer, and by convention we
        won't set any biases for those neurons, since biases are only
        ever used in computing the outputs from later layers."""
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a

    def SGD(self, train_data, epochs, mini_batch_size, eta,
            test_data=None, store_eval=None):
        """Train the neural network using mini-batch stochastic
        gradient descent.  The ``training_data`` is a list of tuples
        ``(label, image)`` representing the training labels and
        pixel inputs repsectively. The other non-optional parameters are
        self-explanatory.  If ``test_data`` is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially. The
        final output of this process are the trained weights
        and biases."""
        n = len(train_data)
        
        trained_b = self.biases
        trained_w = self.weights
        
        if test_data: n_test = len(test_data)
            
        for j in range(epochs):
            random.shuffle(train_data)
            mini_batches = [
                train_data[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            trained_b = self.biases
            trained_w = self.weights
            if test_data:
                print("Epoch {}: {} / {}".format(
                    j, self.evaluate(test_data), n_test))
                store_eval.append(self.evaluate(test_data)/len(test_data))
                        
            else:
                print("Epoch {} complete".format(j))
        
        return (trained_b, trained_w)

    def update_mini_batch(self, mini_batch, eta):
        """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The ``mini_batch`` is a list of tuples ``(value, image)``, and
        ``eta`` is the learning rate."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for value, image in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(image, value)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, image, value):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = image
        activations = [activation] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # backward pass
        delta = self.cost_derivative(activations[-1], value) * sigmoid_prime(zs[-1]) 
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = [(np.argmax(self.feedforward(image)), value)
                        for value, image in test_data]
        return sum(int(x == y) for x, y in test_results)

    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        cost = np.array(output_activations)
        cost[y] = cost[y] - 1.0
        return cost
    

#### Miscellaneous functions
def sigmoid(z):
    """The sigmoid function."""
    return (1.0/(1.0 + np.exp(-z)))


def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))


def format_data(data):
    """Formats the input kaggle data into an appropriate data
    structure to work with. Each pixel entry is normalized to be 
    between 0 and 1 (from 0 to 255) and each input image is stored 
    in a list containing entries with shape (784,1). Note that this 
    is NOT the same as (784,) as this input will cause some numpy
    routins to perform incorrectly. The image label is also put into 
    a list and the two are then zipped together and returned."""
    inputs = [np.reshape(x, (784,1))/255 for x in data[:,1:]]
    outputs = [y for y in data[:,0]] 
    formatted_data = zip(outputs, inputs)
    return formatted_data


def print_image (data, image):
    """Function to output an image to console. The input variable data is the 
    MNIST dataset in the format specified by the format_data function. The 
    input variable image is the choice for which image in the set to output.
    The index starts at zero so choosing the first image would have image = 0."""
    row_length = 28
    for j in range (0, row_length):
        print ('\n')
        for i in range (0, row_length):
            print ("%3i" % data.iloc[image,1+j*row_length:29+j*row_length][i], end = ' ')
