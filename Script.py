import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# =======================
# Save Path Setup
# =======================
documents_path = os.path.join(os.path.expanduser("~"), "Documents", "Titanic_Visuals")
os.makedirs(documents_path, exist_ok=True)

# =======================
# Load Data
# =======================
print("\n STEP 1: Loading Dataset")
df = pd.read_csv("tested.csv")

print("\n=== Dataset Info ===")
print(df.info())
print("\n=== Summary Statistics ===")
print(df.describe())

# Encode categorical for correlation
df_encoded = df.copy()
df_encoded['Sex'] = df_encoded['Sex'].map({'male': 0, 'female': 1})
df_encoded['Embarked'] = df_encoded['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# =======================
# Correlation Heatmap
# =======================
plt.figure(figsize=(8, 6))
sns.heatmap(df_encoded.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap (Encoded Features)", fontsize=14, weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(documents_path, "correlation_heatmap.png"))
plt.show()

# =======================
# Pairplot
# =======================
pairplot_fig = sns.pairplot(df, vars=['Age', 'Fare', 'Pclass', 'SibSp', 'Parch'], hue='Survived', diag_kind='kde')
pairplot_fig.fig.suptitle("Pairplot of Key Features by Survival", y=1.02, fontsize=14, weight='bold')
pairplot_fig.savefig(os.path.join(documents_path, "pairplot.png"))
plt.show()

# =======================
# Histograms
# =======================
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']
df[numeric_cols].hist(bins=20, figsize=(10, 8), edgecolor='black')
plt.suptitle("Histograms of Numeric Features", fontsize=14, weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(documents_path, "histograms.png"))
plt.show()

# =======================
# Box Plots
# =======================
plt.figure(figsize=(10, 6))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}', fontsize=12, weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(documents_path, "boxplots.png"))
plt.show()

# =======================
# Scatter Plots
# =======================
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived', palette='coolwarm')
plt.title("Scatter Plot: Age vs Fare (Survival Highlighted)", fontsize=14, weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(documents_path, "scatter_age_fare.png"))
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Pclass', y='Fare', hue='Survived', palette='coolwarm')
plt.title("Scatter Plot: Pclass vs Fare (Survival Highlighted)", fontsize=14, weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(documents_path, "scatter_pclass_fare.png"))
plt.show()

# =======================
# Grouped Box Plots
# =======================
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Sex', y='Age', hue='Survived')
plt.title("Age Distribution by Sex and Survival", fontsize=14, weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(documents_path, "groupedbox_age_sex_survival.png"))
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Pclass', y='Fare', hue='Survived')
plt.title("Fare Distribution by Class and Survival", fontsize=14, weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(documents_path, "groupedbox_fare_class_survival.png"))
plt.show()

print(f"\n All visuals saved in: { r"C:\Users\dell\Documents"}")


