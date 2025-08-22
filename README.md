# Titanic Visual Analysis Report

## 📌 Overview
This repository contains a **visual exploratory data analysis (EDA)** of the Titanic dataset, prepared by **Niyansha Dubey**.  
It explores relationships between passenger characteristics and survival outcomes using multiple visualizations, with detailed insights provided for each plot.  
The analysis is based on the dataset `tested.csv` from [Kaggle's Titanic Dataset](https://www.kaggle.com/datasets/brendan45774/test-file).

## 📂 Repository Structure
- **Script.py** – Python script that loads the dataset, processes it, and generates visualizations.  
- **tested.csv** – Dataset used for analysis (from Kaggle).  
- **titanic_visual_analysis.pdf** – Full PDF report containing visuals and insights.  

## 📊 Report Contents
1. **Introduction Page** – Purpose of the report and summary of the analysis.  
2. **Correlation Heatmap** – Shows linear relationships between encoded features.  
3. **Boxplots** – Displays distributions and outliers for Age, Fare, SibSp, and Parch.  
4. **Age Distribution by Sex and Survival** – Highlights gender-based survival differences across age groups.  
5. **Fare Distribution by Class and Survival** – Shows how ticket price and passenger class impact survival.  
6. **Histograms** – Frequency distributions of numeric features.  
7. **Pairplot** – Multi-feature comparison with survival status highlighted.  
8. **Scatter Plots** – Age vs Fare and Pclass vs Fare, both color-coded by survival status.  

## 🔍 Key Insights
- **Fare vs Class**: First-class passengers paid significantly more and had higher survival rates.  
- **Gender Impact**: Female passengers had a much higher probability of survival compared to males.  
- **Outliers**: Found in Fare, SibSp, and Parch, indicating unusual passenger cases.  
- **Class Effect**: Passengers in lower classes generally had reduced survival chances.  

## 🛠 How It Was Made
- **Language**: Python  
- **Libraries Used**: Pandas, Matplotlib, Seaborn.  
- **Process**:  
  1. Load dataset (`tested.csv`) from Kaggle.  
  2. Perform basic cleaning and encoding.  
  3. Generate visualizations with Matplotlib & Seaborn.  
  4. Export plots as PNG files.  
  5. Compile visuals and explanations into a PDF using ReportLab.  

## 📄 Dataset Source
- Dataset: [`tested.csv`](https://www.kaggle.com/datasets/brendan45774/test-file)  
- Source: [Kaggle Titanic Dataset](https://www.kaggle.com/datasets/brendan45774/test-file)

## 👩‍💻 Author
**Niyansha Dubey**

---


