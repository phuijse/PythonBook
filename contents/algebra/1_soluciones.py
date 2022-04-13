# Ejercicio linalg.inv

A = np.array([[-1., 5.], [2., 3.]])
b = np.array([2., 1.])

assert not np.linalg.det(A) == 0, "Determinante igual a cero"
assert np.linalg.matrix_rank(A) == A.shape[1], "Matriz no LI"

display(np.dot(np.linalg.inv(A), A))

fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
x1 = np.linspace(-0.5, 0.5, num=100)
x2_1 = (b[0] - A[0, 0]*x1)/A[0, 1]
x2_2 = (b[1] - A[1, 0]*x1)/A[1, 1]
ax.plot(x1, x2_1, 'k-', lw=2, label='Eq. 1')
ax.plot(x1, x2_2, 'k--', lw=2, label='Eq. 2')
ax.grid(); ax.legend();
ax.set_xlabel(r'$x_1$'); ax.set_ylabel(r'$x_2$');

# Ejercicio linalg.lstsq

temperatura = df["temp"].values
consumo = df["cons"].values

A = np.ones(shape=(temperatura.shape[0], 2))
A[:, 1] = temperatura

x, _, _, _ = np.linalg.lstsq(A, consumo, rcond=None)
display(x)


fig, ax = plt.subplots(figsize=(4, 4), tight_layout=True)
ax.scatter(temperatura, consumo); 
ax.set_xlabel('Temperatura [F]'); 
ax.set_ylabel('Consumo promedio');
x_plot = np.linspace(np.amin(temperatura), np.amax(temperatura), num=100)
ax.plot(x_plot, x_plot*x[1] + x[0], 'k-', lw=2)