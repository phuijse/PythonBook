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
    print(dist.name, ks_res[-1])