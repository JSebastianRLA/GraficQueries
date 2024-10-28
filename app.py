import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Leer los datos
df = pd.read_csv('dns_queries_graficador.csv', parse_dates=['timestamp'])

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar consultas por segundo a lo largo del tiempo
ax.plot(df['timestamp'], df['queries_per_second'], marker='o', color='blue', linestyle='-', linewidth=2, markersize=5, alpha=0.7)

# Título y etiquetas
ax.set_title('DNS Queries per Second Over Time', fontsize=16, fontweight='bold', color='darkblue')
ax.set_xlabel('Time', fontsize=12, fontweight='bold', color='darkgreen')
ax.set_ylabel('Queries per Second', fontsize=12, fontweight='bold', color='darkgreen')

# Formatear las fechas en el eje X
date_format = DateFormatter("%Y-%m-%d %H:%M")
ax.xaxis.set_major_formatter(date_format)
plt.xticks(rotation=45)

# Añadir un fondo y grid personalizados
ax.set_facecolor('#f5f5f5')
ax.grid(visible=True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

# Añadir una leyenda opcional (si tienes más de una línea)
# ax.legend(['DNS Queries'], loc='upper left')

# Personalizar el estilo de los ticks
ax.tick_params(axis='x', labelsize=10, rotation=45)
ax.tick_params(axis='y', labelsize=10)

# Mostrar la gráfica
plt.tight_layout()  # Para ajustar los márgenes
plt.show()
