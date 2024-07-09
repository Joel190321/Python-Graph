import matplotlib.pyplot as plt

velocidad_antes = [3.50, 3.81, 3.46, 4.20]
velocidad_rebote = [3.19, 3.43, 3.65, 3.86]

plt.scatter(velocidad_antes, velocidad_rebote, color='blue')

plt.plot(velocidad_antes, velocidad_rebote, color='red', linestyle='--')

plt.xlabel('Velocidad antes de chocar (m/s)')
plt.ylabel('Velocidad inicial del rebote (m/s)')
plt.title('Velocidad inicial del rebote vs. Velocidad antes de chocar')

plt.grid(True)
plt.show()
