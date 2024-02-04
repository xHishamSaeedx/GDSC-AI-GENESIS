# -*- coding: utf-8 -*-
"""Copy of Tensorflow_Basics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DRDPnjAV7n6wveRGpn4bkh7kp7nZrlpl
"""

# Create a scalar (rank 0 tensor)
scalar = tf.constant(7)
scalar

# Check the number of dimensions of a tensor (ndim stands for number of dimensions)
scalar.ndim

# Create a vector (more than 0 dimensions)
vector = tf.constant([10, 10])
vector

# Create a matrix (more than 1 dimension)
matrix = tf.constant([[10, 7],
                      [7, 10]])
matrix

matrix.ndim

# How about a tensor? (more than 2 dimensions, although, all of the above items are also technically tensors)
tensor = tf.constant([[[1, 2, 3],
                       [4, 5, 6]],
                      [[7, 8, 9],
                       [10, 11, 12]],
                      [[13, 14, 15],
                       [16, 17, 18]]])
tensor

tensor.ndim

# scalar: a single number.
# vector: a number with direction (e.g. wind speed with direction).
# matrix: a 2-dimensional array of numbers.
# tensor: an n-dimensional arrary of numbers (where n can be any number, a 0-dimension tensor is a scalar, a 1-dimension tensor is a vector).

changeable_tensor = tf.Variable([10, 7])
unchangeable_tensor = tf.constant([10, 7])
changeable_tensor, unchangeable_tensor

changeable_tensor[0].assign(7)
changeable_tensor

# Shuffle a tensor (valuable for when you want to shuffle your data)
not_shuffled = tf.constant([[10, 7],
                            [3, 4],
                            [2, 5]])
# Gets different results each time
tf.random.shuffle(not_shuffled, seed=42)

rank_4_tensor = tf.zeros([2, 3, 4, 5])
rank_4_tensor

# Get various attributes of tensor
print("Datatype of every element:", rank_4_tensor.dtype)
print("Number of dimensions (rank):", rank_4_tensor.ndim)
print("Shape of tensor:", rank_4_tensor.shape)
print("Elements along axis 0 of tensor:", rank_4_tensor.shape[0])
print("Elements along last axis of tensor:", rank_4_tensor.shape[-1])
print("Total number of elements (2*3*4*5):", tf.size(rank_4_tensor).numpy()) # .numpy() converts to NumPy array

# Create a rank 2 tensor (2 dimensions)
rank_2_tensor = tf.constant([[10, 7],
                             [3, 4]])

tf.expand_dims(rank_2_tensor, axis=-1) # "-1" means last axis

# You can add values to a tensor using the addition operator
tensor = tf.constant([[10, 7], [3, 4]])
tensor + 10

# Multiplication (known as element-wise multiplication)
tensor * 10

# Subtraction
tensor - 10

# Use the tensorflow function equivalent of the '*' (multiply) operator
tf.multiply(tensor, 10)

# Create (3, 2) tensor
X = tf.constant([[1, 2],
                 [3, 4],
                 [5, 6]])

# Create another (3, 2) tensor
Y = tf.constant([[7, 8],
                 [9, 10],
                 [11, 12]])
X, Y

tf.reshape(Y, shape=(2, 3))

X @ tf.reshape(Y, shape=(2, 3))

# Example of transpose (3, 2) -> (2, 3)
tf.transpose(X)

# Create a new tensor with default datatype (float32)
B = tf.constant([1.7, 7.4])

B

# Change from float32 to float16 (reduced precision)
B = tf.cast(B, dtype=tf.float16)
B

x = tf.constant([[1,2],[2,1],[3,4]])

# Find the minimum
tf.reduce_min(X)

# Find the maximum
tf.reduce_max(X)

# Find the mean
tf.reduce_mean(X)

# Find the sum
tf.reduce_sum(X)

# Find the maximum element position of F
tf.argmax(X)

# Find the minimum element position of F
tf.argmin(X)

rank_4_tensor = tf.zeros([1,1,1,5])
rank_4_tensor

# Squeeze tensor G (remove all 1 dimensions)
rank4_squeezed = tf.squeeze(rank_4_tensor)
rank4_squeezed