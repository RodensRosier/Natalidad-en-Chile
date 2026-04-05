import pandas as pd
import matplotlib.pyplot as plt

# Datos históricos aproximados (INE Chile)
data = {
    'Año': [1990, 2000, 2010, 2020, 2023, 2024],
    'Nacimientos': [300000, 260000, 250000, 195000, 170000, 155000],
    'Tasa_Fecundidad': [2.6, 2.0, 1.9, 1.5, 1.3, 1.2]
}
df_natalidad = pd.DataFrame(data)

# Visualización de la caída
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('Año')
ax1.set_ylabel('Total Nacimientos', color='tab:blue')
ax1.plot(df_natalidad['Año'], df_natalidad['Nacimientos'], color='tab:blue', marker='o', linewidth=3)

ax2 = ax1.twinx()
ax2.set_ylabel('Tasa de Fecundidad (Hijos por mujer)', color='tab:red')
ax2.plot(df_natalidad['Año'], df_natalidad['Tasa_Fecundidad'], color='tab:red', linestyle='--', marker='s')

plt.title('El Colapso de la Natalidad en Chile (1990-2024)')
plt.grid(True, alpha=0.3)
plt.show()
