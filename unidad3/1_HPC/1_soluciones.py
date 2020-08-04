
# Midiendo tiempo con %timeit
from fractal import make_fractal, evaluate_z

# Parte 1
N = [5, 10, 50, 100, 500]
fig, ax = plt.subplots(len(N), 1, figsize=(4, 8), tight_layout=True)
for k, n in enumerate(N):
    fractal_image = make_fractal(n, maxiters=50)    
    ax[k].imshow(fractal_image, aspect='equal', cmap=plt.cm.viridis, origin='lower')
    ax[k].axis('off');

# Parte 2
%timeit -r10 make_fractal(N=500, maxiters=50)

# Parte 3
results = []
for k, n in enumerate(N):
    result = %timeit -r10 -q -o make_fractal(n, maxiters=50)
    results.append(result)
    
for n, result in zip(N, results):
    print(n, result.best, result.average, result.worst)

# Parte 4
fig, ax = plt.subplots(figsize=(5, 3), tight_layout=True)
ax.errorbar(N,
            [result.average for result in results],
            [result.stdev for result in results])
ax.set_xlabel('N')
ax.set_ylabel('Tiempo [s]')
ax.set_xscale('log')
ax.set_yscale('log')


# Midiendo tiempo con lprun

%load_ext line_profiler
%lprun -f make_fractal make_fractal(N=500, maxiters=50)
# La linea más costosa es la 20: row.append(evaluate_z(zi, zr, maxiters))
# Usa casi el 90% del tiempo total

%lprun -f evaluate_z make_fractal(N=500, maxiters=50)