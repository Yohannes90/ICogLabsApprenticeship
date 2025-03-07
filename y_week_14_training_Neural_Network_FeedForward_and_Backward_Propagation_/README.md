# **Week 14 Training: Neural Networks – Feedforward and Backpropagation Implementation**

## **Overview**
This training assignment focuses on implementing backpropagation for a neural network previously built using forward propagation. The objectives include performing forward propagation, implementing backpropagation for weight and bias updates, and evaluating the differences in performance between the two approaches.

## **Objectives**
- Implement a **feedforward-only model** without backpropagation.
- Implement a **neural network model with backpropagation**.
- Compare the performance of the two approaches using accuracy and loss metrics.
- Analyze the effect of weight updates on model performance.

## **Implementation Details**
- **Dataset**: Iris dataset (three-class classification).
  - Features are standardized using `StandardScaler`.
  - Labels are one-hot encoded using `LabelEncoder`.
  - The dataset is split into **training (80%)** and **testing (20%)** sets.
- **Model Architecture**:
  - **Input Layer**: 4 features
  - **Hidden Layer**: 10 neurons with **ReLU** activation
  - **Output Layer**: 3 neurons with **Softmax** activation
- **Loss Function**: Cross-entropy loss
- **Optimization**: Manual gradient descent with a learning rate of `0.01`
- **Evaluation Metric**: Accuracy on the test set

## **Training Approaches**
### **1. Feedforward-Only Model**
- The model initializes random weights and biases.
- Forward propagation is performed, but **no backpropagation** is applied.
- The loss is calculated at each epoch, but weights remain unchanged.
- Since learning does not occur, accuracy remains low.

### **2. Backpropagation Model**
- Forward propagation computes activations.
- Backpropagation calculates gradients for weight and bias updates.
- The loss function used is cross-entropy.
- The model updates weights using gradient descent.

The results demonstrate that the backpropagation model significantly improves classification accuracy compared to the feedforward-only model.

## **Key Findings**
### **1. Feedforward-Only Model (No Backpropagation)**
- Accuracy **stalls at ~43.33%** since weights are not updated.
- The loss remains constant throughout training due to the absence of learning.
- The model fails to generalize well to the test data.

### **2. Backpropagation Model (With Training)**
- Accuracy **reaches ~96.67%**, showing a major improvement.
- Loss decreases progressively as the model learns optimal weights.
- The model can continue improving but may risk **overfitting** if trained excessively.

| Model                  | Accuracy  |
|------------------------|----------|
| **Feedforward-Only**   | 43.33%   |
| **Backpropagation**    | 96.67%   |

## **Code File**
- [`backpropagation_vs_feedforward.py`](./backpropagation_vs_feedforward.py)

## **Conclusion**
Backpropagation is essential for training a neural network effectively. Without weight updates, a model cannot improve its predictions beyond a baseline accuracy (in this case, **43.33%**). However, while backpropagation significantly enhances performance, **overfitting** remains a risk if training continues without proper regularization techniques.
