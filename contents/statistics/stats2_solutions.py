# Probabilidades

#1. nominal, continua, continua
# diagnosis = ['M', 'B']
hrange = [[df["radius1"].min(), df["radius1"].max()], 
          [df["texture1"].min(), df["texture1"].max()]]

#2
def ECDF(x):
    x = np.sort(x)
    n = len(x)
    def result(a):
        return np.searchsorted(x, a, side='right')/n
    return result

rango_radius = np.linspace(df["radius1"].min(), df["radius1"].max())

fig, ax = plt.subplots()
for diag in ['M', 'B']:
    sample = df.loc[df.diagnosis==diag]["radius1"]
    cumprob = np.cumsum(counts).astype(np.double) / sample.size
    ax.plot(rango_radius, ECDF(sample)(rango_radius), label=diag)
ax.set_xlabel('Radio')
ax.legend()

#3.
for diag in ["M", "B"]:
    sample = df.loc[df.diagnosis==diag]["radius1"]
    print(diag, ECDF(sample)(15.))
    
#4.
for diag in ["M", "B"]:
    sample = df.loc[df.diagnosis==diag]["texture1"]
    print(diag, ECDF(sample)(20.) - ECDF(sample)(10.))
    
#5.
# Fe de erratas: Estoy asumiendo P(A y B) = P(A)P(B) Es decir que las probabilidades de ambos eventos son independientes
# Pero en la práctica es un supuesto que debemos comprobar
for diag in ["M", "B"]:
    sample = df.loc[df.diagnosis==diag][["radius1", "texture1"]].values
    print(diag, ECDF(sample[:, 0])(15.)*(ECDF(sample[:, 1])(20.) - ECDF(sample[:, 1])(10.)))
    


# Histogramas

fig, ax = plt.subplots(figsize=(6, 3), tight_layout=True)
ax.hist(df.loc[df.diagnosis=='M']["radius1"], alpha=0.5, label='Maligno', density=True)
ax.hist(df.loc[df.diagnosis=='B']["radius1"], alpha=0.5, label='Benigno', density=True)
ax.set_xlabel('Radio')
ax.legend();

fig, ax = plt.subplots(figsize=(6, 3), tight_layout=True)
ax.hist(df.loc[df.diagnosis=='M']["texture1"], alpha=0.5, label='Maligno', density=True)
ax.hist(df.loc[df.diagnosis=='B']["texture1"], alpha=0.5, label='Benigno', density=True)
ax.set_xlabel('Textura')
ax.legend();

fig, ax = plt.subplots(1, 2, figsize=(6, 3), tight_layout=True, sharex=True, sharey=True)

hrange = [[df["radius1"].min(), df["radius1"].max()], 
          [df["texture1"].min(), df["texture1"].max()]]

print(hrange)
ax[0].hist2d(df.loc[df.diagnosis=='M']["radius1"], 
             df.loc[df.diagnosis=='M']["texture1"], 
             cmap=plt.cm.Blues, alpha=0.5, label='Maligno', bins=15, range=hrange)
ax[1].hist2d(df.loc[df.diagnosis=='B']["radius1"],
             df.loc[df.diagnosis=='B']["texture1"], 
             cmap=plt.cm.Oranges, alpha=0.5, label='Benigno', bins=15, range=hrange)
ax[0].set_xlabel('Radius')
ax[0].set_ylabel('Textura');

# Dados y Teorema central del límite

import scipy.stats
import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots(figsize=(8, 3))

def update_plot(k):
    ax.cla()
    ax.set_title("Promedio de {0} lanzamiento/s de dado".format(k+1))
    dist = scipy.stats.multinomial(n=k+1, p=[1/6]*6)
    repeats = dist.rvs(size=1000)
    average_dice = np.sum(repeats*range(1, 7)/(k+1), axis=1)
    ax.hist(average_dice, bins=12, density=True)
    ax.set_xlim([1, 6])

anim = animation.FuncAnimation(fig, update_plot, frames=15, interval=1000, 
                               repeat=True, blit=False)