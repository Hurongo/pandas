import pandas as pd
import matplotlib.pyplot as plt

# Зчитування CSV-файлу
df = pd.read_csv('company_sales_data - company_sales_data.csv')

# Побудова гістограми (facecream і facewash по місяцях)
months = df['month_number']
plt.bar(months - 0.2, df['facecream'], width=0.4, label='Face Cream', color='skyblue')
plt.bar(months + 0.2, df['facewash'], width=0.4, label='Face Wash', color='lightgreen')

# Декорації
plt.title('Місячні продажі: крем і засіб для вмивання')
plt.xlabel('Місяць')
plt.ylabel('Продажі (одиниць)')
plt.xticks(months)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
