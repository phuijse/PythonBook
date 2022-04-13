# Regresión lineal multivariada

df = pd.read_csv('../data/helados.csv', index_col=0)
temperatura = df["temp"].values
precio = df["price"].values
consumo = df["cons"].values

A = np.ones(shape=(temperatura.shape[0], 3))
A[:, 1] = temperatura
A[:, 2] = precio

x, _, _, _ = np.linalg.lstsq(A, consumo, rcond=None)
display(x)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(temperatura, precio, consumo); 
ax.set_xlabel('Temperatura [F]'); 
ax.set_ylabel('Precio');
ax.set_zlabel('Consumo promedio');
x_plot = np.linspace(np.amin(temperatura), np.amax(temperatura), num=10)
y_plot = np.linspace(np.amin(precio), np.amax(precio), num=10)
X_plot, Y_plot = np.meshgrid(x_plot, y_plot)
ax.plot_surface(X_plot, Y_plot, x[0] + x[1]*X_plot + x[2]*Y_plot, alpha=0.5)

# Regresión polinomial

import ipywidgets as widgets

fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
poly_basis = lambda x, M : np.vstack([x**k for k in range(M)]).T

def update_plot(M):
    ax.cla()
    ax.scatter(x, y)
    theta = np.linalg.lstsq(poly_basis(x, M), y, rcond=None)[0]
    ax.plot(x_plot, np.dot(poly_basis(x_plot, M), theta));
    
widgets.interact(update_plot, M=widgets.IntSlider(min=1, max=20));

# Validación

fig, ax = plt.subplots(1, 2, figsize=(7, 4), tight_layout=True)

np.random.seed(1234)
P = np.random.permutation(len(x))
train_idx, valid_idx = P[:len(x)//2], P[len(x)//2:]

poly_degree = np.arange(1, 10)
L = np.zeros(shape=(len(poly_degree), 2))

def mse(theta, Phi, Y):
    return np.mean(np.power(Y - np.dot(Phi, theta), 2))

for i, M in enumerate(poly_degree):
    Phi = poly_basis(x, M)
    theta_hat = np.linalg.lstsq(Phi[train_idx, :], y[train_idx], rcond=None)[0]
    L[i, 0] = mse(theta_hat, Phi[train_idx, :], y[train_idx])
    L[i, 1] = mse(theta_hat, Phi[valid_idx, :], y[valid_idx])
    
ax[0].plot(poly_degree, L[:, 0], label='Error de entrenamiento')
ax[0].plot(poly_degree, L[:, 1], label='Error de validación')
best_degree = np.argmin(L[:, 1])
ax[0].scatter(poly_degree[best_degree], L[best_degree, 1], c='k', label='Mejor')
ax[0].legend()
ax[0].set_yscale('log')
ax[0].set_xlabel('Grado del polinomio')

ax[1].scatter(x[train_idx], y[train_idx], label='Entrenamiento')
ax[1].scatter(x[valid_idx], y[valid_idx], label='Validación')
Phi = poly_basis(x, poly_degree[best_degree])
best_theta_hat = np.linalg.lstsq(Phi[train_idx, :], y[train_idx], rcond=None)[0]
ax[1].plot(x_plot, np.dot(poly_basis(x_plot, poly_degree[best_degree]), best_theta_hat))
ax[1].legend()