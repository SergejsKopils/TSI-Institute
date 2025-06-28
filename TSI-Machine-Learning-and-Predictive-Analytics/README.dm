# 🧠 Mushroom Risk Prediction and Grouping

This project was developed as part of the **Machine Learning and Predictive Analytics** course at Transport and Telecommunication Institute (TSI).

## 📂 Project Structure
- `Sergejs_Kopils_ST83519_20241222_CP_ML.ipynb`: Main notebook with all steps of the machine learning pipeline
- `primary_data.csv`: Raw dataset containing mushroom features and class labels
- `Sergejs_Kopils_ST83519_20241222_CP_ML.pdf`: Final submitted report

## 📊 Objective
The goal of this project is to:
- Predict whether a mushroom is **edible or poisonous** using supervised learning (Logistic Regression)
- Discover **natural groupings** in the data using unsupervised learning (K-Means Clustering)

## 🔧 Methods Used

### 🔹 Data Preprocessing
- Cleaned malformed CSV lines
- Filled missing values with the mode
- Encoded categorical features using `LabelEncoder`
- Scaled numerical features with `StandardScaler`

### 🔹 Classification: Logistic Regression
- Binary classification model (edible vs. poisonous)
- Evaluated with **accuracy**, **precision**, **recall**, **F1-score**, and **AUC**
- Accuracy: ~63%, AUC: 0.56
- Cross-validation (10-fold) confirms stability of results

### 🔹 Clustering: K-Means
- Used **Elbow method** and **Silhouette score** to choose optimal `k`
- Visualized clusters with PCA (2D)
- Silhouette Score: 0.085 (suggests weak natural clusters in this dataset)

## 📈 Tools and Libraries
- Python (`pandas`, `numpy`, `scikit-learn`)
- Visualization: `matplotlib`, `seaborn`

## 📎 Files
| File Name | Description |
|-----------|-------------|
| `Sergejs_Kopils_ST83519_20241222_CP_ML.ipynb` | Full notebook with code, EDA, modeling |
| `primary_data.csv` | Original raw data |
| `Sergejs_Kopils_ST83519_20241222_CP_ML.pdf` | Report summarizing the analysis and results |
