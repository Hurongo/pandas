import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)


n = 50

time = np.linspace(0, 10, n)

acceleration = np.random.uniform(-2, 2, size=n)

# Обчислення швидкості шляхом накопичення прискорення
velocity = np.cumsum(acceleration) * (time[1] - time[0])

# Обчислення позиції шляхом інтегрування швидкості
position = np.cumsum(velocity) * (time[1] - time[0])

# Створення DataFrame
df = pd.DataFrame({
    'Час': time,
    'Позиція': position,
    'Швидкість': velocity,
    'Прискорення': acceleration
})

# Обчислення середньої швидкості і прискорення
mean_velocity = df['Швидкість'].mean()
mean_acceleration = df['Прискорення'].mean()

print(" Середня швидкість: {:.2f} м/с".format(mean_velocity))
print(" Середнє прискорення: {:.2f} м/с^2".format(mean_acceleration))

# --- Графіки ---

# Позиція від часу
plt.figure(figsize=(8, 5))
plt.plot(df['Час'], df['Позиція'], color='blue')
plt.xlabel('Час (с)')
plt.ylabel('Позиція (м)')
plt.title('Позиція від часу')
plt.grid(True)
plt.show()

# Швидкість від часу
plt.figure(figsize=(8, 5))
plt.plot(df['Час'], df['Швидкість'], color='green')
plt.xlabel('Час (с)')
plt.ylabel('Швидкість (м/с)')
plt.title('Швидкість від часу')
plt.grid(True)
plt.show()

# Прискорення від часу
plt.figure(figsize=(8, 5))
plt.plot(df['Час'], df['Прискорення'], color='red')
plt.xlabel('Час (с)')
plt.ylabel('Прискорення (м/с^2)')
plt.title('Прискорення від часу')
plt.grid(True)
plt.show()
