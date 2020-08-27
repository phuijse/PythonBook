import numpy as np
from sklearn.datasets import make_moons

def create_data(N):
    """
    Esta función retorna E y T, donde cada uno es una tupla con datos, etiquetas
    """
    x, y = make_moons(n_samples=N, shuffle=True, noise=0.25, random_state=1234)
    x = (x - np.mean(x, axis=0, keepdims=True))/np.std(x, axis=0, keepdims=True)
    
    return (x[:N//4], y[:N//4]), (x[N//4:], y[N//4:])


def KNN(X, Y, Z, k=5, p=2.):
    C = np.unique(Y)
    N, D = X.shape
    M, _ = Z.shape
    dist = np.zeros(shape=(M, N))
    for i in range(M):
        for j in range(N):
            dist[i, j] = np.power(np.sum(np.power(np.absolute(Z[i] - X[j]), p)), 1./p)
    neighbours = np.argsort(dist, axis=1)[:, :k]
    Z_Y = np.zeros(shape=(M, ))
    for i in range(M):
        criterion = np.zeros(shape=(len(C),))
        for c in C:
            criterion[c] = np.sum(1./dist[i, neighbours[i]][Y[neighbours[i]] == c])
        Z_Y[i] = np.argmax(criterion)
    return Z_Y
