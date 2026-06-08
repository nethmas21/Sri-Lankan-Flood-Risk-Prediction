import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/sri_lanka_flood_risk_dataset_25000.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFlood Occurrence Counts:")
print(df["flood_occurrence_current_event"].value_counts())

print("\nFlood Occurrence Percentage:")
print(df["flood_occurrence_current_event"].value_counts(normalize=True)*100)

print("\nMissing Values:")
print(df.isnull().sum())

flood_counts = df["flood_occurrence_current_event"].value_counts()

plt.figure(figsize=(6,4))
flood_counts.plot(kind="bar")

plt.title("Flood Occurrence Distribution")
plt.xlabel("Flood Occurrence")
plt.ylabel("Count")

plt.figure(figsize=(8,5))

sns.boxplot(
    x="flood_occurrence_current_event",
    y="monthly_rainfall_mm",
    data=df
)

plt.title("Monthly Rainfall vs Flood Occurrence")
plt.xlabel("Flood Occurrence")
plt.ylabel("Monthly Rainfall (mm)")

plt.tight_layout()
plt.show()


plt.tight_layout()
plt.show()

# --------------------------
# Graph 3 - Floods by District
# --------------------------

flooded = df[df["flood_occurrence_current_event"] == "Yes"]

top_districts = flooded["district"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_districts.plot(kind="bar")

plt.title("Top 10 Flood-Prone Districts")
plt.xlabel("District")
plt.ylabel("Number of Flood Events")

plt.tight_layout()
plt.show()

# --------------------------
# Graph 4 - Correlation Heatmap
# --------------------------

numeric_df = df.select_dtypes(include=["int64", "float64"])

plt.figure(figsize=(12,8))
sns.heatmap(numeric_df.corr(), cmap="coolwarm", annot=False)

plt.title("Correlation Heatmap of Numeric Features")
plt.tight_layout()
plt.show()