# Machine Learning 2 – Exercise Solutions

**Author:** Taha El Amine Kassabi  
**Course:** Machine Learning 2 (WS 2023/24)  
**Instructor:** Prof. Dr. Dominik Heider  
**University:** Heinrich Heine University Düsseldorf (HHU)

---

## 📚 Overview

This repository contains solutions to all 11 exercises from the Machine Learning 2 course at HHU. Each assignment covers
foundational or advanced topics in classical machine learning — from matrix manipulation and statistics to support
vector machines and neural networks. Most solutions consist of Jupyter notebooks, supplementary markdown or PDF answers,
and linked datasets.

---

## 📂 Repository Structure

```
Sheets/
├── Sheet 0 – Conda, YAML, file IO
├── Sheet 1 – Text processing & matrices
├── Sheet 2 – Descriptive statistics, correlation
├── Sheet 3 – PCA & MDS (PCoA)
├── Sheet 4 – Clustering (K-Means, Hierarchical)
├── Sheet 5 – Linear and logistic regression
├── Sheet 6 – k-Nearest Neighbors
├── Sheet 7 – Support Vector Machines
├── Sheet 8 – Decision Trees
├── Sheet 9 – Random Forest & Performance Measures
└── Sheet 10 – Neural Nets, Backprop, CNN filters
```

Each folder includes a task sheet (`exercise_N.pdf`) and data or helper files. Solutions are
under `Solutions/Exercise N`.

---

## 🧠 Topics Covered

| Exercise | Topics                                                                         |
|----------|--------------------------------------------------------------------------------|
| 0        | Conda setup, YAML, reading/writing files                                       |
| 1        | Text parsing, matrix algebra                                                   |
| 2        | Descriptive stats, skewness, correlation                                       |
| 3        | PCA & classical MDS                                                            |
| 4        | K-means, silhouettes, hierarchical clustering                                  |
| 5        | Linear regression, logistic regression                                         |
| 6        | k-Nearest Neighbors (k-NN), normalization                                      |
| 7        | SVM, Lagrange multipliers, separating hyperplanes                              |
| 8        | Decision trees, information gain, Gini                                         |
| 9        | Random forests, Gini importance, AUC, precision/recall                         |
| 10       | McCulloch/Pitts networks, backpropagation, CNN filters, MNIST training (bonus) |

---

## 💾 Setup

```bash
pip install -r requirements.txt
```

You may also use JupyterLab or Google Colab for individual notebooks.

---

## 🚀 Usage

Navigate to any exercise in `Solutions/Exercise N`, open the notebook(s), and run the cells. Some tasks also
include `.md`, `.pdf`, or `.docx` explanations for handwritten answers.

---

## 📝 Notes

- Most exercises were completed using Python with **NumPy**, **Pandas**, **Matplotlib**, **Scikit-learn**, and **SciPy
  **.
- For neural networks (Exercise 10 bonus), models were implemented using **Keras/TensorFlow** and **PyTorch**.
