import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

proyectos = [
    'Capítulo I: El Problema',
    '  1.1 Planteamiento del problema',
    '  1.2 Formulación del problema',
    '  1.3 Objetivos de la investigación',
    '  1.4 Justificación de la investigación',
    'Capítulo II: Marco Teórico',
    '  2.1 Antecedentes de la investigación',
    '  2.2 Bases Teóricas',
    '  2.3 Bases Legales',
    '  2.4 Definición de términos',
    'Capítulo III: Marco Metodológico',
    '  3.1 Tipo de Investigación',
    '  3.2 Diseño de Investigación',
    '  3.3 Población y Muestra',
    '  3.4 Técnicas e Instrumento',
    '  3.5 Validez y Confiabilidad'
]

fechas_inicio = [
    datetime.date(2025, 5, 12), datetime.date(2025, 5, 12), datetime.date(2025, 5, 26), datetime.date(2025, 5, 29), datetime.date(2025, 6, 6),
    datetime.date(2025, 6, 19), datetime.date(2025, 6, 19), datetime.date(2025, 7, 16), datetime.date(2025, 8, 21), datetime.date(2025, 9, 2),
    datetime.date(2025, 9, 7), datetime.date(2025, 9, 7), datetime.date(2025, 9, 11), datetime.date(2025, 9, 15), datetime.date(2025, 9, 18),
    datetime.date(2025, 9, 21)
]

fechas_fin = [
    datetime.date(2025, 6, 18), datetime.date(2025, 5, 25), datetime.date(2025, 5, 28), datetime.date(2025, 6, 5), datetime.date(2025, 6, 18),
    datetime.date(2025, 9, 6), datetime.date(2025, 7, 15), datetime.date(2025, 8, 20), datetime.date(2025, 9, 1), datetime.date(2025, 9, 6),
    datetime.date(2025, 9, 22), datetime.date(2025, 9, 10), datetime.date(2025, 9, 14), datetime.date(2025, 9, 17), datetime.date(2025, 9, 20),
    datetime.date(2025, 9, 22)
]

plt.style.use("seaborn-v0_8-whitegrid")  

fig, ax = plt.subplots(figsize=(14, 8))

for i, (inicio, fin) in enumerate(zip(fechas_inicio, fechas_fin)):
    ax.barh(
        proyectos[i],
        (fin - inicio).days,
        left=inicio,
        height=0.35,  # más delgadas
        color=plt.cm.Blues(0.3 + 0.7 * (i / len(proyectos))),  # gradiente azul suave
        alpha=0.9
    )

ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%b"))

# Invertir orden
ax.invert_yaxis()

plt.title("Cronograma de Actividades", fontsize=18, fontweight="bold", color="#2C3E50")
plt.xlabel("Fecha", fontsize=12, fontweight="medium")
plt.ylabel("Actividades", fontsize=12, fontweight="medium")
plt.xticks(rotation=45, fontsize=10, color="#34495E")
plt.yticks(fontsize=9, color="#2C3E50")


for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)

ax.grid(axis="x", color="gray", linestyle="--", linewidth=0.5, alpha=0.5)
ax.grid(axis="y", visible=False)

plt.tight_layout()
plt.show()
