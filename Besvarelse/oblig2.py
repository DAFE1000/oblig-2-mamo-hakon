import numpy as np
import matplotlib.pyplot as plt

# definere funksjon
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# range for x-verdier, y-verdier = f(x) (funksjonen definert over)
x_values = np.linspace(0, 8, 200000)
y_values = f(x_values)

# finner makspunkt, i_max = der y-verdi er størst
# x_max = x-verdien der y (f(x)) er størst, y_max = y-verdien der y er størst
i_max = np.argmax(y_values)
x_max = x_values[i_max]
y_max = y_values[i_max]

# henter variabelverdi for x_max, begrenser til 4 desimaler (.4f)
print(f"makspunkt: x = {x_max:.4f}")

# plot, scatter for makspunkt
plt.figure(figsize=(8,5))
plt.plot(x_values, y_values)
plt.scatter(x_max, y_max, color="red", label=f"makspunkt: x = {x_max:.4f}")
plt.title("f(x) = e^(-x/4) * tan^(-1)x")
plt.grid(True)
plt.legend()
plt.show()