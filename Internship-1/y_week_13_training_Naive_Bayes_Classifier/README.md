# Week 13 Training: Naive Bayes Classifier

## Overview
This training assignment focuses on implementing a **Naive Bayes Classifier** for binary classification. The objectives include performing Exploratory Data Analysis (EDA), preprocessing a chosen dataset, implementing a Gaussian Naive Bayes model, and evaluating its performance. Additionally, the task involves summarizing the Bayesian Optimization Algorithm paper.

## Objectives
1. Implement a **Naive Bayes classifier** for any dataset of your choice.
   - Write a problem statement explaining the problem it solves.
   - Ensure it is a **binary classification** problem.
2. Implement a solution for **Logistic Regression** that can be used as a classifier.
3. Your code should contain a **well-defined Exploratory Data Analysis (EDA)**.
4. Write a coherent summary for **Bayesian Optimization Algorithm**.
---

## Files and Links

- [Naive Bayes Classifier Model (Jupyter Notebook)](naive_bays_classifier_model.ipynb)
- [Summary of Bayesian Optimization Algorithm](summaryBayesianOptimizationAlgorithm.md)


## Loan risk Naive Bayes classifier

This project aims to predict loan repayment failure based on financial history and credit factors, helping lenders assess default risk. Using a LendingClub dataset, the target variable is not_fully_paid (1 for non-repayment, 0 otherwise) with features like credit score, debt-to-income ratio, and loan interest rate. The project includes Exploratory Data Analysis (EDA), data preprocessing, and modeling with Gaussian Naive Bayes, evaluated using accuracy, F1-score, and confusion matrix. [Naive Bayes Classifier Model (Jupyter Notebook)](naive_bays_classifier_model.ipynb)

---

## Bayesian Optimization Algorithm Summary
Bayesian Optimization is a **probabilistic model-based approach** for optimizing expensive functions, commonly used for hyperparameter tuning. It builds a **Gaussian Process (GP) model** to estimate function behavior and selects new evaluation points using **acquisition functions** like Expected Improvement (EI) and Upper Confidence Bound (UCB). By balancing exploration and exploitation, it reduces evaluations needed for optimization, making it more efficient than grid or random search. [Summary of Bayesian Optimization Algorithm](summaryBayesianOptimizationAlgorithm.md)

---

## References
- [Naive Bayes classifier: A friendly approach](https://www.youtube.com/watch?v=Q8l0Vip5YUw)
- [Bayesian Optimization Paper](https://arxiv.org/abs/1206.2944)
- [Kaggle: Loan Data](https://www.kaggle.com/itssuru/loan-data)
