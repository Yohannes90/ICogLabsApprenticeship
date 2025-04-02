# Neural Networks: An Overview

## What is a Neural Network?
A neural network is a computational model inspired by the structure and function of the human brain. It consists of interconnected layers of neurons that process and transform input data to produce meaningful outputs. Neural networks are widely used in tasks such as image recognition, natural language processing, and predictive analytics.

## What is Forward Propagation?
Forward propagation is the process where input data passes through the network layer by layer until it produces an output. Each layer applies transformations using weights, biases, and activation functions to refine the data and generate predictions.

### Components of Forward Propagation:
#### 1. Input Layer
- The first layer of the network.
- Receives raw input data (e.g., images, text, numerical values).
- The number of neurons equals the number of features in the dataset (e.g., car age, engine power).

#### 2. Hidden Layers
- Where most of the computations take place.
- Each neuron in a hidden layer:
  - Computes a weighted sum of inputs from the previous layer.
  - Adds a bias term.
  - Applies an activation function.
- The number of hidden layers and neurons per layer depends on the network architecture.

#### 3. Output Layer
- The final layer of the network.
- Produces the final prediction or classification result.
- The number of neurons in the output layer depends on the task type:
  - **Binary Classification:** 1 neuron with a Sigmoid activation function.
  - **Multi-class Classification:** Multiple neurons with a Softmax activation function.
  - **Regression Tasks:** 1 neuron with no activation or linear activation.

### Keywords:
**Bias:** A constant added to the weighted sum of inputs in each neuron, allowing the activation function to shift for better fitting of data.

## What is Backward Propagation?
Backward propagation (backpropagation) is the learning process where the model updates its parameters after making predictions. It minimizes the prediction error by adjusting weights and biases using the gradient of the loss function.

### Steps in Backward Propagation:
#### 1. Loss Calculation
- After forward propagation, the network outputs a prediction.
- The difference between the prediction and the actual value is the **error**.
- The **loss function** quantifies the magnitude of this error:
  - **Regression:** Mean Squared Error (MSE) is commonly used.
  - **Classification:** Cross-Entropy Loss is often applied.

#### 2. Compute Gradients
- The objective is to determine how each weight and bias contributes to the loss.
- The gradient of the loss function is computed using the **chain rule of calculus**.
- Gradients indicate the direction and magnitude of adjustments needed.

#### 3. Backpropagation Through Layers
- **Output Layer:**
  - Calculate how much the loss changes with respect to the output neurons.
  - Use derivatives of activation functions (e.g., Sigmoid, Softmax) to compute gradients.
- **Hidden Layers:**
  - Propagate the error backward through each layer.
  - Compute the gradient for each neuron’s weights and biases.
  - Use derivatives of activation functions (e.g., ReLU, Sigmoid, Tanh) for updates.
- **Input Layer:**
  - Continue backpropagating gradients to the input layer.
  - While weights are not typically updated at this stage, these gradients influence earlier layers’ updates.

## Summary
Neural networks operate through forward propagation to make predictions and backward propagation to refine their parameters. This iterative learning process allows the model to improve over time by minimizing error and optimizing performance.

