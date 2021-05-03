# Ajuste MLE con scipy.stats

x_plot = np.linspace(np.amin(x), np.amax(x), num=500)
dist = scipy.stats.norm
params = dist.fit(x)
print(dist.name, params)
p_plot = dist(*params[:-2], loc=params[-2], scale=params[-1]).pdf(x_plot)
ax.plot(x_plot, p_plot, label=dist.name)
plt.legend();

# kstest con scipy

z = (x-np.mean(x))/np.std(x)
ks_res = []
for dist in [scipy.stats.norm, scipy.stats.lognorm, scipy.stats.beta, 
             scipy.stats.gamma, scipy.stats.genextreme]:    
    params = dist.fit(z)
    fitted_dist = dist(*params[:-2], loc=params[-2], scale=params[-1])
    ks_res.append(scipy.stats.kstest(rvs=z, cdf=fitted_dist.cdf))
    print(dist.name, ks_res[-1], ks_res[-1].pvalue < 0.05)
    
    
# linregress    
fig, ax = plt.subplots(1, 3, figsize=(8, 3), tight_layout=True, sharey=True)
ax[0].set_ylabel(df.columns[0]);

for i, col in enumerate(df.columns[1:]):
    ax[i].scatter(df[col], df["consumo"])    
    res = scipy.stats.linregress(df[col], df["consumo"])
    ax[i].set_title("r: {0:0.5f}".format(res.rvalue))
    x_plot = np.linspace(np.amin(df[col]), np. amax(df[col]), num=100)
    ax[i].plot(x_plot, res.slope*x_plot + res.intercept, lw=4, alpha=0.5, c='k');
    ax[i].set_xlabel(col)

# Existe:    
#una correlación positiva alta entre consumo y temperatura
#una correlación negativa moderada entre consumo y precio
#una correlación cercana a cero entre consumo e ingreso