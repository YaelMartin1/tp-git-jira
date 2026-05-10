# PROY 2
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/ventas.csv")

df["total"] = df["cantidad"] * df["precio"]

ventas_totales = df["total"].sum()

producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

ventas_por_producto = df.groupby("producto")["total"].sum()

ventas_por_producto.plot(kind="bar")

plt.title("Ventas por Producto")

plt.savefig("resultados/grafico_ventas.png")

plt.show()
