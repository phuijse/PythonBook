# Ejercicio interact

fig, ax = plt.subplots(figsize=(6, 3), tight_layout=True)

time = np.linspace(0, 3, num=500); 
twopift = 2.0*np.pi*time
line = ax.plot(time, 3*np.cos(twopift))

def plot_sinewave(A1, A2, A3, phi):
    data = A1*np.cos(twopift + phi) + A2*np.cos(2*twopift + phi) + A3*np.cos(3*twopift + phi)
    line[0].set_ydata(data)

slider_layout = widgets.Layout(width='600px', height='20px')
A = [widgets.FloatSlider(description=r'$A_{0}$'.format(i), min=0.0, max=1.0, 
                         step=0.01, value=0.0, layout=slider_layout) for i in range(3)]
phi = widgets.FloatSlider(description=r'$\phi$', min=0.0, max=2*np.pi, step=0.1, layout=slider_layout)
widgets.interact(plot_sinewave, A1=A[0], A2=A[1], A3=A[2], phi=phi);

# Ejercicio observe

import ipywidgets as widgets

fig, ax = plt.subplots(figsize=(5, 3), tight_layout=True)

poly = {'a': 1., 'b': 1., 'c': 1.}

def update_plot():
    ax.cla()
    x = np.arange(-2, 2, step=0.1)
    ax.plot(x, poly['a']*x**2 + poly['b']*x+ poly['c'])
    ax.set_title(f"{poly['a']}$x^2$ + {poly['b']}$x$ + {poly['c']}")

update_plot()        

def handler(change):    
    poly[change.owner.description] = change['new']
    update_plot()

params = [widgets.FloatText(description=name) for name in 'abc']
for param in params:
    param.observe(handler, names='value')
display(widgets.VBox(params))
