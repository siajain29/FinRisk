# FinRisk — Explainable Credit Default Risk Prediction

FinRisk is an end-to-end machine learning application that predicts the probability of credit card default and provides interpretable risk explanations using SHAP.

The project combines exploratory data analysis, feature engineering, imbalanced classification, model comparison, threshold optimization, explainable AI, and Streamlit deployment.

---

## 🚀 Project Overview

FinRisk predicts whether a customer is likely to default on their credit card payment based on demographic, credit, repayment, billing, and payment history.

The application provides:

- Default probability
- Low / Medium / High risk classification
- SHAP-based prediction explanations
- Model performance comparison
- Interactive Streamlit interface

---

## 🧠 Machine Learning Pipeline

```text
Customer Financial Data
          ↓
Data Cleaning & EDA
          ↓
Feature Engineering
          ↓
34 Predictive Features
          ↓
Train / Test Split
          ↓
Class Imbalance Handling
          ↓
Model Comparison
          ↓
XGBoost Selection
          ↓
Threshold Optimization
          ↓
Risk Classification
          ↓
SHAP Explainability
          ↓
Streamlit Application