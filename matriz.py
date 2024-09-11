import numpy as np
A = np.array([
    [0.52, 0.20, 0.25],
    [0.30, 0.50, 0.20],
    [0.18, 0.30, 0.55]
])

B = np.array([4800, 5810, 5690])

# Calcular la inversa de la matriz

A_inv = np.linalg.inv(A)
print("La inversa de la matriz A es:")
print(A_inv)
    
X = np.dot(A_inv, B)
print("\nLa cantidad de material a transportar desde cada cantera es:")
print("Cantera 1: {:.2f} m³".format(X[0]))
print("Cantera 2: {:.2f} m³".format(X[1]))
print("Cantera 3: {:.2f} m³".format(X[2]))
