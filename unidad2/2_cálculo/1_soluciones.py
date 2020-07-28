# Optimización sin restricciones 1

import scipy.optimize

f = lambda x : x**2 - 2*x + 5*np.sin(2*x)
df = lambda x : 2*x - 2 + 10*np.cos(2*x)

fig, ax = plt.subplots(1, figsize=(7, 2), tight_layout=True, sharex=True)
x_plot = np.linspace(-5, 8, num=100)
ax.plot(x_plot, f(x_plot))

for x0 in [-4, 0, 4, 6]:
    res = scipy.optimize.minimize(f, x0, jac=df,
                                  options={'disp':False})

    print(x0, res.x[0], res.fun, res.message)
    ax.scatter(res.x, f(res.x), s=100, label=f'$x_0$={x0}')
ax.legend();

# Optimización sin restricciones 2

from mpl_toolkits.mplot3d import Axes3D  
import scipy.optimize

def fun(x):
    return dromedario(x[0], x[1])

def dromedario(x, y):
    return (4 -2.1*x**2+x**4/3)*x**2 +x*y + 4*y**2*(y**2 -1)

x = np.linspace(-2, 2, num=20)
y = np.linspace(-1, 1, num=20)
X, Y = np.meshgrid(x, y)
F = (4 -2.1*A**2+A**4/3)*A**2 +A*B + (4*B**2 -4)*B**2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, dromedario(X, Y), cmap=plt.cm.Blues);
ax.set_xlabel('x')
ax.set_ylabel('y')

x0 = [-1.0, -1.0]
for x0 in [[-1, -1], [1, 1]]:
    res = scipy.optimize.minimize(fun, x0)
    print(x0, res.x, res.fun, res.message)
    ax.scatter(res.x[0], res.x[1], fun(res.x), s=200, label=f'$x_0$:{x0}');
ax.legend();

# Optimización con restricciones

import scipy.optimize

def f(x):
    return -(2*x[0]*x[1] + 2*x[0] - x[0]**2 - 2*x[1]**2)

cons = ({'type': 'eq',
         'fun' : lambda x: np.array([x[0]**3 - x[1]]),
         'jac' : lambda x: np.array([3.0*(x[0]**2.0), -1.0])},
        {'type': 'ineq',
         'fun' : lambda x: np.array([x[1] - (x[0]-1)**4 - 2])})

bnds = ((0.5, 1.5), (1.5, 2.5))
x0 = np.array([0, 1])
res1 = scipy.optimize.minimize(f, x0, method='BFGS', 
                              options={'disp':True})
res2 = scipy.optimize.minimize(f, x0, method='L-BFGS-B', bounds=bnds,
                              options={'disp':True})
res3 = scipy.optimize.minimize(f, x0, method='SLSQP', 
                              constraints=cons, bounds=bnds,
                              options={'disp':True})
display(res1.x, res2.x, res3.x)

x = np.linspace(0, 3, 100)
y = np.linspace(0, 3, 100)
A, B = np.meshgrid(x, y)
C = f(np.vstack([A.ravel(), B.ravel()])).reshape((100,100))
fig, ax = plt.subplots(figsize=(5, 3))
ax.contourf(A, B, C, cmap=plt.cm.Blues);
ax.plot(x, x**3, 'k--', lw=2)
ax.plot(x, 2+(x-1)**4, 'k:', lw=2)
ax.fill([0.5, 0.5, 1.5, 1.5], [2.5, 1.5, 1.5, 2.5], alpha=0.3)
ax.axis([0, 3, 0, 3])
ax.scatter(res1.x[0], res1.x[1], s=20, c='b', label='BFGS');
ax.scatter(res2.x[0], res2.x[1], s=20, c='g', label='L-BFGS-B');
ax.scatter(res3.x[0], res3.x[1], s=20, c='r', label='SLSQP');
plt.legend();