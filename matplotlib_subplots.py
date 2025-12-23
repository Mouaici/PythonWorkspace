import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employees_updated.csv')

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(df['Name'], df['Salary'])
axes[0].set_title("Salaries")
axes[0].set_xlabel("Name")
axes[0].set_ylabel("Salary")
axes[0].tick_params(axis='x', rotation=30)

axes[1].scatter(df['Age'], df['Salary'])
axes[1].set_title("Age vs Salary")
axes[1].set_xlabel("Age")
axes[1].set_ylabel("Salary")
axes[1].grid(True)

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].bar(df['Name'], df['Salary'])
axes[0, 0].set_title("Salary")

axes[0, 1].plot(df['Name'], df['Salary_Raised'], marker='o')
axes[0, 1].set_title("Raised Salary")

axes[1, 0].pie(df['Department'].value_counts(),
               labels=df['Department'].value_counts().index,
               autopct='%1.1f%%')
axes[1, 0].set_title("Departments")

axes[1, 1].scatter(df['Age'], df['Salary'])
axes[1, 1].set_title("Age vs Salary")

plt.tight_layout()
plt.show()
