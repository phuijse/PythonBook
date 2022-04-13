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

def fun(x):
    return dromedario(x[0], x[1])

def dromedario(x, y):
    return (4 -2.1*x**2+x**4/3)*x**2 +x*y + 4*y**2*(y**2 -1)

x = np.linspace(-2, 2, num=20)
y = np.linspace(-1, 1, num=20)
X, Y = np.meshgrid(x, y)
F = dromedario(X, Y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, F, cmap=plt.cm.Blues);
ax.set_xlabel('x')
ax.set_ylabel('y')

x0 = [-1.0, -1.0]
for x0 in [[-1, -1], [1, 1]]:
    res = scipy.optimize.minimize(fun, x0)
    print(x0, res.x, res.fun, res.message)
    ax.scatter(res.x[0], res.x[1], fun(res.x), s=200, label=f'$x_0$:{x0}');
ax.legend();

# Optimización con restricciones

def f(z):
    return -(2*z[0]*z[1] + 2*z[0] - z[0]**2 - 2*z[1]**2)

def df(z):
    return np.array([-2*z[1] - 2 + 2*z[0],
                     -2*z[0] + 4*z[1]])

cons = ({'type': 'eq', 
         'fun': lambda z: z[0]**3 - z[1], 
         'jac': lambda z: np.array([3*z[0]**2, -1.])
        },
        {'type': 'ineq',
         'fun': lambda z: z[1] - (z[0]-1)**4 - 2,
         'jac': lambda z: np.array([-4*(z[0]-1)**3, 1.])
        })

bnds = ((0.5, 1.5), (1.5, 2.5))

x0 = np.array([0, 1])

res1 = scipy.optimize.minimize(f, x0, jac=df)
res2 = scipy.optimize.minimize(f, x0, jac=df, 
                               method='L-BFGS-B', bounds=bnds)
res3 = scipy.optimize.minimize(f, x0, jac=df,
                               method='SLSQP', bounds=bnds, constraints=cons)

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