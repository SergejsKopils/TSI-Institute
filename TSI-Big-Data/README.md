# 🧠 Big Data Project: Structured & Unstructured Data Analysis

## 📌 Project Overview

This project demonstrates end-to-end data processing and analysis for both **structured (CSV)** and **unstructured (JSON)** datasets. It includes data cleaning, transformation, visualization, and ontology creation using semantic web technologies.

---

## 📂 Dataset Description

### 📑 Structured Data (CSV)
- **Rows**: 50,000 transactions
- **Fields**: Customer ID, Name, Gender, Birthdate, Transaction Amount, Merchant Name, Category, Date

### 📘 Unstructured Data (JSON)
- **Source**: Amazon Musical Instruments Reviews
- **Rows**: 10,261 reviews
- **Fields**: Reviewer ID, Review Text, Helpfulness, Overall Rating, Summary, Date

---

## ⚙️ Steps Performed

### 1. Data Cleaning
- Handled missing values (`Gender`, `reviewerName`)
- Parsed date fields (`Birthdate`, `Date`, `reviewTime`)
- Removed duplicates and validated data types

### 2. Feature Engineering
**Structured:**
- Calculated `Age`
- Extracted `Transaction_Year`, `Transaction_Month`, `Transaction_Day`
- Encoded `Gender` and `Category`
- Normalized `Transaction Amount`

**Unstructured:**
- Calculated `sentiment polarity` using `TextBlob`
- Computed `helpfulness_score` from `[helpful votes / total votes]`
- Extracted `reviewYear`

### 3. Data Analysis & Visualization

#### 📊 Structured Dataset
- **Top 5 Spending Categories**
- **Avg. Transaction by Gender**
- **Avg. Transaction by Age Group**
- **Monthly Transaction Trends**

#### 📝 Unstructured Dataset
- **Sentiment Distribution**
- **Helpfulness Score Distribution**
- **Yearly Review Activity**

> Plots were created using `matplotlib` and `seaborn`

### 4. Ontology Creation (RDF)
- Used `rdflib` to model relationships between:
  - Customers
  - Products
  - Reviews
- Added semantic triples such as:
  - `Customer → writesReview → Review`
  - `Review → ratesProduct → Product`
  - `Customer → buysProduct → Product`
- Exported to `ontology_output.rdf` (RDF/XML format)

---

## 🧪 Key Results

- Most spending occurred in Category `5` (e.g., Electronics or Market)
- Highest spending by Age Group `51–65`
- Peak transaction months: **May and July**
- Sentiment analysis showed mostly positive reviews (avg polarity ≈ 0.25)
- Most reviews had **low helpfulness scores**, with a peak review activity in **2013**

---

## 🛠️ Technologies Used

- **Python**, **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **TextBlob** (for sentiment analysis)
- **rdflib** (for RDF ontology creation)
- **Jupyter Notebook**

