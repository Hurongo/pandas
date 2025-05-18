import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Завантаження Excel-файлу
df = pd.read_excel('voltage.xlsx')

# Заміна назв колонок для зручності
df.columns = ['Voltage', 'Current', 'Iabs', 'Uabs', 'I/U', '1/U', 'I/U^2', 'U^0.5', 'logI']

# Переконаємось, що всі колонки числові
df = df.apply(pd.to_numeric, errors='coerce')

# Фільтрація значень для стабільності log10
df = df[(df['Iabs'] > 0) & (df['Uabs'] > 0)]

# Обчислення додаткових колонок для графіків
df['log_abs_current'] = np.log10(np.abs(df['Current']))
df['log_I_U'] = np.log10(df['Iabs'] / df['Uabs'])
df['log_I_U2'] = np.log10(df['Iabs'] / df['Uabs']**2)
df['sqrt_U'] = np.sqrt(df['Uabs'])

# Графік 1: Омічна провідність
plt.figure(figsize=(10, 6))
plt.plot(df['Voltage'], df['log_abs_current'], label='log10(|Current|) vs Voltage', color='blue')
plt.xlabel('Voltage (V)')
plt.ylabel('log10(|Current|)')
plt.title('Омічна провідність')
plt.grid(True)
plt.legend()
plt.show()

# Графік 2: Інжекційна провідність
plt.figure(figsize=(10, 6))
plt.plot(df['1/U'], df['log_I_U'], label='log10(I/U) vs 1/U', color='green')
plt.xlabel('1 / Uabs')
plt.ylabel('log10(I/U)')
plt.title('Інжекційна провідність')
plt.grid(True)
plt.legend()
plt.show()

# Графік 3: Провідність Фаулера-Нордгейма
plt.figure(figsize=(10, 6))
plt.plot(df['1/U'], df['log_I_U2'], label='log10(I/U^2) vs 1/U', color='red')
plt.xlabel('1 / Uabs')
plt.ylabel('log10(I/U^2)')
plt.title('Провідність за Фаулера-Нордгеймом')
plt.grid(True)
plt.legend()
plt.show()

# Графік 4: Провідність Пула-Френкеля
plt.figure(figsize=(10, 6))
plt.plot(df['sqrt_U'], df['log_I_U'], label='log10(I/U) vs sqrt(U)', color='purple')
plt.xlabel('sqrt(Uabs)')
plt.ylabel('log10(I/U)')
plt.title('Провідність Пула-Френкеля')
plt.grid(True)
plt.legend()
plt.show()

# Пошук екстремумів
min_current = df['Current'].min()
max_current = df['Current'].max()
min_voltage = df['Voltage'].min()
max_voltage = df['Voltage'].max()

print("🔽 Найменший струм:", min_current)
print("🔼 Найбільший струм:", max_current)
print("🔽 Найменша напруга:", min_voltage)
print("🔼 Найбільша напруга:", max_voltage)
