
# Midiendo tiempo con %timeit


# Parte 1
for N in [5, 10, 50, 100, 500]:
    fractal_image = make_fractal(N, maxiters=50)
    fig, ax = plt.subplots(figsize=(8, 4), tight_layout=True)
    ax.imshow(fractal_image, aspect='equal', cmap=plt.cm.viridis, origin='lower')
    ax.axis('off');

# Parte 2
%timeit -r10 -n5 make_fractal(N=500, maxiters=50)

# Parte 3
times = []
N = [5, 10, 50, 100, 500]
for n in N:
    result = %timeit -r10 -n5 -o -q make_fractal(N=n, maxiters=50)
    times.append(result)
    
fig, ax = plt.subplots()
ax.errorbar(N, 
            [time.average for time in times],  
            [time.stdev for time in times])
ax.set_xlabel('N')
ax.set_ylabel('Tiempo [s]')
ax.set_yscale('log')
ax.set_xscale('log')


# Midiendo tiempo con lprun

%load_ext line_profiler
%lprun -f make_fractal make_fractal(N=500, maxiters=50)
# La linea más costosa es la 20: row.append(evaluate_z(zi, zr, maxiters))
# Usa casi el 90% del tiempo total

%lprun -f evaluate_z make_fractal(N=500, maxiters=50)